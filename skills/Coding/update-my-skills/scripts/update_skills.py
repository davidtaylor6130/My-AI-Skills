#!/usr/bin/env python3
"""Install David's current GitHub skills and global Codex instructions."""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


REMOTE = "https://github.com/davidtaylor6130/My-AI-Skills.git"
BRANCH = "main"
NAME = re.compile(r"^name:\s*[\"']?([a-z0-9]+(?:-[a-z0-9]+)*)[\"']?\s*$", re.MULTILINE)
AGENT_BEGIN = "<!-- BEGIN: My AI Skills agents/Agent.md (managed) -->"
AGENT_END = "<!-- END: My AI Skills agents/Agent.md (managed) -->"


def git(*args: str, capture: bool = False) -> str:
    result = subprocess.run(
        ["git", *args], check=True, text=True, capture_output=capture
    )
    return result.stdout.strip() if capture else ""


def update_checkout(checkout: Path) -> None:
    checkout.parent.mkdir(parents=True, exist_ok=True)
    if not checkout.exists():
        with tempfile.TemporaryDirectory(dir=checkout.parent) as temporary:
            clone = Path(temporary) / "repo"
            git("clone", "--filter=blob:none", "--branch", BRANCH, REMOTE, str(clone))
            shutil.move(str(clone), checkout)
        return

    if not (checkout / ".git").is_dir():
        raise RuntimeError(f"Managed checkout is not a Git repository: {checkout}")
    origin = git("-C", str(checkout), "remote", "get-url", "origin", capture=True)
    if origin != REMOTE:
        raise RuntimeError(f"Managed checkout has unexpected origin: {origin}")
    if git("-C", str(checkout), "status", "--porcelain", capture=True):
        raise RuntimeError(f"Managed checkout has local changes: {checkout}")
    git("-C", str(checkout), "fetch", "--prune", "origin", BRANCH)
    git("-C", str(checkout), "checkout", BRANCH)
    git("-C", str(checkout), "merge", "--ff-only", f"origin/{BRANCH}")


def discover_skills(checkout: Path) -> dict[str, Path]:
    skills: dict[str, Path] = {}
    for manifest in sorted((checkout / "skills").rglob("SKILL.md")):
        match = NAME.search(manifest.read_text(encoding="utf-8"))
        if not match:
            raise RuntimeError(f"Missing valid skill name: {manifest}")
        name = match.group(1)
        if manifest.parent.name != name:
            raise RuntimeError(f"Skill folder does not match name {name}: {manifest.parent}")
        if name in skills:
            raise RuntimeError(f"Duplicate skill name: {name}")
        skills[name] = manifest.parent
    if not skills:
        raise RuntimeError("The managed checkout contains no skills")
    return skills


def move_aside(target: Path, backup: Path) -> None:
    if not (target.exists() or target.is_symlink()):
        return
    backup.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(target), str(backup))


def link(source: Path, target: Path, backup: Path) -> bool:
    if target.is_symlink() and target.resolve(strict=False) == source.resolve():
        return False
    move_aside(target, backup)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.symlink_to(source, target_is_directory=source.is_dir())
    return True


def install_agent(source: Path, target: Path, backup: Path) -> bool:
    block = f"{AGENT_BEGIN}\n{source.read_text(encoding='utf-8').strip()}\n{AGENT_END}"
    existing = target.read_text(encoding="utf-8") if target.exists() else ""
    start = existing.find(AGENT_BEGIN)
    end = existing.find(AGENT_END)
    if (start >= 0) != (end >= 0) or (start >= 0 and end < start):
        raise RuntimeError(f"Malformed managed Agent.md block: {target}")
    if start >= 0:
        end += len(AGENT_END)
        remainder = existing[:start] + existing[end:]
    else:
        remainder = existing
    updated = block + (f"\n\n{remainder.lstrip(chr(10))}" if remainder.strip() else "\n")
    if updated == existing:
        return False
    move_aside(target, backup)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(updated, encoding="utf-8")
    return True


def install(checkout: Path) -> tuple[int, list[str], Path | None, bool]:
    home = Path.home()
    skills_home = home / ".agents" / "skills"
    codex_home = Path(os.environ.get("CODEX_HOME", home / ".codex")).expanduser()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup_root = home / ".agents" / "backups" / "update-my-skills" / stamp
    removed: list[str] = []

    skills = discover_skills(checkout)
    agent_source = checkout / "agents" / "Agent.md"
    if not agent_source.is_file() or not agent_source.read_text(encoding="utf-8").strip():
        raise RuntimeError(f"Missing or empty agent instructions: {agent_source}")

    for name, source in skills.items():
        link(source, skills_home / name, backup_root / "skills" / name)

    if skills_home.exists():
        for target in skills_home.iterdir():
            if not target.is_symlink() or target.name in skills:
                continue
            resolved = target.resolve(strict=False)
            if resolved == checkout or checkout in resolved.parents:
                target.unlink()
                removed.append(target.name)

    install_agent(agent_source, codex_home / "AGENTS.md", backup_root / "codex" / "AGENTS.md")

    override = codex_home / "AGENTS.override.md"
    override_updated = False
    if override.is_file() and override.read_text(encoding="utf-8").strip():
        override_updated = install_agent(
            agent_source, override, backup_root / "codex" / "AGENTS.override.md"
        )

    backup = backup_root if backup_root.exists() else None
    return len(skills), removed, backup, override_updated


def main() -> int:
    if shutil.which("git") is None:
        print("ERROR: git is required", file=sys.stderr)
        return 1

    checkout = Path.home() / ".agents" / "repos" / "my-ai-skills"
    try:
        update_checkout(checkout)
        count, removed, backup, override_updated = install(checkout)
        commit = git("-C", str(checkout), "rev-parse", "--short", "HEAD", capture=True)
    except (OSError, RuntimeError, subprocess.CalledProcessError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Installed {count} skills from {commit}.")
    if backup:
        print(f"Backups: {backup}")
    if removed:
        print(f"Removed stale managed links: {', '.join(removed)}")
    if override_updated:
        print("AGENTS.override.md also refreshed because it overrides AGENTS.md.")
    print("AGENTS.md is installed. Start a new Codex session to load it.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
