---
name: edge-case-sweep
description: Run a deliberate edge-case review. Use when the user asks for a sweep, systematic analysis, or hardening report. Skip ordinary implementation; use edge-case-guard.
---

# Edge case sweep

Find high-value cases hidden by the happy path. Review or report by default; modify code only when requested.

## Establish the flow

Read the intended behaviour and relevant code. Trace `caller/input → shared boundary/state → persistence/dependency → consumer/output`, including sibling callers, existing constraints, error handling, and nearby tests. Label assumptions when the feature does not exist yet.

## Sweep

Apply only relevant lenses:

- input: missing, empty, wrong type, zero, negative, boundary ±1, Unicode, duplicates, ordering, and scale;
- identity: authentication, permission, ownership, tenancy, expiry, deletion, and stale identity;
- lifecycle: first use, repeat, completed state, unexpected order, refresh, restart, cancel, and resume;
- recovery: partial write, timeout, retry, duplicate submission, idempotence, rollback, and cleanup;
- concurrency and time: races, reordered events, clock drift, time zones, and date boundaries;
- dependencies: unavailable, slow, malformed, quota-limited, offline, read-only, or version-incompatible;
- data and compatibility: existing records, migrations, serialization, corrupt data, and older clients;
- user surface: loading, empty, error, long content, accessibility, and unsaved work.

Reject cases that are implausible, harmless, already prevented by verified constraints, or would not change a decision, implementation, or test. Prefer one shared invariant over guards in every caller.

## Output

Prioritise `Cover`, `Decision`, and `Accept` cases. For each retained case give the scenario, impact, evidence or assumption, expected behaviour, shared control point, and smallest useful verification. Lead with data loss, security, corruption, crashes, and unrecoverable user work.

Return the sweep in chat unless a file is useful or requested. Store any sweep document in `.UAM/AINotes/`, creating the directory on first write and reusing an existing relevant note. Do not claim the sweep is exhaustive.
