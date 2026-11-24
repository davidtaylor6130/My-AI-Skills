---
name: github-issue-sweep
description: Triage a scoped GitHub backlog or investigate untracked product problems, then prepare evidence-based, deduplicated issue proposals. Use for issue sweeps, backlog review and repository issue discovery. Exclude implementation and automatic tracker cleanup.
---

# GitHub Issue Sweep

Fetch [the live-reference entry guide](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/using-references.md), then follow its shared context
and action policy. Use [the shared issue workflow](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/issue-workflow.md) for evidence, duplicates,
repository-owned labels and any proposed tracker changes.

## Choose the useful scope

Use the user's requested area, journeys, reports or backlog query to define a bounded sweep.
Distinguish triaging existing reports from discovering untracked problems. If the request is broad,
state a useful first area and the coverage limit; ask only when a missing choice blocks useful work.
Do not start by collecting an arbitrary last N commits, every issue or a fixed list of code markers.

## Investigate and triage

For an existing backlog, read the selected reports and relevant comments/linked work, assess whether
they are actionable, try appropriate safe reproduction, and check whether current evidence supports
the stated impact. Query/paginate the relevant subset; do not treat a truncated list as the whole
tracker or lack of reproduction as proof that a report is false.

For untracked problems, follow the selected product behaviour through current code, tests, docs
and safe runtime checks. Investigate concrete failures, missing agreed behaviour and consequential
maintenance problems. Use history when it answers a specific question. Comments can be leads;
a marker or stylistic preference alone is not an issue. Do not change the working tree as part of
this sweep; hand an implementation request to [Fix Issue](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/github-fix-issue/SKILL.md) instead.

For each candidate, record the affected area, user impact, evidence source, reproduction status,
confidence and the next useful action. Separate confirmed defects, reported failures, feature
requests and unanswered questions. Search likely open/closed matches before proposing a new issue.
Recommend missing information, a related issue, a focused new report or a supported resolution;
do not automatically close stale reports, post comments, change labels or assign people.

## Present a reviewable result

Show a concise candidate list with evidence links, duplicate decisions and proposed next actions.
For new issues, prepare full bodies using [the issue format](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/issue-format.md). For edits or
comments, show the exact proposed changes. Apply the shared issue/publishing approval workflow to
only the items David selects. Return the real URLs, skipped items and coverage/reproduction limits.

This evidence-first triage approach draws on [GitHub CLI's triage guide](https://github.com/cli/cli/blob/trunk/docs/triage.md)
and [Python's triage guide](https://devguide.python.org/triage/triaging/index.html). Their project-specific
labels, bots, inactivity deadlines and automatic actions are not defaults for David's repositories.
