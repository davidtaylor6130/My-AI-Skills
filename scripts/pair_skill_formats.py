#!/usr/bin/env python3
"""Pair every SKILL.md with a UAM file containing the same instructions."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def split_document(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError(f"{path}: missing YAML frontmatter")
    header, body = text[4:].split("\n---\n", 1)
    return header, body.lstrip("\n").rstrip() + "\n"


def fields(header: str) -> dict[str, str]:
    result: dict[str, str] = {}
    lines = header.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        index += 1
        if not line or line[0].isspace() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if value in {"|", ">"}:
            block: list[str] = []
            while index < len(lines) and (not lines[index] or lines[index][0].isspace()):
                block.append(lines[index].strip())
                index += 1
            value = ("\n" if value == "|" else " ").join(block).strip()
        elif value.startswith('"'):
            value = json.loads(value)
        result[key] = value
    return result


def title_from(body: str, fallback: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].removeprefix("Skill: ").strip()
    return fallback.replace("-", " ").title()


def write_skill(path: Path, name: str, description: str, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"---\nname: {name}\ndescription: {json.dumps(description, ensure_ascii=False)}\n---\n\n{body}",
        encoding="utf-8",
    )


def write_uam(path: Path, name: str, description: str, body: str, group: str) -> None:
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    relative = path.relative_to(ROOT).as_posix()
    header = [
        "uamVersion: V1 Imported",
        f"title: {json.dumps(title_from(body, name), ensure_ascii=False)}",
        "maker: AutoImporter",
        f"review: {json.dumps(description, ensure_ascii=False)}",
        f"dateCreated: {now}",
        f"dateUpdated: {now}",
        "favorite: false",
        "sourceProvider: Standard Skill",
        f"sourcePath: {relative}",
        f"commandName: {name}",
        f"group: {group}",
    ]
    path.write_text(f"---\n{'\n'.join(header)}\n---\n\n{body}", encoding="utf-8")


def normalize_standard_folder(manifest: Path, write: bool) -> Path:
    name = fields(split_document(manifest)[0]).get("name", "")
    if not SLUG.fullmatch(name):
        raise ValueError(f"{manifest}: invalid skill name {name!r}")
    if manifest.parent.name == name:
        return manifest
    target = manifest.parent.parent / name
    if target.exists():
        if not manifest.parent.samefile(target):
            raise ValueError(f"Cannot rename {manifest.parent} to existing {target}")
        temporary = manifest.parent.parent / f".{name}-case-rename"
        if temporary.exists():
            raise ValueError(f"Cannot use existing temporary path {temporary}")
        print(f"rename {manifest.parent.relative_to(ROOT)} -> {target.relative_to(ROOT)}")
        if write:
            manifest.parent.rename(temporary)
            temporary.rename(target)
        return target / "SKILL.md"
    print(f"rename {manifest.parent.relative_to(ROOT)} -> {target.relative_to(ROOT)}")
    if write:
        manifest.parent.rename(target)
    return target / "SKILL.md"


def create_missing_pairs(write: bool) -> None:
    for manifest in sorted(SKILLS.rglob("SKILL.md")):
        header, body = split_document(manifest)
        metadata = fields(header)
        name = metadata.get("name", "")
        uam = manifest.parent / f"{name}.uam"
        if not uam.exists():
            print(f"create {uam.relative_to(ROOT)}")
            if write:
                write_uam(uam, name, metadata.get("description", ""), body, manifest.parts[len(SKILLS.parts)])

    for uam in sorted(SKILLS.rglob("*.uam")):
        manifest = uam.parent / "SKILL.md"
        if manifest.exists():
            continue
        header, body = split_document(uam)
        metadata = fields(header)
        print(f"create {manifest.relative_to(ROOT)}")
        if write:
            write_skill(manifest, metadata["commandName"], metadata["review"], body)


def replace_field(header: str, key: str, value: str) -> str:
    replacement = f"{key}: {value}"
    lines = header.splitlines()
    for index, line in enumerate(lines):
        if line.startswith(f"{key}:"):
            lines[index] = replacement
            return "\n".join(lines)
    lines.append(replacement)
    return "\n".join(lines)


def sync_pairs(write: bool) -> None:
    for manifest in sorted(SKILLS.rglob("SKILL.md")):
        skill_header, skill_body = split_document(manifest)
        skill_fields = fields(skill_header)
        name = skill_fields["name"]
        description = skill_fields.get("description", "")
        uam = manifest.parent / f"{name}.uam"
        uam_header, uam_body = split_document(uam)
        uam_fields = fields(uam_header)
        source_path = uam.relative_to(ROOT).as_posix()
        changed = any(
            (
                uam_fields.get("commandName") != name,
                uam_fields.get("review") != description,
                uam_fields.get("sourcePath") != source_path,
                uam_body != skill_body,
            )
        )
        if not changed:
            continue
        updated_header = replace_field(uam_header, "commandName", name)
        updated_header = replace_field(
            updated_header, "review", json.dumps(description, ensure_ascii=False)
        )
        updated_header = replace_field(updated_header, "sourcePath", source_path)
        now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
        updated_header = replace_field(updated_header, "dateUpdated", now)
        print(f"sync {uam.relative_to(ROOT)} from SKILL.md")
        if write:
            uam.write_text(f"---\n{updated_header}\n---\n\n{skill_body}", encoding="utf-8")


def validate() -> list[str]:
    errors: list[str] = []
    manifests = sorted(SKILLS.rglob("SKILL.md"))
    uams = sorted(SKILLS.rglob("*.uam"))
    for manifest in manifests:
        skill_header, skill_body = split_document(manifest)
        name = fields(skill_header).get("name", "")
        uam = manifest.parent / f"{name}.uam"
        if not uam.exists():
            errors.append(f"{manifest.relative_to(ROOT)} has no {name}.uam")
            continue
        uam_header, uam_body = split_document(uam)
        uam_fields = fields(uam_header)
        if uam_fields.get("commandName") != name:
            errors.append(f"{uam.relative_to(ROOT)} commandName does not match {name}")
        if uam_fields.get("review") != fields(skill_header).get("description", ""):
            errors.append(f"{uam.relative_to(ROOT)} review does not match description")
        if uam_fields.get("sourcePath") != uam.relative_to(ROOT).as_posix():
            errors.append(f"{uam.relative_to(ROOT)} sourcePath is stale")
        if skill_body != uam_body:
            errors.append(f"{manifest.parent.relative_to(ROOT)} bodies differ")
    for uam in uams:
        if not (uam.parent / "SKILL.md").exists():
            errors.append(f"{uam.relative_to(ROOT)} has no SKILL.md")
    if len(manifests) != len(uams):
        errors.append(f"format counts differ: {len(manifests)} standard, {len(uams)} UAM")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="create and normalize missing pairs")
    args = parser.parse_args()

    if args.write:
        manifests = list(SKILLS.rglob("SKILL.md"))
        for manifest in manifests:
            normalize_standard_folder(manifest, True)
        create_missing_pairs(True)
        sync_pairs(True)

    errors = validate()
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print(f"Valid: {len(list(SKILLS.rglob('SKILL.md')))} paired skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
