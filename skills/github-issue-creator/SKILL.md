---
name: github-issue-creator
description: Create one or more GitHub issues from a description. Checks for existing duplicates first — if an issue with the same title/description already exists, reports back. If none found, creates the issue with `gh`. Use when user says "create issue", "file an issue", "make a github issue", "/create-issue", or describes a bug/feature they want tracked.
---

# GitHub Issue Creator

Workflow: parse description → check duplicates → report existing or create.

> [!CRITICAL]
> **Never pass a multi-line body with `\n` inside a bash double-quoted string.**
> In bash, `"...\n..."` keeps `\n` as the literal two characters `\` + `n`. `gh` then stores the literal text `Problem\n\n...` and GitHub renders it as one unbroken line of escaped text — headings (`##`) and bullet lists never appear. This is the #1 way issue bodies get silently mangled.
>
> **Always write the body to a temp file with real newlines, then use `--body-file`:**
> ```bash
> # write the body (real newlines) to a file, e.g. via the Write tool or printf
> gh issue create --title "<title>" --body-file /tmp/issue_body.md --label "<label1,label2>"
> ```
> Same rule applies to `gh issue edit --body-file <file>` and `gh pr create --body-file <file>`.
> Note: `gh issue edit` has **no** `--label` flag — use `--add-label <name>` (and create missing labels first with `gh label create`).

## Labels are MANDATORY

Every created issue MUST have at least one label. Do not skip this.

1. Before creating, check which labels already exist: `gh label list --json name`.
2. Pick labels that fit (e.g. `bug`, `enhancement`, `ui`, `provider`, `reliability`, `tool-call`, `accessibility`, `goal-loop`, `acp-runtime`, `refactor`, `documentation`).
3. If a fitting label does not exist, create it first: `gh label create "<name>"` (optionally `--description "..." --color "..."`).
4. Pass labels at creation: `gh issue create --title "..." --body-file /tmp/issue_body.md --label "bug,ui"`.
5. If you forgot at creation, retro-fit with `gh issue edit <number> --add-label "bug,ui"`.

An issue with no labels is incomplete — always confirm labels are present before reporting success.

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

**No duplicates:** Create each issue. Write the body (with real newlines) to a temp file first, then pass it with `--body-file` — do NOT inline `\n` in a double-quoted string:

```bash
gh issue create --title "<title>" --body-file /tmp/issue_body.md --label "<label1,label2>"
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
