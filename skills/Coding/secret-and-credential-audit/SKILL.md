---
name: secret-and-credential-audit
description: Audit credentials, API keys, tokens, environment files, repository publication, release artifacts, and accidental secret exposure. Use automatically before commits or releases involving credentials, when publishing code, or when secret leakage is suspected. Exclude broader application threat modelling and non-secret personal-data review.
---

# Secret and credential audit

## Inputs and workflow

Use the repository/publication boundary, tracked and relevant untracked files, ignore rules, configs, fixtures, logs, archives, and generated artifacts. Inspect history only when authorised. Run locally with one agent by default, using existing scanners or local pattern checks; never print full secrets. Distinguish examples from live values and report path, line, type, exposure, and remediation.

## Verification, output, and safety

Verify removal and ignore coverage. Return `clean`, `findings`, or `blocked` with commands, redacted evidence, and the exact unavailable input when blocked. Read-only by default; never revoke, rotate, rewrite history, publish, or contact a provider without explicit authority. No internet or paid service is required.
