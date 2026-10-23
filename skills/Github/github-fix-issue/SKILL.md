---
name: github-fix-issue
description: Investigate and fix a referenced GitHub issue using the project's native version-control tools, isolated implementation work and shared commit/PR workflows. Use when asked to fix or implement a GitHub issue. Exclude issue creation without implementation and local bugs with no GitHub issue.
---

# GitHub Fix Issue

Fetch [the live-reference entry guide](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/using-references.md) and follow its shared context and
action policy. Use native repository tools for the detected VCS and GitHub tools for hosted records.

## Understand and isolate

Resolve the issue number/URL; ask only if it is missing. Read the report, relevant comments,
acceptance expectations and linked work. Keep reported behaviour, reproduction results and suspected
causes distinct. Inspect the relevant implementation and tests before settling on the cause.

Use [the worktree guide](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/worktrees.md). For a new Git task, prefer an isolated worktree and
branch; reuse the correctly bound task checkout and preserve existing edits when already in one.
Do not switch a shared working copy to a new branch by default or abandon uncommitted task work.

## Plan, fix and verify

Explain the proposed scope, approach and material edge cases. Resolve decisions that affect the
requested behaviour, then implement within the agreed scope using the project's existing patterns.
Use the repository's actual build/test guidance and checks appropriate to the change. Capture a
meaningful regression where practical; use a justified alternative when no automated test applies.
Report actual outcomes and gaps rather than requiring an invented test command.

Use [the shared writing guide](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/writing-guide.md) when recording proof and actual contributor
or review metadata. Editing the issue report itself is separate scope; if requested, use
[the issue workflow](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/issue-workflow.md).

## Commit and PR handoff

Use [the shared commit workflow](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/commits.md) for commit preparation and approval. Then fetch
and follow [Create PR](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/github-create-pr/SKILL.md) for PR drafting, issue-resolution links,
approval, publication and verification.

If approval is absent, leave a concrete local diff, evidence and prepared next step. Do not push,
comment on or close the issue merely because the local fix is complete.
