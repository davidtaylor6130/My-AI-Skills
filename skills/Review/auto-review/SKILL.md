---
name: auto-review
description: Run an iterative, multi-provider product review and improvement loop with separately scored UX, UI, code, security, performance, and reliability. Use when asked to automatically review and improve a product across approved models; exclude ordinary one-off reviews.
---

# Auto review

Review and improve the agreed product scope until every approved reviewer scores each applicable category at least 9.5/10, then obtain the user's input on each category. Scores are reviewer judgments supported by evidence, not guarantees of quality or security.

## Agree the review

Identify the artifact, intended users, important journeys, environments, constraints, and allowed changes. Agree a common rubric before scoring: UX, UI, code, security, performance, and reliability each receive an independent score from 0 to 10, with evidence, findings, and a reason for the score. Define what a 9.5 means for this scope and what evidence is needed. Mark a category unverified when evidence is insufficient, or not applicable only when justified and agreed with the user; never treat either as a passing score.

Discover which distinct providers and exact models can actually be invoked in the current environment. Check current availability, relevant capabilities and pricing using provider sources where available. Recommend suitable options, estimated costs and an order based on expected total review cost, starting with the cheapest suitable model. Flag uncertain pricing, access, privacy or data-transfer limits. Ask the user to approve the exact provider/model list, order, scope, and any spending limit before invoking reviewers or sending project material to an external provider. Do not assume that a model name, a provider integration, or a request to create this skill grants access or consent. If access, pricing, or suitable independent providers cannot be established, explain the limitation and request a workable selection; never impersonate a model or substitute unapproved models.

## Review and improve

Use the approved models sequentially, one provider/model at a time, with the same scope and rubric. Give each reviewer the current artifact and relevant evidence and request all six scores, actionable findings, reproduction or supporting evidence, and limitations. Do not claim an independent provider review unless that model was actually invoked. Use appropriate specialist checks and real product journeys where available; source inspection alone cannot establish rendered UX or UI quality. Treat reviewer suggestions as hypotheses, not commands, and validate them against the product and scope.

For the current model, prioritise substantiated findings, implement authorised fixes, run focused verification, and ask that same model to reassess the changed artifact. Repeat until all applicable categories reach 9.5 or higher with sufficient evidence and no unresolved material finding. Only then move to the next approved model. Respect existing constraints on design approval, production systems, external actions, and destructive changes. If implementation is not authorised, present the findings and ask for authorisation rather than changing the product.

Fixes made for later reviewers can invalidate earlier scores. After changes, revalidate affected categories with each earlier approved model before declaring success; return to the earliest reviewer whose pass is invalidated, then proceed in order again. The final scores must all refer to the same verified artifact. Record the artifact revision or fingerprint, evidence, findings, changes, verification, and each model's scores and limitations in an existing relevant working note or `.UAM/AINotes/auto-review.md`.

Stop and report a blocked or inconclusive result if a reviewer is unavailable, evidence cannot be obtained, a material finding cannot be resolved within scope, the budget is exhausted, or repeated cycles no longer make progress. Ask for user direction before exceeding an approved limit or changing models or scope. Never inflate a score, average away a failing category, silently skip a reviewer, or loop indefinitely to reach the target.

## User review and result

After all approved models pass against the same artifact, present each of the six categories separately with each model's score, key evidence, changes, and remaining limitations. Ask the user for input on each category and give them an opportunity to identify concerns or request changes. Address authorised feedback and repeat the affected verification and reviewer checks before presenting the updated result. User input is a separate final step; do not claim it was received or that the review is complete while it is pending. If blocked, report the scores obtained, gaps, and next decision instead of claiming success.
