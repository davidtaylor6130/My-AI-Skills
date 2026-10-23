# Issue format

Read [the shared writing guide](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/writing-guide.md) for prose, evidence, review, factual model/app/harness
attribution and text publication. Use this structure for reports and requests unless David asks
otherwise. Repository templates may add fields. An issue describes work to assess or do; it does
not imply that a fix, test pass or acceptance has already happened.

## Title

Use `type(element): summary` when the affected area is known. Prefer `bug` for a reported defect
and `feature` for a requested capability; `refactor`, `docs` or `question` can fit other work.
Use a short, specific summary, ideally under 80 characters, without a final full stop.

Examples: `bug(settings): saved config path fails to reopen on Windows` and
`feature(search): filter results by date`.

Describe the reported problem or requested outcome, not an unverified cause or a completed fix.
If the affected area is unknown, use a clear plain title rather than inventing an element. The
title type is separate from labels; use the shared issue workflow's repository-owned label rules.

## Description order

1. **Short explanation.** State the problem or request, its impact and the source of the report
   when known. Separate independently actionable problems into separate issues.
2. **Reproduction or desired outcome.** For a bug, give available preconditions, reproduction steps
   and expected versus actual behaviour. If steps are missing, state that rather than inventing
   them. For a feature, describe the use case, desired behaviour and relevant constraints instead.
3. **Environment.** Include the affected version/revision, OS, configuration or dependencies only
   where relevant and recorded. This is the product environment, separate from the model's tools.
4. **Evidence and reproduction status.** Distinguish observed, user-reported and hypothetical facts.
   Say whether reproduction was attempted, what was tried and what happened, or that its status is
   not recorded. Include useful file/line or commit references, concise logs and graphical evidence
   only where applicable. A suspected cause remains a hypothesis. A passing unrelated test does
   not show that a reported bug is absent.
5. **Acceptance criteria, when useful.** List observable outcomes that would resolve the report or
   satisfy the request. Keep future checks unchecked. Do not turn a preferred implementation into
   a requirement unless agreed.
6. **Review.** Record actual triage/review, reviewers/models, rounds, verdicts and unresolved
   questions. Distinguish reviewing a report from reproducing a bug or reviewing a fix.
7. **Preparation and filing.** Name the actual model drafting/filing on behalf of David Taylor,
   with the actual host app and harness. Keep the original reporter distinct. Combine roles when
   they match; record separate models/environments when they differ.
8. **Generated with.** End with the tools actually used for the issue.

Scale the structure to the report. Combine short fields; omit inapplicable sections. If essential
details are missing, record the gap or ask a focused question. Do not fabricate facts to fill a
template. Use [the shared issue workflow](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/issue-workflow.md) for duplicate
search, repository-owned labels and the concrete filing decision.

## Body pattern

Replace placeholders with facts and remove inapplicable parts:

```markdown
<Short problem/request and impact, with the report's source when known.>

**Reproduction:** <Available preconditions and steps, or the missing details.>
**Expected:** <Expected behaviour.>
**Actual:** <Reported/observed behaviour.>
<For a feature, replace these with the use case and desired outcome.>

**Environment:** <Relevant product version/revision, OS and configuration, where recorded.>

**Evidence:** <Observed facts, user reports and hypotheses, clearly distinguished; links if useful.>
**Reproduction status:** <Actual attempt and result, not attempted, or not recorded, as supported.>

**Acceptance criteria:**

- [ ] <Observable outcome, if useful.>

**Review:** <Actual triage/review and its limits, or review history not recorded.>

**Prepared by:** <Drafting model> in <actual host app> (<actual harness>), on behalf of David Taylor.
<If a different model files it, add Filed by with that model and its actual environment.>

🤖 Generated with <tools actually used, with verified links when available>.
```

For the same model/environment, change `Prepared by` to `Prepared and filed by` only when filing.
Use the shared guide's wording for standalone CLIs and facts that are not recorded. Writing an
issue or accepting its text does not establish acceptance of a future implementation.
