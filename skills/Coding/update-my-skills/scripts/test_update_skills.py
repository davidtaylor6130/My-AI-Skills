#!/usr/bin/env python3
"""Small isolated check for the local installation behavior."""

import os
import tempfile
from pathlib import Path

from update_skills import install


def main() -> None:
    original_home = os.environ.get("HOME")
    original_codex_home = os.environ.get("CODEX_HOME")
    try:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            checkout = root / "checkout"
            skill = checkout / "skills" / "Coding" / "demo"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text(
                "---\nname: demo\ndescription: Test.\n---\n", encoding="utf-8"
            )
            (checkout / "agents").mkdir()
            agent = checkout / "agents" / "Agent.md"
            agent.write_text("Use the demo instructions.\n", encoding="utf-8")

            os.environ["HOME"] = str(root / "home")
            os.environ.pop("CODEX_HOME", None)
            home = Path(os.environ["HOME"])
            codex_home = home / ".codex"
            codex_home.mkdir(parents=True)
            (codex_home / "AGENTS.md").write_text(
                "Keep the machine-local instructions.\n", encoding="utf-8"
            )
            (codex_home / "AGENTS.override.md").write_text(
                "Keep the temporary override.\n", encoding="utf-8"
            )
            count, removed, backup, override_updated = install(checkout)

            assert count == 1 and not removed
            assert (home / ".agents" / "skills" / "demo").resolve() == skill.resolve()
            installed_agent = (codex_home / "AGENTS.md").read_text(encoding="utf-8")
            assert installed_agent.startswith("<!-- BEGIN: My AI Skills")
            assert "Use the demo instructions." in installed_agent
            assert installed_agent.endswith("Keep the machine-local instructions.\n")
            installed_override = (codex_home / "AGENTS.override.md").read_text(encoding="utf-8")
            assert "Use the demo instructions." in installed_override
            assert installed_override.endswith("Keep the temporary override.\n")
            assert backup is not None and override_updated
            assert (backup / "codex" / "AGENTS.md").read_text(encoding="utf-8") == (
                "Keep the machine-local instructions.\n"
            )
    finally:
        if original_home is None:
            os.environ.pop("HOME", None)
        else:
            os.environ["HOME"] = original_home
        if original_codex_home is None:
            os.environ.pop("CODEX_HOME", None)
        else:
            os.environ["CODEX_HOME"] = original_codex_home


if __name__ == "__main__":
    main()
