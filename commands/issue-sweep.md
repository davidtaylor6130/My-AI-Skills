# Issue Sweep — Audit Code and File GitHub Issues

You are helping the user identify problems, gaps, and improvements in their codebase and turn them into well-written GitHub Issues.

---

## Step 0 — Gather context

Run in parallel:
- `git log --oneline -20`
- `gh issue list --state all --limit 200 --json number,title,state` — avoid duplicating open issues or re-filing ones already closed
- Read `AGENTS.md`, `CLAUDE.md`, or any known-issues docs (check your agent's conventions)

---

## Step 1 — Scan for inline flags

Search the codebase for markers that indicate known problems or deferred work. Use your built-in search tool (Grep) with a word-bounded pattern so `BUG` doesn't match `DEBUG` and `XXX` doesn't match hex strings:

```
\b(TODO|FIXME|HACK|XXX|WORKAROUND|KLUDGE)\b
```

Restrict to source files for the project's language(s) and skip build output, vendored dependencies, and lockfiles. List every genuine hit with file and line number; discard false positives (variable names, third-party code, strings that merely contain a marker word).

---

## Step 2 — Review recent commits for hints

Look at commit messages for phrases like "fix later", "temporary", "broken", "skip", "disable", "workaround" — these often indicate debt that didn't get an issue:

```
git log -50 -i --grep="fix later" --grep="temporar" --grep="workaround" --grep="broken" --grep="disable" --oneline
```

---

## Step 3 — Categorise findings

Group everything found into:
- **Bugs** — incorrect behaviour, crashes, data loss risk
- **Enhancements** — missing features, incomplete implementations
- **Refactors** — code quality issues that affect maintainability
- **Documentation** — missing or wrong docs, stale comments
- **Questions / decisions** — unresolved design choices

---

## Step 4 — Confirm before filing

Show the user the full list grouped by category. Ask:
- Which ones to file as issues (default: all bugs, then user decides on the rest)
- Any to skip or merge together

---

## Step 5 — File the issues

First run `gh label list` — `gh issue create` fails if you pass a label that doesn't exist in the repo. Only use labels that exist (or create missing standard ones with `gh label create` after asking).

For each confirmed issue, create a GitHub issue with:
- Clear title: describes the problem, not the fix
- Body: what the problem is, where in the code (file:line if known), what the expected vs actual behaviour is, any relevant context
- Label: `bug`, `enhancement`, `question`, or `documentation`

Use `gh issue create --title "..." --body-file <temp>` with a body written to a temp file to avoid shell quoting problems. Show each URL as it's created.

---

## Ground rules

- Never file duplicate issues — check existing issues first
- One issue per distinct problem — do not bundle unrelated things
- Do not exaggerate severity — label bugs as bugs, enhancements as enhancements
- Show the user the list before filing anything
