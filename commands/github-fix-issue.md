---
name: github-fix-issue
description: End-to-end GitHub issue fix workflow. Ask → Branch → Investigate → Plan → Approve → Fix → Test → Confirm Commit → Confirm PR → Browser.
---

# GitHub Fix Issue

Workflow: ask → branch → investigate → plan → approve → fix → test → confirm commit → confirm PR → browser.

---

## Step 0 — Ask for issue

If user did NOT provide issue number/URL, ask: "Which issue(s) to fix? Number, URL, or list."

## Step 1 — Branch

```bash
gh issue develop <number> --branch-name <slug>
```
If that fails:
```bash
git checkout -b fix/issue-<number>
```

Branch name: `fix/issue-<number>-<slug>` or `gh` default.

## Step 2 — Investigate

Read issue body + comments:
```bash
gh issue view <number> --json title,body,comments,labels
```

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

Stage changes (`git add -A`). Show user the diff summary. Present proposed commit title + description (Conventional Commits format). Ask user to approve or edit wording. Only commit after user confirms.

## Step 7 — Confirm PR

```bash
gh pr create --fill --issue <number>
```

Show user the PR title + body. Ask approval:
- "Approve — open PR in browser"
- "Edit title/body"
- "Cancel"

Only push / create PR after user confirms wording.

## Step 8 — Open Browser

```bash
gh pr view --web
```

User reviews final PR in browser and merges themselves.

## Ground rules

- No GitHub writes (commit, push, PR) until user approves exact wording at each gate
- Requires `gh` CLI authenticated and `git` configured
- If no `gh` CLI, stop and tell user to install it
- If not a GitHub repo, stop
