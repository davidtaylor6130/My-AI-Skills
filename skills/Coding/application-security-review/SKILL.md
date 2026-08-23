---
name: application-security-review
description: Review authentication, authorisation, input validation, file handling, network boundaries, permissions, cryptography, webhooks, remote execution, deserialisation, public APIs, data exposure, and security-sensitive architecture. Use automatically when code or design crosses a security boundary. Exclude repository secret scanning and public-release privacy cleanup unless those risks are also explicit.
---

# Application security review

Map assets, trust boundaries, actors, inputs, privileged actions, and failure modes. Trace callers and effects, validate highest-risk assumptions with executable evidence when practical, and rank findings by exploitability and impact. Prefer platform security primitives and boundary validation. Do not exploit production, access unrelated data, rotate credentials, or apply consequential changes without authority. Report intended behaviour, evidence, findings, fixes, verification, and stopped evidence. Return `clean`, `findings`, or `blocked`.
