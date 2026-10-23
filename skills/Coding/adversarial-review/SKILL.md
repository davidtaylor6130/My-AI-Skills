---
name: adversarial-review
description: Coordinate independent completion reviews after code, configuration, documentation, or agent/skill changes, and formal design or product assessments. The parent dispatches fresh read-only reviewers and adjudicates their findings. Review workers use specialist methods without invoking this coordinator.
---

# Independent review gate

The parent delivering the work owns this gate. Its own checks are preparation, not an independent review. Run the gate after relevant local verification and before claiming a completed change, including documentation and instruction changes. Discussion and investigation without changes do not require a completion gate.

A delegated implementer returns its candidate and verification evidence to the parent with review pending. A review worker performs its assigned pass and returns findings; it never invokes this coordinator, spawns reviewers, or starts another completion gate. For a standalone formal assessment, the requesting thread coordinates the same independent process.

## Select reviewers

Use the highest applicable default, based on affected contracts, uncertainty, and consequences rather than line count:

- **Two reviewers minimum:** small, bounded changes, including documentation and copy.
- **Three reviewers:** substantial behavioural changes, shared contracts, several subsystems, or material agent/skill policy changes.
- **Four reviewers:** security boundaries, data migrations or integrity, concurrency, broad architectural changes, or release-critical behaviour.

Discover the live provider/model catalog and permitted delegation capabilities. Prefer distinct underlying models of comparable capability, including suitable configured local models. Different harnesses using the same model do not provide model diversity. Do not substitute a less capable model merely to increase the model count. Record the intended count, selected models, and rationale; prioritise defect detection over token savings within the user's explicit limits.

If only one suitable model is available, use the required number of separate fresh reviewer chats and disclose reduced model diversity. Quota, access, tool, or startup failures are missing reviews, not successful passes. Respect provider and usage restrictions; if the required independent coverage cannot be obtained, return `INCOMPLETE` rather than reviewing the work yourself or silently reducing the count.

## Freeze the review target

Establish the requested outcome, relevant requirements and constraints, review boundary, baseline, exact candidate version, relevant tests, and permitted execution surface. Include scoped uncommitted and untracked changes. Identify the candidate through an immutable snapshot or a recorded commit plus content hashes/diff that cover those changes.

A fresh worktree based only on a commit does not contain uncommitted edits. Supply the actual candidate before using such isolation, or use a read-only shared checkout and keep the review target unchanged while reviewers run. Give runtime reviewers separate disposable profiles or data; serialize interactions when safe isolation is unavailable without sharing earlier reviewer conclusions.

## Dispatch independent workers

Launch the required `review` workers through UAM's orchestrator or the available equivalent with fresh chat histories and no inherited implementation conversation. Use delegation that can preserve that independence and the worker's read-only role. A new title or role prompt in the implementation chat is insufficient.

Give every worker the same core brief:

- intended behaviour, user requirements, constraints, and scope;
- baseline and candidate identity, actual artifacts, and relevant surrounding contracts;
- verification commands and observed results, with known evidence gaps stated neutrally;
- permitted tools and test surface, the specialist review methods to apply, and the expected evidence-backed findings.

Do not supply the implementer's verdict, desired approval, proposed findings, or other reviewers' first-pass results. Neutral additional lenses may supplement the common rubric; every reviewer still checks the core requirements. Reviewers must inspect the artifacts rather than merely judge a summary.

Use `review-site`, `review-desktop-app`, `review-mobile-app`, `application-security-review`, or other relevant methods for the affected scope; a small diff does not imply a whole-product audit. Run workers in parallel where their tools and test state are isolated. Retain task IDs and actual provider/model identities, collect every required result, and verify that the target remained unchanged. Retry only actionable failures within the user's limits, reusing idempotency keys where supported and never duplicating an accepted active task.

## Parent adjudication and corrections

Check each finding against the artifact or reproducible evidence. Deduplicate root causes and record the reviewers' agreement and disagreement. Classify findings as `Act on`, `Consider`, `Noted`, or `Dismissed`, with evidence and a reason, especially for dismissals. A majority vote, model reputation, or self-reported confidence is not proof. The parent decides which correction best satisfies the requirements.

Apply accepted corrections only within existing task authority, then run affected checks. Every edit invalidates readiness for its affected scope. Obtain the required number of fresh independent reviews for that corrected scope, using its current risk tier, while retaining evidence for unaffected scope only when still applicable. A follow-up brief includes the original requirements, current candidate, prior findings, responses, and unresolved objections as claims to verify. Start new delegated tasks rather than continuing old reviewer chat histories.

Do not expand the assignment to satisfy speculative preferences or chase unanimous approval. Stop when the required coverage and evidence support a verdict; unresolved material concerns remain visible and cannot become a pass merely because a retry or usage limit was reached.

## Gate result

Report the reviewed candidate and scope, target and completed reviewer counts, actual models and any diversity, availability, or usage limits that affected coverage, verification evidence, disposition of findings, unresolved disagreements, and one gate status:

- `PASSED`: required independent reviews cover the final candidate, accepted required corrections are verified and independently reviewed, and no material blocker or evidence gap remains.
- `NEEDS_WORK`: evidence establishes a material defect or a required correction remains unresolved.
- `INCOMPLETE`: required reviews, artifacts, final-version coverage, or decisive verification evidence are missing. Explain exactly what is missing; this is not approval.

Keep specialist verdicts as supporting results; a worker's `READY` is not the combined gate result. Never claim independent or cross-model review that did not occur. Review grants no authority to publish, deploy, mutate external systems, or override access boundaries. Return results in chat; save a record in `.UAM/AINotes/` only when useful or requested.
