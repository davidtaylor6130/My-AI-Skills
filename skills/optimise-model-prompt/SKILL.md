---
name: optimise-model-prompt
description: Optimise and regression-test prompts for specific Gemini API, Gemini app, and GitHub Copilot models, including free-tier Gemini text models, GPT-5 mini, and GPT-5.4 mini, with a Ralph-style iteration loop and a Markdown unit-test ledger. Use when a user asks to tune, compare, benchmark, or iteratively improve a prompt for Gemini, Copilot Auto, GPT, Claude, MAI, Raptor, or Kimi models available through those surfaces.
---

# Optimise Model Prompt

Optimise against measured behavior and guidance for the exact target model, not generic prompt folklore. Preserve the user's intent, safety constraints, and required output while changing the fewest prompt elements.

## Require the Exact Target

Before changing the prompt, require:

- Exact model name or API ID.
- Surface: Gemini API, Google AI Studio, Gemini Apps, or GitHub Copilot.
- Plan when access depends on it.
- Original prompt and intended result.

If the exact model or surface is missing, ask one concise question for both and stop optimisation until answered. Do not silently choose a model. For Copilot Free or Student, target `Copilot Auto` unless current official documentation exposes named model selection; never claim a named model was tested when Auto chose it.

For Gemini API targets, also record the API endpoint or SDK method and thinking configuration when known. The Interactions API and legacy `generateContent` API may expose different controls.

## Research That Model

1. Search current official platform and model-provider documentation for the exact model before editing the prompt. Prefer model-specific pages over family-wide advice.
2. Confirm current availability, retirement or preview status, plan/client limits, reasoning or thinking controls, context behavior, tool support, sampling advice, and prompting tips or known quirks.
3. Record the URLs and retrieval date in the final result. Clearly separate official guidance from inference based on test results.
4. Read [model-profiles.md](references/model-profiles.md) as cached orientation, not as a replacement for live research. If internet access is unavailable, disclose that the optimisation uses cached guidance and may be stale.
5. Obtain representative inputs, required outputs, and authenticated access to the target surface. If the target model cannot be run, produce a candidate and test plan, but label it unmeasured.

## Define Tests Before Editing

Create the smallest representative test table before changing the prompt:

```markdown
| Test | Input | Pass condition | Baseline |
|---|---|---|---|
| T1 | <representative input> | Contains `APPROVED`; contains no `TODO` | PASS/FAIL |
```

Make every pass condition observable: exact text, valid JSON shape, maximum length, required facts, forbidden content, successful downstream unit tests, or a user-approved rubric. Avoid vague checks such as “better” or “high quality.”

Keep at least one final holdout case outside the tuning loop when enough examples exist. Do not weaken checks to make a candidate pass.

## Run the Ralph Loop

1. Save the unchanged prompt and run iteration `0` as the baseline.
2. Form one explicit hypothesis from the failing tests and the target model profile.
3. Change one prompt behavior at a time. Prefer clearer task, context, constraints, examples, and output contract over extra persona prose.
4. Run the same cases, model settings, and repeat count. Record every result in the Markdown ledger below.
5. Keep a candidate only when it improves the fixed score without breaking a hard requirement. Revert regressions.
6. Stop when all cases pass, five iterations complete, or two consecutive iterations fail to improve. Run the holdout once against the best candidate.

Use this ledger throughout the loop:

```markdown
## Prompt optimisation ledger

Target: <surface / plan / exact model / settings>

| Iteration | Single tweak | Passed | Failed | Score | Decision |
|---:|---|---:|---:|---:|---|
| 0 | Baseline | 2 | 2 | 50% | Keep as baseline |
| 1 | Put output contract before context | 3 | 1 | 75% | Keep |

### Iteration 1 unit tests

- PASS T1 — <observable evidence>
- FAIL T2 — expected <x>; received <y>
- PASS T3 — <observable evidence>
- PASS T4 — <observable evidence>
```

Do not put credentials or unnecessarily reproduce private model responses in the ledger.

## Model-Specific Rules

- Keep reasoning private. Ask for verification or a concise rationale, not hidden chain-of-thought.
- For Gemini 3.x, use direct instructions, one consistent delimiter style, explicit verbosity, critical rules first, and the task after long context. Keep default sampling unless a measured case proves otherwise.
- For Gemini 2.5, use clear examples and control thinking through the surface setting rather than repeated “think step by step” prose.
- For a free-tier Gemini text model, use the exact API-ID profile in [model-profiles.md](references/model-profiles.md). Treat quota, `429`, unavailable-tool, and safety-filter failures as infrastructure results, not prompt-quality failures.
- For Copilot, name relevant files or selections, state the goal before requirements, include examples, and keep chat history relevant.
- For Claude, state desired behavior positively and explicitly, explain important reasons, align examples with the desired output, and use XML tags when they clarify boundaries.
- For `GPT-5 mini` or `gpt-5-mini`, use its exact profile in [model-profiles.md](references/model-profiles.md); do not merge it with GPT-5.4 mini guidance.
- For `GPT-5.4 mini` or `gpt-5.4-mini`, use its exact profile in [model-profiles.md](references/model-profiles.md); optimise for bounded coding, codebase navigation, debugging loops, or subagent work.
- For other fast or mini models, reduce scope and ambiguity before adding detail. For deep-reasoning models, state acceptance tests and let the configured reasoning mode do the work.

## Deliver

Return:

- The best prompt in a single copyable block.
- Exact surface, model, and settings tested.
- Baseline and best pass counts.
- One line per retained tweak with its measured effect.
- Remaining failures, holdout result, and any unmeasured assumptions.

Never describe a prompt as universally optimal. Say it is the best candidate for the recorded cases and settings.
