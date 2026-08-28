---
name: user-experience-design
description: Design or audit complete product experiences across websites, desktop software, mobile apps, games, and other interactive products. Use automatically for user journeys, task flows, information architecture, navigation, guidance, feedback, error prevention, and recovery. A broad UX request defaults to a full product experience audit; a named feature, screen, role, or journey stays scoped. Use Wayfinder only when a clear destination is too large or uncertain for one normal working session. Exclude purely visual styling and tiny copy-only edits.
---

# User Experience Design

Make meaningful journeys understandable, recoverable, and complete without forcing users to understand the whole system first.

## Scope

A broad UX request without a narrower area begins with a full product experience audit across its principal journeys, not a mechanical visit to every screen. Adapt coverage to the product and platform. Use a specialised site, desktop, or mobile review skill to operate the real surface when available; this skill owns the journey model and UX judgment.

A request naming a feature, screen, role, journey, or problem stays within that boundary. When this skill supports another task, inherit that task's scope rather than expanding it. If the product boundary, intended actors, destination, or available surface is materially unclear, ask before proceeding.

## Wayfinder

Use `wayfinder` only when all are true: the experience is too large or uncertain for one normal working session, a meaningful destination can be stated, and important questions prevent a trustworthy journey map or plan. A broad request is a reason to evaluate this gate, not proof that Wayfinder is needed. If one agent can handle the work honestly in one pass, do it directly.

Wayfinder resolves the blocking decisions; it does not perform the audit or implementation. Return to this skill when the route is clear. Do not use it merely because the product has many screens or stories.

## Journeys and feedback

Build journeys from product evidence before making recommendations. For each materially different user or role, capture the actor, starting context, goal, key actions, and observable success. Cover the primary path, first use, interruption and recovery, and return use; add role, permission, input-method, accessibility, or platform-lifecycle variants only when they change the experience.

Use capability bands such as new, regular, and expert users when knowledge changes the journey. Do not invent names, biographies, demographics, or multiple personas that behave the same. Formal “As a user…” wording is optional; a story is useful only when it clarifies a distinct need.

Treat inferred journeys as assumptions, not facts. When a misunderstanding could materially change the product, show the user a compact journey set and ask them to confirm the disputed intent before designing around it. Stakeholder confirmation establishes product intent; it does not replace evidence from actual users. Prefer observed behaviour, usability sessions, analytics, support reports, and existing research when available. Do not contact users or enable tracking without explicit authority.

When genuinely different journeys are hard to judge in prose, use `prototype` to compare the smallest useful alternatives before implementation.

## UX judgment

- Make the next action, prerequisites, result, and consequence clear.
- Show what is needed for the current decision; disclose advanced or rare detail without hiding risk, cost, or irreversible consequences.
- Remove steps, choices, fields, explanations, and interruptions that do not help the user's goal.
- Preserve context and user work through back, cancel, retry, undo, interruption, and return.
- Add guidance only where labels, examples, defaults, and the interface itself cannot make the action clear.
- Cover loading, empty, error, blocked, disabled, success, and completed states where relevant.
- Use the user's vocabulary and put feedback or errors beside the action they concern.

## Verification and output

Verify complete journeys on the real product with representative content, roles, permissions, failures, and platform lifecycle where practical. Static inspection or visual polish alone cannot verify comprehension.

For a full audit, report the journey set, coverage and evidence, cross-journey problems, prioritised findings, strengths to preserve, and untested assumptions. For a scoped review, report only the affected journey. Use: `[priority] [journey step] — [user obstacle] → [smallest useful change]`.

Return `VERIFIED`, `INCONCLUSIVE`, or `BLOCKED`. Never deploy, change production, contact users, enable analytics, or perform destructive actions without explicit authority.
