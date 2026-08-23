---
name: decision-trail
description: Maintain an append-only, reviewable decision and evidence log for long-running, autonomous, multi-phase, transferred, or high-risk work. Use automatically when a human will review after the fact, a goal spans many iterations, or work may transfer between agents. Skip routine short tasks.
---

# Decision trail

## Inputs

The goal, current phase, reviewer needs, evidence locations, and local output path.

## Workflow

Use CSV or TSV with `timestamp`, `phase`, `decision`, `reason`, `evidence`, and `result`. Append one meaningful decision or checkpoint per row. Evidence must resolve to a path, command output, commit, test, screenshot, trace, or artifact. Do not log trivial actions. Keep the trail local by default and commit it only when it is part of the deliverable. Single-writer operation is the baseline; separate files before concurrent writing.

## Verification and output

Check that rows parse, remain append-only, and point to available evidence. Report the trail path and final checkpoint. Automatic selection does not authorise commits, publication, external messages, or destructive operations.
