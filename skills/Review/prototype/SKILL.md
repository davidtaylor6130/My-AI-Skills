---
name: prototype
description: "Build a small disposable prototype to answer one unresolved product, interaction, visual, state-model, or logic question with runnable evidence. Use automatically when several genuinely distinct alternatives are hard to judge on paper, when a user asks to try or compare approaches, or when a cheap experiment can remove uncertainty before implementation. Exclude debugging existing failures, implementation-ready work, small obvious corrections, and prototypes that would touch production data or services."
---

# Prototype

A prototype answers one question. It is evidence for a decision, not an early production implementation.

## Inputs

Identify the question, the decision it unlocks, the minimum realistic inputs, the comparison criteria, and a stop predicate. Infer these from the task when safe; ask only when different answers would produce materially different experiments.

## Choose the smallest branch

- **Experience or visual question:** create meaningfully different variants on one isolated route or static artifact with an obvious switcher. Apply `user-experience-design` to journey and progressive disclosure; apply `de-vibe-design` when visual direction is being compared.
- **State or logic question:** create a tiny interactive harness that exposes the complete relevant state after each action and includes awkward transitions, not only the happy path.
- **Feasibility question:** create the smallest isolated spike that exercises the uncertain boundary and records observable success or failure.

## Rules

1. Mark the artifact `PROTOTYPE` and keep it outside production paths, data, credentials, and services.
2. Reuse the repository's runtime and task runner when cheap; otherwise prefer a standalone local artifact. Add no dependency unless the question cannot be answered without it.
3. Keep state in memory by default. Use disposable local data only when persistence is the question.
4. Build only what makes the comparison runnable: no production hardening, speculative abstraction, analytics, or broad test suite.
5. Make variants structurally distinct. Several cosmetic variations do not settle a design question.
6. Put controls, assumptions, and current state where the reviewer can see them. Make it runnable with one clear command or direct file open.
7. Stop when the question is answered. Do not merge prototype code into production or create branches, commits, tracker entries, or external messages without authority.

This adapts the useful question-first and visual-versus-logic split from Matt Pocock's prototype workflow while remaining local-first and provider-agnostic.

## Verification

Run the prototype once through every comparison or critical transition. Confirm it can distinguish the alternatives and capture the resulting evidence. A prototype that only compiles is not verified.

## Output

Return:

- the question and stop predicate;
- how to run the prototype and where it lives;
- alternatives or transitions exercised;
- evidence and verdict;
- limitations and conditions that could reverse the decision;
- the recommended production direction, without silently implementing it.

If the environment cannot run the artifact, report `BLOCKED` with the exact failed command and missing prerequisite. Use one agent by default; independent variants are optional only when they improve the comparison.
