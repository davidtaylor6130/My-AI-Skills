# Pull request format

Read [the shared writing guide](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/writing-guide.md) for prose, evidence, review, factual model/app/harness
attribution and text publication. Use this PR structure unless David requests another format.
Repository templates may add required fields. Keep the description proportional to the change.

## Title

`type(element): summary`

Use a lowercase type: `fix`, `feat`, `perf`, `refactor`, `test`, `docs`, `build` or `chore`.
The element identifies the affected area or subsystem in the actual repository, such as `parser`,
`auth`, `search` or `storage`. Describe the resulting change without adding the worktree name.

Examples: `fix(parser): reject incomplete configuration records` and
`perf(search): reuse parsed query plans`.

## Description order

1. **Short explanation.** State the problem, change and resulting behaviour. Include an essential
   boundary or dependency when it changes what the PR delivers.
2. **Visual evidence, when applicable.** For graphical or visible interaction changes, show labelled
   before/after views or a relevant state comparison from the actual product. Omit this block for
   code-only and test-only changes. Record a relevant capture/verification gap if needed.
3. **Proof.** Give the checks actually run and their results. Where available, explain a regression
   failing before the fix and passing after it. Performance claims need measured before/after values
   for the same workload and budgets. State relevant failures or unrun checks; link detailed evidence
   rather than pasting logs. A compact metrics table belongs here when useful.
4. **Review.** Use [the review workflow](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/review-workflow.md)'s compact agent/iteration summary and one
   line per reviewer with actual suggestion/implementation counts. Keep detailed findings in the
   review records. Required review must be complete before publication.
5. **Creation and submission.** Name the actual implementation model/environment and the model
   preparing/opening the PR on behalf of David Taylor. Include each role's host app and harness;
   use one line when the model and environment match, and separate role lines only when they differ.

Keep unresolved checks or dependencies beside the relevant proof/review statement. Link related
issues or task identifiers where useful. Do not turn this into an empty checklist for every PR.

## Body pattern

Replace the explanatory placeholders with verified facts and remove inapplicable parts:

```markdown
<Short explanation of the problem and resulting behaviour.>

<For graphical/interaction changes only: labelled screenshots or a recording.>

**Proof:** <Actual checks, regression evidence and results; relevant unrun checks or limitations.>

**Review:** Reviewed by <N> agents over <M> iterations.

- Agent 1: <exact model ID> — suggested <X>; implemented <Y>.
- Agent 2: <exact model ID> — suggested <X>; implemented <Y>.

**Created with:** <Model for implementation and PR> in <actual host app> (<actual harness>), on behalf of David Taylor.
```

Use only the reviewer lines that actually apply; this pattern does not prescribe two reviewers.
Record any rejected/out-of-scope suggestions briefly rather than implying they were implemented.

The single attribution line is the default when the roles match. When they differ, replace it with:

```markdown
**Created with:** <Implementation model> in <actual host app> (<actual harness>).
**PR prepared by:** <PR-preparing model> in <actual host app> (<actual harness>), on behalf of David Taylor.
```

Use `PR opened by` once the PR is opened, even when it is a GitHub draft. Follow the shared guide
for standalone CLIs and facts that are not recorded. Do not append inherited-work disclaimers.
