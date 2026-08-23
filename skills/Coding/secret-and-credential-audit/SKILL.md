---
name: secret-and-credential-audit
description: Audit credentials, API keys, tokens, environment files, repository publication, release artifacts, and accidental secret exposure. Use automatically before commits or releases involving credentials, when publishing code, or when secret leakage is suspected. Exclude broader application threat modelling and non-secret personal-data review.
---

# Secret and credential audit

Inspect tracked and relevant untracked release content, history when authorised, ignore rules, configs, fixtures, logs, archives, and generated artifacts. Use existing scanners or local pattern checks; never print full secrets. Distinguish examples from live values and report path, line, type, exposure, and remediation. Verify removal and ignore coverage. Read-only by default; never revoke, rotate, rewrite history, publish, or contact a provider without explicit authority. Return `clean`, `findings`, or `blocked` with commands and redacted evidence.
