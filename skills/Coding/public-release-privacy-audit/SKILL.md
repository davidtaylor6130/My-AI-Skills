---
name: public-release-privacy-audit
description: Audit personal and organisational information before open-sourcing, publishing a repository, making a public release, sharing archives, uploading logs or screenshots, or publishing generated content. Use automatically for public distribution checks. Exclude pure credential-only scans and internal application security design.
---

# Public release privacy audit

## Inputs and workflow

Inspect the exact local publication set for personal paths, emails, usernames, internal hostnames/domains, customer names, private repository links, secrets, and sensitive logs, screenshots, fixtures, metadata, or generated content. Check archives by listing before extraction where possible. One local agent is the baseline; split only genuinely independent large artifacts.

## Verification, output, and safety

Report redacted evidence and the public artifact affected. Verify the sanitized artifact, not only its source files. Return `clean`, `findings`, or `blocked` with the unavailable artifact or tool. Read-only unless edits are requested; never publish, upload, or rewrite history automatically. No internet or paid service is required.
