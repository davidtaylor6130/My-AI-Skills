#!/usr/bin/env python3
"""Build a static HTML review of the current branch's changes.

skeleton: write one JSON entry per changed file for the AI to fill in.
build:    validate the filled JSON, attach the real git diffs, write the HTML.

Diffs always come from git, never from the JSON, so the page cannot show a
diff that does not exist.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


TEMPLATE = Path(__file__).resolve().parent / "template.html"
NOTES_DIR = ".UAM/AINotes"
REQUIRED_CHECKS = ("Knock-on", "Conventions")
VERDICTS = ("pass", "concern", "fail")
RISKS = ("high", "medium", "low")
REVIEWERS = ("independent", "author")
UAM_VIEW_LIMIT = 131072


def git(root: Path | None, *args: str, ok: tuple[int, ...] = (0,)) -> str:
    result = subprocess.run(
        ["git", *args], cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace"
    )
    if result.returncode not in ok:
        sys.exit(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout


def changed_files(root: Path, base: str) -> tuple[str, dict[str, str]]:
    """Return the merge base and {path: diff} for committed, uncommitted and untracked changes."""
    merge_base = git(root, "merge-base", base, "HEAD").strip()
    tracked = git(root, "diff", "--name-only", "--no-renames", "-z", merge_base).split("\0")
    untracked = git(root, "ls-files", "--others", "--exclude-standard", "-z").split("\0")
    diffs: dict[str, str] = {}
    for path in tracked + untracked:
        # The review's own working files are not part of the change.
        if not path or path.startswith(NOTES_DIR + "/"):
            continue
        if path in untracked:
            raw = git(root, "diff", "--no-color", "--no-index", "--", "/dev/null", path, ok=(0, 1))
        else:
            raw = git(root, "diff", "--no-color", "--no-renames", merge_base, "--", path)
        lines = raw.rstrip("\n").split("\n")
        first_hunk = next((i for i, line in enumerate(lines) if line.startswith("@@")), 1)
        diffs[path] = "\n".join(lines[first_hunk:])
    return merge_base, diffs


def diff_id(path: str, diff: str) -> str:
    """Stable id for one file's diff. Changes when the diff changes, which marks a review stale."""
    return "c" + hashlib.sha1(f"{path}\n{diff}".encode("utf-8")).hexdigest()[:10]


def skeleton(args: argparse.Namespace) -> None:
    root = Path(git(None, "rev-parse", "--show-toplevel").strip())
    branch = git(root, "rev-parse", "--abbrev-ref", "HEAD").strip()
    _, diffs = changed_files(root, args.base)
    if not diffs:
        sys.exit(f"No changes against {args.base}.")

    slug = re.sub(r"[^A-Za-z0-9]+", "-", branch).strip("-")
    out = Path(args.out) if args.out else root / NOTES_DIR / f"review-{slug}.json"
    old = json.loads(out.read_text(encoding="utf-8")) if out.exists() else {}
    old_changes = {change["file"]: change for change in old.get("changes", [])}

    changes, stale = [], []
    for path, diff in diffs.items():
        change = old_changes.get(path) or {
            "file": path, "title": "", "risk": "", "why": "",
            "checks": [{"kind": kind, "verdict": "", "note": "", "evidence": ""} for kind in REQUIRED_CHECKS],
            "review": "",
        }
        if change.get("id") not in (None, diff_id(path, diff)):
            # The reviewed diff no longer exists: clear the verdicts so build refuses until it is reviewed again.
            stale.append(path)
            checks = [{**check, "verdict": "", "note": "", "evidence": ""} for check in change.get("checks", [])]
            change = {**change, "risk": "", "review": "", "checks": checks}
        changes.append({**change, "id": diff_id(path, diff)})

    review = {
        "id": slug, "title": old.get("title", ""), "branch": branch, "base": args.base,
        "reviewer": old.get("reviewer", ""), "summary": old.get("summary", ""),
        "unchecked": old.get("unchecked", ""), "changes": changes,
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(review, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{out}\n{len(changes)} files to review.")
    for path in stale:
        print(f"STALE, diff changed, review fields cleared: {path}")


def validate(review: dict, diffs: dict[str, str]) -> list[str]:
    errors = [f"{key}: empty" for key in ("title", "summary", "unchecked") if not str(review.get(key, "")).strip()]
    if review.get("reviewer") not in REVIEWERS:
        errors.append(f"reviewer: must be one of {', '.join(REVIEWERS)}")

    entries = {change.get("file"): change for change in review.get("changes", [])}
    errors += [f"{path}: changed in git but has no entry, rerun skeleton" for path in diffs if path not in entries]
    for path, change in entries.items():
        if path not in diffs:
            errors.append(f"{path}: has an entry but is not changed in git, rerun skeleton")
            continue
        if change.get("id") != diff_id(path, diffs[path]):
            errors.append(f"{path}: diff changed since it was reviewed, rerun skeleton and review it again")
        errors += [f"{path}: {key} empty" for key in ("title", "why", "review") if not str(change.get(key, "")).strip()]
        if change.get("risk") not in RISKS:
            errors.append(f"{path}: risk must be one of {', '.join(RISKS)}")
        checks = change.get("checks", [])
        kinds = [check.get("kind") for check in checks]
        errors += [f"{path}: missing {kind} check" for kind in REQUIRED_CHECKS if kind not in kinds]
        for check in checks:
            label = f"{path}: {check.get('kind') or 'unnamed'} check"
            if check.get("verdict") not in VERDICTS:
                errors.append(f"{label} verdict must be one of {', '.join(VERDICTS)}")
            errors += [f"{label} {key} empty" for key in ("note", "evidence") if not str(check.get(key, "")).strip()]
    return errors


def build(args: argparse.Namespace) -> None:
    source = Path(args.review)
    review = json.loads(source.read_text(encoding="utf-8"))
    root = Path(git(None, "rev-parse", "--show-toplevel").strip())
    _, diffs = changed_files(root, review.get("base", "main"))

    errors = validate(review, diffs)
    if errors:
        sys.exit("Review not built. Fix:\n" + "\n".join(f"  {error}" for error in errors))

    for change in review["changes"]:
        change["diff"] = diffs[change["file"]]
    review["changes"].sort(key=lambda change: RISKS.index(change["risk"]))

    # Escaping "<" keeps "</script>" in a diff from ending the data block.
    data = json.dumps(review, ensure_ascii=False).replace("<", "\\u003c")
    out = Path(args.out) if args.out else source.with_suffix(".html")
    out.write_text(TEMPLATE.read_text(encoding="utf-8").replace("__REVIEW_DATA__", data), encoding="utf-8")
    print(out)
    if out.stat().st_size > UAM_VIEW_LIMIT:
        print(f"{out.stat().st_size} bytes: over the UAM HTML view limit, open it in a browser.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)
    skeleton_parser = commands.add_parser("skeleton", help="write or refresh the review JSON")
    skeleton_parser.add_argument("--base", default="main", help="branch the work started from (default: main)")
    skeleton_parser.add_argument("--out", help=f"default: {NOTES_DIR}/review-<branch>.json")
    skeleton_parser.set_defaults(run=skeleton)
    build_parser = commands.add_parser("build", help="validate the review JSON and write the HTML")
    build_parser.add_argument("review", help="path to the filled review JSON")
    build_parser.add_argument("--out", help="default: the JSON path with .html")
    build_parser.set_defaults(run=build)
    args = parser.parse_args()
    args.run(args)


if __name__ == "__main__":
    main()
