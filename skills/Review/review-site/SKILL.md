---
name: review-site
description: "Review a website or browser application on its real rendered surface for user journeys, progressive disclosure, guidance, responsive behaviour, accessibility, visual quality, content, failures, and performance. Use automatically for whole-site reviews, launch-readiness audits, or requests to find and prioritise web experience problems even when the skill is not named. Exclude isolated copy or style edits, native desktop or mobile apps, and security-only reviews."
---

# Review Site

Review the experience a visitor can actually use, not only its source code.

## Inputs

Use the URL or launch command, intended users and goals, supported viewports, existing requirements, and any authenticated test account the user has supplied. Do not request credentials unless the journey genuinely requires them.

## Workflow

1. Establish the main user journeys and success criteria from the product and repository. Start with the first visit, primary task, recovery path, and return visit.
2. Launch the real site with its existing browser harness when available. Record environment, viewport, build, and any data assumptions.
3. Apply `user-experience-design` to each journey first. Check that the next action is obvious, essential choices appear before advanced ones, guidance arrives at the point of need, and users can recover without losing work.
4. Apply `design` only when visual design or polish is in scope. Review hierarchy, spacing, typography, responsive layout, states, controls, focus, keyboard use, overlays, contrast, and motion.
5. Exercise loading, empty, error, disabled, slow-network, validation, refresh, back/forward, and narrow/wide viewport behaviour where relevant.
6. Use available accessibility, console, network, and performance checks as supporting evidence. Do not let automated scores replace direct journey testing.
7. Rank findings by user harm and confidence. Separate defects, usability friction, visual polish, content issues, and unverified risks.

Do not redesign the product during a review unless asked. Do not publish, deploy, submit forms with external effects, create accounts, purchase, or message users without explicit authority.

## Verification

Re-run each journey affected by a proposed or completed change on the same rendered surface. Preserve reproducible evidence such as steps, screenshots, logs, timings, or accessibility output. Compilation and static inspection are not user-facing proof.

## Output

Return:

- overall verdict: `READY`, `NEEDS_WORK`, `INCONCLUSIVE`, or `BLOCKED`;
- tested journeys, environments, and viewports;
- prioritised findings with reproduction, user impact, evidence, and recommended outcome;
- what worked well and should be preserved;
- evidence limits and the next highest-value check.

If the site cannot run, report the exact failing command, missing prerequisite, and what static review could and could not establish. A single agent is sufficient; use independent review only for a broad or high-risk release audit.
