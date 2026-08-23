---
name: github-version-tag-release
description: Prepare a version tag, release notes, and GitHub Release. Use automatically when the user asks to version, tag, draft release notes, or publish a GitHub release. Exclude ordinary commits and non-GitHub release packaging; publication remains explicitly gated.
---

# GitHub Version Tag Release — Tag, Release Notes & GitHub Release

Follow `../references/action-policy.md`; automatic pickup never authorises tag, push, or release creation.

You are helping the user create a clean, well-documented release for their GitHub repository.

Before any commit, push, tag, or release, show all proposed commands/text for user review. Do not execute irreversible actions without explicit confirmation.

---

## Step 0 — Gather context

Run in parallel:
- `git tag -l` — existing tags
- `git status --short` and `git log --oneline -5` — confirm the tree is clean and see where HEAD is
- `git remote get-url origin` — confirm the release destination
- Read `AGENTS.md`, `CLAUDE.md`, `CHANGELOG.md`, or any notes file if present — extract known issues

Then, once you know the most recent tag, get the full set of commits the release will cover:
- `git log <last-tag>..HEAD --oneline` (or `git log --oneline` for a first release)

If the tree is dirty, tell the user — uncommitted work won't be in the release. Do not require `gh`
while inspecting commits, tags, versions, or README content.

---

## Step 1 — Determine version number

Suggest the next logical version number based on existing tags:
- No tags yet → suggest `v0.1.0`
- Existing tags → suggest the next logical increment (semver, date-based, or custom scheme)

Use `question` tool with version options to confirm — do not ask an open-ended question.

### Version inventory gate

Before choosing the target commit, scan every tracked file for product version declarations and the exact previous version:

```bash
git grep -nE 'project\([^)]*VERSION|kAppVersion|CFBundle(Short)?Version|MARKETING_VERSION|CURRENT_PROJECT_VERSION|"version"[[:space:]]*:|(^|[[:space:]])version[[:space:]]*=|latest stable.*v[0-9]+\.[0-9]+\.[0-9]+'
git grep -nE '(V|v)?<previous-version-with-escaped-dots>'
```

Review every match. Update all product-owned version sources, including build metadata, application constants, package manifests and root lockfile entries, UI displays and tests, installer metadata, and current-version documentation. Do not alter dependency versions or intentionally historical release/changelog references.

Run both searches again after editing. List and justify every remaining old-version match. Build or test enough to verify the packaged application and visible UI report the new version. Commit and merge the version bump before confirming the release target. Do not tag or publish while a stale product-version match remains.

---

## Step 2 — Confirm target commit

Default to the latest commit on the current branch. Use `question` tool to confirm target commit — show hash and message, offer option to pick a different commit.

Check the commit has been pushed (`git branch -r --contains <commit>`). If it only exists locally, confirm with the user before pushing the branch — a GitHub release pointing at an unpushed commit is the most common way this flow fails.

---

## Step 3 — Audit README

Read README.md. Check for stale version numbers, outdated feature lists, broken badges, or missing changes since last release. Use `question` tool to propose README updates. If changes needed, apply and commit before proceeding.

## Step 4 — Write release notes

This is the first step that needs GitHub-hosted data. Run `gh auth status`, then
`gh issue list --state open --limit 100 --json number,title,labels`. If authentication fails, finish
drafting from local evidence and mark the GitHub issue inventory as blocked.

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

- Use git for status, history, version changes, commits, tags, and pushes. Use `gh` only to read
  GitHub-hosted issues and create the GitHub Release.
- Use `question` tool to confirm version number and target commit before tagging
- Use `question` tool before any push — user must approve what will be tagged
- Respect the user's preference for Co-Authored-By trailers — ask whether to include or omit them
- Never tag a release before its version inventory update is committed and merged
