---
name: user-experience-design
description: Design and review user journeys, task flows, information architecture, navigation, progressive disclosure, onboarding, in-product guidance, feedback, error prevention, and recovery. Use automatically when users may not know what to do next, a workflow feels confusing or overwhelming, important information appears at the wrong time, or a product needs clearer guidance through a multi-step task. Exclude purely visual styling, branding, spacing, colour, and small copy-only edits.
---

# User Experience Design

Make the next useful action clear without forcing the user to understand the whole system first.

## Inputs

The audience, their goal, entry point, current journey, required information, decisions, risks, product constraints, representative content, and available behavioural evidence.

## Workflow

1. State the user's goal in their language and map the shortest successful journey as actions.
2. Identify what the user knows at entry, what the system knows, and what must be learned or decided at each step.
3. Remove steps, choices, fields, explanations, and interruptions that do not help the current decision.
4. Apply progressive disclosure using the rules below.
5. Make the primary next action, its prerequisites, expected result, and consequence explicit.
6. Design prevention and recovery for invalid input, interruption, cancellation, retry, undo, partial completion, and return visits.
7. Add guidance only where the interface cannot make the action self-evident. Prefer labels, examples, defaults, and contextual help over tours or walls of instructions.
8. Cover first use, empty, loading, error, blocked, success, and completed states without discarding user work.
9. Exercise the journey with realistic users, content, and failure cases on the real product when practical.

## Progressive disclosure

- Show only the information and controls needed for the current decision.
- Keep the primary path visible; place advanced, rare, administrative, diagnostic, and historical detail behind clearly named disclosure.
- Reveal prerequisites before an action becomes relevant, not after it fails.
- Preserve context when revealing detail. Prefer inline expansion or a secondary region when leaving the page would disrupt the task.
- Do not hide essential constraints, costs, uncertainty, destructive consequences, security implications, or information required for informed consent.
- Do not use hover as the only route to necessary information.
- Remember disclosure state only when doing so helps the user's next visit and does not conceal changed risk.
- Let users inspect details before committing and return to the summary without losing work.
- Use staged forms only when grouping reduces cognitive load; do not turn a short form into a needless wizard.

## User guidance

- Use the user's vocabulary and one consistent name per concept.
- Explain what to do, why it matters only when non-obvious, and what happens next.
- Put help beside the decision it supports and errors beside the field or action that caused them.
- Prefer a realistic example or constrained default over a paragraph.
- Empty states should explain the value, first action, and any prerequisite without pretending sample data is real.
- Loading feedback should say what is happening and preserve the user's sense of progress; use determinate progress when available.
- Success feedback should confirm the result and expose the next likely action without trapping the user in celebration screens.

## When not to use

Skip isolated visual polish, token changes, straightforward CSS fixes, and tiny wording corrections. Do not add onboarding, tooltips, dialogs, steps, or documentation merely because the interface has space. A single agent and local inspection are the baseline; use research or additional reviewers only when the audience or evidence is genuinely uncertain.

## Verification and output

Verify the real journey rather than individual screens alone. Check first use, normal completion, back/cancel, invalid input, interruption, retry, keyboard operation, and preservation of entered data where relevant. Report:

`[priority] [journey step] — [user obstacle] → [smallest flow or guidance change]`

State tested paths, evidence, untested assumptions, and a verdict of `VERIFIED`, `INCONCLUSIVE`, or `BLOCKED`. Do not claim user comprehension from static metadata or visual polish. Never deploy, contact users, change production, or perform destructive actions without explicit authority. No subagent, internet connection, provider-specific feature, or paid service is required.
