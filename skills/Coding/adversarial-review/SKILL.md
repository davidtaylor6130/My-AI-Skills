---
name: adversarial-review
description: Challenge a proposed design or code change with independent review perspectives and a lead verdict. Use automatically for contested or high-risk architecture, concurrency, persistence, security boundaries, public APIs, large refactors, release candidates, or uncertain initial reviews. Do not invoke for routine low-risk diffs.
---

# Adversarial review

## Inputs and workflow

State intended behaviour, scope, artifact, and rubric. Give each available reviewer the same material; one reviewer is enough for ordinary work, while risk, disagreement, or uncertainty may justify a second genuinely distinct reviewer. A single-agent critical pass is the fallback. Deduplicate findings, record agreement and disagreement, and classify each as `Act on`, `Consider`, `Noted`, or `Dismissed` using lead judgment.

## Verification and output

Return the verdict, evidence, classifications, and unresolved risks. Never auto-apply suggestions; verify every accepted change separately. Review selection grants no authority to publish or mutate external systems.
