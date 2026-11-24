#!/usr/bin/env python3
"""Regression: a review must not build after the diff it covered has changed."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parent / "build_review.py"


def run(repo: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(list(args), cwd=repo, capture_output=True, text=True)


class StaleReviewTest(unittest.TestCase):
    def test_changed_diff_blocks_build_until_reviewed_again(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            run(repo, "git", "init", "-q", "-b", "main")
            (repo / "a.txt").write_text("one\n")
            run(repo, "git", "add", "-A")
            run(repo, "git", "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", "init")
            review_path = repo / ".UAM/AINotes/review-main.json"

            (repo / "a.txt").write_text("two\n")
            run(repo, sys.executable, str(SCRIPT), "skeleton")
            review = json.loads(review_path.read_text())
            review.update(title="t", summary="s", unchecked="u", reviewer="author")
            for change in review["changes"]:
                change.update(title="t", why="w", review="r", risk="low")
                for check in change["checks"]:
                    check.update(verdict="pass", note="n", evidence="a.txt:1")
            review_path.write_text(json.dumps(review))
            self.assertEqual(run(repo, sys.executable, str(SCRIPT), "build", str(review_path)).returncode, 0)

            (repo / "a.txt").write_text("three\n")
            stale = run(repo, sys.executable, str(SCRIPT), "build", str(review_path))
            self.assertIn("diff changed since it was reviewed", stale.stderr)

            refreshed = run(repo, sys.executable, str(SCRIPT), "skeleton")
            self.assertIn("STALE", refreshed.stdout)
            rebuilt = run(repo, sys.executable, str(SCRIPT), "build", str(review_path))
            self.assertNotEqual(rebuilt.returncode, 0, "stale review built after skeleton refresh")


if __name__ == "__main__":
    unittest.main()
