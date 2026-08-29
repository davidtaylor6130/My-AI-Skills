---
name: resume-work
description: Reconstruct and continue interrupted work from checkpoints, transcripts, branches, worktrees, goal state, and verification evidence without repeating completed investigation. Use automatically when resuming, taking over, transferring between worker nodes, recovering after restart or context compaction, or asking where a task was left. Skip fresh tasks with no prior work.
---

# Resume work

## Checkpoint contract

Record goal ID; task/thread ID; worker node; model/runtime when known; repository; workspace/worktree; branch; HEAD; dirty files; phase; original done predicate; completed work; verified claims and evidence; failed approaches; open decisions; active processes/sessions; locks/ownership; next exact action.

Store checkpoints at `.UAM/AINotes/resume-<task>.md`, creating `.UAM/AINotes/` on first write. Reuse the existing task checkpoint instead of creating dated duplicates; honour a user-specified or inherited checkpoint path.

## Workflow

Read the prior trail, verify live repository/process state, separate done from pending, and test inherited completion claims against artifacts. Do not repeat investigation merely for reassurance. Route only remaining work to the narrowest skill and update the checkpoint on pause or transfer. A single agent is sufficient unless remaining work is independently divisible.

## Verification and output

Report reconstructed state, mismatches, remaining predicate, next action, and evidence. Never create an untested `wip:` commit; commit only a coherent verified unit when policy permits. Return `BLOCKED` with the missing checkpoint, workspace, or authority.
