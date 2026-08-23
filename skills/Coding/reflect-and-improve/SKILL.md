---
name: reflect-and-improve
description: Extract durable lessons from completed or difficult work and propose targeted updates to skills, Agent.md, tests, lint rules, scripts, or tooling. Use automatically after a complex task, repeated failure, significant user correction, a new reusable workflow, or the same instruction being needed more than once. Skip trivial one-off work.
---

# Reflect and improve

## Inputs and workflow

Inspect the transcript, goal state, worker/reviewer messages, user corrections, rejected approaches, failed calls, verification evidence, repeated instructions, and overlapping skills. Classify each lesson as an existing-skill edit, new skill, `Agent.md` edit, test/eval, lint/type/runtime/script enforcement, UAM backlog item, note, or discardable one-off. Prefer structural enforcement over more prose.

Present a concise proposed-change set before editing organisation-wide skills unless the surrounding goal already authorises those edits. One strong reviewer is enough; use another independent review only for consequential or disputed changes. Work without subagents when unavailable or wasteful.

## Verification and output

Report evidence, classification, proposed enforcement, files affected, and checks. Never turn reflection into permission for commits, external messages, or production changes. Return `BLOCKED` only when required history or authority is unavailable.
