---
name: github-issue-creator
description: Create one or more GitHub issues from a description. Checks for existing duplicates first — if an issue with the same title/description already exists, reports back. If none found, creates the issue with `gh`. Use when user says "create issue", "file an issue", "make a github issue", "/create-issue", or describes a bug/feature they want tracked.
---

# GitHub Issue Creator

Workflow: parse description → check duplicates → report existing or create.

---

## Step 1 — Parse user description

User describes issue(s). Could be:
- Single bug report ("The login button doesn't work on mobile")
- Single feature request ("Add dark mode")
- Multiple items ("Two bugs: 1. login broken, 2. profile pic won't upload")

Parse into structured items. Each item needs:
- **Title** — short summary (<80 chars)
- **Body** — detailed description, steps to reproduce, expected vs actual behavior
- **Labels** — optional, ask user if unclear

If user provides a list, treat each item as a separate issue.

Use `question` tool to confirm parsed issues before proceeding:
- "Confirm — create these N issues"
- "Edit titles — I'll clarify"
- "Cancel"

## Step 2 — Check for duplicates

For each parsed issue, check if a matching issue already exists:

```bash
gh issue list --search "<title keywords>" --json title,number,state,labels --limit 10
```

```bash
gh issue list --state all --search "<title keywords>" --json title,number,state,labels --limit 10
```

Matching criteria (use judgment):
- **Exact title match** → definite duplicate
- **Strong semantic match** (same bug/feature described differently) → probable duplicate
- **Partial keyword overlap** on unique terms → possible duplicate

## Step 3 — Report or create

**Duplicates found:** Show user a table:

| # | User's Item | Matched Issue | State |
|---|-------------|---------------|-------|
| 1 | Login broken | #42 Mobile login fails | open |
| 2 | Dark mode | — | new |

Use `question` tool:
- "Create only the new items (#2)"
- "Reopen #42 instead of creating #1"
- "Create all anyway (existing issues differ from what I want)"
- "Add my description as a comment to #42 instead"
- "Cancel"

**No duplicates:** Create each issue:

```bash
gh issue create --title "<title>" --body "<body>" --label "<label1,label2>"
```

If multiple issues, create them one at a time.

## Step 4 — Confirm

Show user the result:
- "Created: #N — Title (https://github.com/owner/repo/issues/N)"
- "Skipped: Title — duplicate of #N (https://github.com/owner/repo/issues/N)"

Open in browser for created issues:

```bash
gh issue view <number> --web
```

## Ground rules

- Requires `gh` CLI authenticated. Only for GitHub-hosted repos.
- If no `gh`, stop and tell user. If not a GitHub repo, stop.
- Duplicate detection is heuristic — always present results for user to confirm.
