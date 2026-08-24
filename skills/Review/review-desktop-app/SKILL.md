---
name: review-desktop-app
description: "Review a native or Electron desktop application on the real running product for user journeys, progressive disclosure, guidance, platform conventions, keyboard and window behaviour, accessibility, persistence, recovery, performance, installation, and updates. Use automatically for whole desktop-app reviews, release-readiness checks, or requests to find and prioritise desktop experience problems. Exclude websites, mobile apps, narrow code review, and isolated visual edits."
---

# Review Desktop App

Judge the application users launch and operate, not a test summary or screenshot alone.

## Inputs

Use the executable or launch command, target operating systems, intended users and journeys, build identity, test data, and existing verification harness. Prefer an installed or packaged build when release behaviour matters.

## Workflow

1. Map first launch, the primary task, interruptions, recovery, settings, persistence, and return use. Include install, update, and uninstall only when in scope.
2. Launch the real app and record OS, build, window state, data location, and isolation assumptions.
3. Apply `user-experience-design` first. Check orientation, next-action clarity, progressive disclosure, contextual guidance, undo, error recovery, and preservation of user work.
4. Apply `de-vibe-design` only when visual design or polish is in scope. Check hierarchy, density, resizing, high-DPI behaviour, focus, keyboard navigation, menus, dialogs, shortcuts, contrast, loading, empty, disabled, and error states.
5. Exercise multiple windows, minimise/restore, relaunch, interrupted work, corrupt or missing optional data, offline behaviour, and slow operations where relevant. For Electron, test the packaged app or its actual browser/debug surface rather than treating unit tests as proof.
6. Inspect logs, process behaviour, startup/resource measurements, crashes, and accessibility tooling as evidence proportional to the review.
7. Rank findings by user harm and confidence. Keep product defects distinct from harness or environment failures.

Do not alter real user data, installers, signing, production services, or release channels without explicit authority. Use isolated profiles and disposable data where possible.

## Verification

Repeat affected journeys in the same real application surface and confirm persistence or recovery across relaunch when relevant. Preserve steps, screenshots, logs, build identity, and measurements.

## Output

Return `READY`, `NEEDS_WORK`, `INCONCLUSIVE`, or `BLOCKED`, plus tested journeys and environment, prioritised evidence-backed findings, strengths to preserve, untested areas, and the next highest-value check. If launch fails, give the exact command and failure evidence. A single agent is the baseline; add independent review only for a broad or high-risk release candidate.
