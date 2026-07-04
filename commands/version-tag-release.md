---
name: version-tag-release
description: Tag a repository, write release notes & create a GitHub Release. Use when the user wants to tag a version, write release notes, or publish a GitHub release. Requires gh CLI with appropriate permissions and a connected remote.
---

# Version Tag Release — Tag, Release Notes & GitHub Release

You are helping the user create a clean, well-documented release for their GitHub repository.

Before any commit, push, tag, or release, show all proposed commands/text for user review. Do not execute irreversible actions without explicit confirmation.

---

## Step 0 — Gather context

Run in parallel:
- `gh auth status --show-token` — verify gh CLI is authenticated; if invalid/expired, stop and ask the user to run `gh auth login` before proceeding
- `git tag -l` — existing tags
- `git status --short` and `git log --oneline -5` — confirm the tree is clean and see where HEAD is
- `git remote get-url origin` — confirm remote; if no remote exists, note this and skip all gh steps below — output manual commands where applicable
- `gh issue list --state open --limit 100 --json number,title,labels` — open issues to include in release notes (skip if no remote)
- Read `AGENTS.md`, `CLAUDE.md`, `CHANGELOG.md`, or any notes file if present — extract known issues

Then, once you know the most recent tag, get the full set of commits the release will cover:
- `git log <last-tag>..HEAD --oneline` (or `git log --oneline` for a first release)

If the tree is dirty, tell the user — uncommitted work won't be in the release. If gh fails at any point before Step 4, output the exact command for the user to run manually rather than proceeding without it.

---

## Step 1 — Determine version number

Suggest the next logical version number based on existing tags:
- No tags yet → suggest `v0.1.0`
- Existing tags → suggest the next logical increment (semver, date-based, or custom scheme)

Use `question` tool with version options to confirm — do not ask an open-ended question.

---

## Step 2 — Confirm target commit

Default to the latest commit on the current branch. Use `question` tool to confirm target commit — show hash and message, offer option to pick a different commit.

Check the commit has been pushed (`git branch -r --contains <commit>`). If it only exists locally, confirm with the user before pushing the branch — a GitHub release pointing at an unpushed commit is the most common way this flow fails.

---

## Step 3 — Audit README

Read README.md. Check for stale version numbers, outdated feature lists, broken badges, or missing changes since last release. Use `question` tool to propose README updates. If changes needed, apply and commit before proceeding.

## Step 4 — Write release notes

Release notes must include:

1. **What the project is** — one sentence for anyone landing here cold
2. **Version numbering note** — if the scheme is non-standard, explain it briefly
3. **What's in this release** — summarise the meaningful commits since the last tag (or all commits if first release); group by: new features, fixes, removed/cleaned up
4. **Known issues** — pulled from open GitHub Issues; link each by number; be honest
5. **Platform / environment** — OS, hardware, key dependencies if relevant

Do not pad. Short and accurate beats long and vague.

If a `CHANGELOG.md` exists, append an entry for this release using the project's existing format. Show it to the user for review.

---

## Step 5 — Create tag and GitHub release

Show user the release notes. Use `question` tool to approve or edit. Ask whether to include or omit `Co-Authored-By` trailers.

Use `question` tool to confirm tag, push, and release before running any of these:

1. `git tag -a <version> <commit> -m "<version> — <short title>"` — annotated, so the tag records who/when
2. `git push origin <version>`
3. Default to publishing immediately: `gh release create <version> --verify-tag --title "<version> — <short title>" --notes-file <temp file>`

Write the notes to a temp file rather than inline `--notes` to avoid shell quoting problems. Only use `--draft` if the user explicitly requests a pre-review on GitHub first.

Show the release URL when done. If any command fails, show the exact output and suggest the next step: re-auth (`gh auth login`), retry after a delay, or fall back to creating the release manually on GitHub.

---

## Ground rules

- Use `question` tool to confirm version number and target commit before tagging
- Use `question` tool before any push — user must approve what will be tagged
- Respect the user's preference for Co-Authored-By trailers — ask whether to include or omit them
