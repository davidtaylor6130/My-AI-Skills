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


def migrate_uam_files(write: bool) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for source in sorted((SKILLS / "Marketing").rglob("*.uam")):
        header, _ = split_document(source)
        name = fields(header).get("commandName", "")
        if not SLUG.fullmatch(name):
            raise ValueError(f"{source}: invalid commandName {name!r}")
        if source.parent.name == name and (source.parent / "SKILL.md").exists():
            continue
        target = source.parent / name / f"{name}.uam"
        if target.exists():
            raise ValueError(f"Cannot move {source} over {target}")
        old_relative = source.relative_to(SKILLS / "Marketing").as_posix()
        new_relative = target.relative_to(SKILLS / "Marketing").as_posix()
        mapping[old_relative] = new_relative
        mapping[f"marketing/{old_relative}"] = f"skills/Marketing/{new_relative}"
        mapping[f"skills/Marketing/{old_relative}"] = f"skills/Marketing/{new_relative}"
        print(f"move {source.relative_to(ROOT)} -> {target.relative_to(ROOT)}")
        if write:
            target.parent.mkdir(parents=True, exist_ok=True)
            source.rename(target)
    return mapping


def update_marketing_paths(mapping: dict[str, str], write: bool) -> None:
    replacements = {
        "~/Documents/GitHub/My AI Skills/marketing/": "~/Documents/GitHub/My AI Skills/skills/Marketing/",
        "tree/main/marketing": "tree/main/skills/Marketing",
        **mapping,
    }
    for path in sorted((SKILLS / "Marketing").rglob("*.uam")):
        text = path.read_text(encoding="utf-8")
        updated = text
        for old, new in sorted(replacements.items(), key=lambda item: len(item[0]), reverse=True):
            updated = updated.replace(old, new)
        header, body = split_text(updated, path)
        metadata = fields(header)
        relative = path.relative_to(ROOT).as_posix()
        updated = updated.replace(
            f"sourcePath: {metadata.get('sourcePath', '')}", f"sourcePath: {relative}", 1
        )
        if updated != text:
            print(f"update paths in {path.relative_to(ROOT)}")
            if write:
                path.write_text(updated, encoding="utf-8")


def split_text(text: str, path: Path) -> tuple[str, str]:
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError(f"{path}: missing YAML frontmatter")
    header, body = text[4:].split("\n---\n", 1)
    return header, body.lstrip("\n").rstrip() + "\n"


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
        mapping = migrate_uam_files(True)
        update_marketing_paths(mapping, True)
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
