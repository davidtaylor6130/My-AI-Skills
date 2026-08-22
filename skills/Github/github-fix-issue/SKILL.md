---
name: github-fix-issue
description: End-to-end GitHub issue fix workflow using git for repository work and gh only for GitHub issues and pull requests. Ask → Branch → Investigate → Plan → Approve → Fix → Test → Confirm Commit → Confirm PR.
---

# GitHub Fix Issue

Workflow: ask → branch → investigate → plan → approve → fix → test → confirm commit → confirm PR.

---

## Step 0 — Ask for issue

If user did NOT provide issue number/URL, ask: "Which issue(s) to fix? Number, URL, or list."

## Step 1 — Branch

```bash
git switch -c fix/issue-<number>-<slug>
```

Use git for all branch, status, diff, staging, commit, fetch, and push operations. Do not use
`gh issue develop`; creating a local branch does not require GitHub's API.

## Step 2 — Investigate

Read issue body + comments:
```bash
gh issue view <number> --json title,body,comments,labels
```

This is the first step that requires an authenticated `gh` session. If it is unavailable, ask the
user to authenticate before reading the GitHub-hosted issue; do not block local git checks.

Search codebase for relevant code. Look at related tests. Understand the root cause.

## Step 3 — Plan

Present structured plan: what files change, approach, edge cases. Use `question` tool with approval options:
- "Approve — proceed with fix"
- "Adjust plan — describe changes"
- "Cancel"

Wait for user response before proceeding.

## Step 4 — Fix

Implement changes per approved plan. Keep minimal. Reuse existing patterns.

## Step 5 — Test

Find project test command (package.json, CMakeLists, etc.) and run it. If none found, ask user. If tests fail, fix and retry. Report results.

## Step 6 — Confirm Commit

Inspect `git status` and stage only the confirmed files with `git add -- <paths>`. Show the staged diff
summary. Present the proposed commit title and description in Conventional Commits format. Commit only
after the user confirms.

## Step 7 — Confirm PR

Draft the PR title and body, including `Closes #<number>`, then show both to the user. Ask approval:
- "Approve — push branch and create PR"
- "Edit title/body"
- "Cancel"

Only after approval:

```bash
git push -u origin <branch>
gh pr create --title "<title>" --body-file <temp-file>
```

Write the body to a temporary file with real newlines. Return the URL printed by `gh pr create`; do not
make another `gh` call merely to open a browser. The user reviews and merges the PR themselves.

## Ground rules

- Use git for every repository operation. Use `gh` only to read the GitHub issue and create the PR.
- No commit, push, or PR creation until the user approves the relevant files and wording.
- Requires authenticated `gh` only when the workflow reaches a GitHub-hosted operation.
- If not a GitHub repo, stop
