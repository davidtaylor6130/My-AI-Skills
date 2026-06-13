# Repo Release — Tag, Release Notes & GitHub Release

You are helping the user create a clean, well-documented release for their GitHub repository.

---

## Step 0 — Gather context

Run in parallel:
- `git tag -l` — existing tags
- `git status --short` and `git log --oneline -5` — confirm the tree is clean and see where HEAD is
- `git remote get-url origin` — confirm remote
- `gh issue list --state open --limit 100 --json number,title,labels` — open issues to include in release notes
- Read `AGENTS.md`, `CHANGELOG.md`, or any notes file if present — extract known issues

Then, once you know the most recent tag, get the full set of commits the release will cover:
- `git log <last-tag>..HEAD --oneline` (or `git log --oneline` for a first release)

If the tree is dirty, tell the user — uncommitted work won't be in the release.

---

## Step 1 — Determine version number

Ask the user what version to tag, or suggest one based on existing tags:
- No tags yet → suggest `v0.1.0`
- Existing tags → suggest the next logical increment
- Ask if the versioning scheme is semver, date-based, or a custom scheme (e.g. pre-live attempt numbers)

Confirm before proceeding.

---

## Step 2 — Confirm target commit

Default to the latest commit on the current branch. Ask the user if they want to tag a different commit. Show the commit hash and message for confirmation.

Check the commit has been pushed (`git branch -r --contains <commit>`). If it only exists locally, confirm with the user before pushing the branch — a GitHub release pointing at an unpushed commit is the most common way this flow fails.

---

## Step 3 — Write release notes

Release notes must include:

1. **What the project is** — one sentence for anyone landing here cold
2. **Version numbering note** — if the scheme is non-standard, explain it briefly
3. **What's in this release** — summarise the meaningful commits since the last tag (or all commits if first release); group by: new features, fixes, removed/cleaned up
4. **Known issues** — pulled from open GitHub Issues; link each by number; be honest
5. **Platform / environment** — OS, hardware, key dependencies if relevant

Do not pad. Short and accurate beats long and vague.

---

## Step 4 — Create tag and GitHub release

1. `git tag -a <version> <commit> -m "<version> — <short title>"` — annotated, so the tag records who/when
2. `git push origin <version>`
3. `gh release create <version> --verify-tag --title "<version> — <short title>" --notes-file <temp file>`

Write the notes to a temp file rather than inline `--notes` to avoid shell quoting problems. If the user wants to review the release on GitHub before it goes public, add `--draft`.

Show the release URL when done.

---

## Ground rules

- Confirm the version number and target commit with the user before tagging
- Never push without the user seeing what will be tagged
- Do not add Co-Authored-By trailers to any commits
