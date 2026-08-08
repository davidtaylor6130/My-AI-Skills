# Model Profiles

Checked against official documentation on 2026-07-13. Model catalogs and plan access change often; verify the linked live pages before a paid or long-running evaluation.

## Surfaces

| Surface | Current targeting constraint | Profile |
|---|---|---|
| Gemini API free | Free text/chat access includes Gemini 3.5 Flash, 3.1 Flash-Lite, 3 Flash Preview, 2.5 Pro, 2.5 Flash, and 2.5 Flash-Lite. Gemini 3.1 Pro Preview is paid API only. Free-tier content may be used to improve Google products. | Use the exact API model ID and preserve endpoint, SDK, generation, thinking, and tool settings. Do not send secrets or private repository content without explicit approval. |
| Google AI Studio | Models can be tried without API token charges, but availability and product limits differ from the API. | Record AI Studio as the surface; do not call it an API free-tier result. |
| Gemini Apps | Flash-Lite, Flash, and Pro are exposed across no-plan, Plus, Pro, and Ultra tiers with different context and usage limits. Deep Think requires Ultra and Pro. | Record plan and thinking level; app labels may not equal API IDs. |
| Copilot Free / Student | Named model selection is not currently exposed; access is through Auto selection. | Optimise for `Copilot Auto`, not an assumed provider model. |
| Paid Copilot plans | Availability varies by plan, client, organization policy, preview status, and retirement. | Record plan, client, extension version, named model, reasoning, and context settings. |

## Free-Tier Gemini API Text Profiles

Verify the live pricing and models pages before every run. Keep quota, rate-limit, unavailable-tool, and safety-filter failures out of the prompt score. Use small fixed cases so the Ralph loop does not waste free quota.

### `gemini-3.5-flash`

- Prefer this stable model for the hardest free-tier coding, agentic, analysis, and multimodal text-output tasks.
- Use concise, direct instructions and one consistent Markdown or XML structure. Put critical behavior and output rules first.
- Put long context before the task, then anchor the question with “Based on the preceding information...”. State desired verbosity explicitly.
- Keep default sampling; remove legacy `temperature`, `top_p`, and `top_k` tweaks unless fixed tests prove they help.
- Use `thinking_level`: start at `medium` for most work, `minimal` for quick factual or simple tool tasks, `low` for shorter coding or agentic work, and `high` for genuinely complex cases.
- Do not promise current facts through Google Search grounding on the free tier when the live pricing page marks grounding unavailable.

### `gemini-3.1-flash-lite`

- Use this stable model for high-volume translation, transcription, classification, extraction, routing, document triage, and lightweight agentic tasks.
- Give one bounded operation, explicit labels or schema, and the exact allowed output. Use system instructions such as “Only output the translated text” when extra prose is a failure.
- Prefer structured outputs for extraction and classification. Add a few consistent examples only when the schema alone does not stabilize behavior.
- Keep `thinking_level` at `minimal` for straightforward high-throughput work. Increase it only when the same fixed tests improve; route deep debugging or broad planning to 3.5 Flash instead of bloating the prompt.
- Do not ask for Search or Maps grounding on the free tier when the live pricing page marks those tools unavailable.

### `gemini-3-flash-preview`

- Optimise this preview model only when the user is pinned to it; otherwise recommend testing the same prompt on stable `gemini-3.5-flash`.
- Follow the Gemini 3 structure: concise instructions, critical rules first, explicit verbosity, long context before the final anchored task.
- Record preview status and model ID in every ledger entry. Do not treat behavior changes between runs as prompt improvements without repeats.
- Test `thinking_level` separately from wording. Its default differs from 3.5 Flash, so never compare scores without recording the level.
- Avoid investing in preview-specific prompt work that the stable replacement already passes.

### `gemini-2.5-pro`

- Use this model for complex reasoning, difficult coding, research synthesis, and long-context work available within free-tier limits.
- State the goal, supplied evidence, constraints, required output, and acceptance checks. Use a few varied, consistently formatted examples for brittle behavior.
- Keep reasoning private. On legacy `generateContent`, use `thinkingBudget`; Pro thinking cannot be disabled. On the Interactions API, use the currently documented thinking control.
- Do not ask the prompt to compensate for unavailable free-tier grounding. Supply current evidence directly or mark the test unsupported.

### `gemini-2.5-flash`

- Use this balanced model for low-latency, high-volume tasks that still need reasoning.
- Give a clear task, relevant context, explicit output contract, and consistent few-shot examples. Prefer structured outputs for non-trivial JSON.
- Tune thinking separately from prompt text. On legacy `generateContent`, start with dynamic thinking, use `thinkingBudget = 0` for simple deterministic work, and increase the budget only when fixed tests justify it.
- Enable Search grounding only when the live free-tier allowance supports the test; record grounded and ungrounded runs separately.

### `gemini-2.5-flash-lite`

- Use this model for the simplest high-volume classification, extraction, transformation, and routing tasks.
- Give one operation, a strict schema or label set, minimal relevant context, and one or two consistent examples. Reject extra commentary in the test contract.
- Thinking is off by default. Enable it only when a fixed case needs additional reasoning; move multi-step or ambiguous work to 2.5 Flash or 3.5 Flash instead of adding prompt scaffolding.
- Use structured outputs whenever the required response is data rather than prose.

### Excluded free-tier endpoints

Do not apply these text/chat profiles to Live audio, translation audio, TTS, image generation, embedding, robotics, or other specialized endpoints. Research their modality-specific prompt guides and define modality-specific tests before adding them.

## Copilot Model Profiles

Current named catalog: GPT-5 mini; GPT-5.3-Codex; GPT-5.4, 5.4 mini, and 5.4 nano; GPT-5.5; GPT-5.6 Luna, Sol, and Terra; Claude Fable 5; Claude Haiku 4.5; Claude Opus 4.5, 4.6, 4.7, 4.8, and 4.8 fast preview; Claude Sonnet 4.5, 4.6, and 5; Gemini 2.5 Pro, 3 Flash, 3.1 Pro, and 3.5 Flash; MAI-Code-1-Flash; Raptor mini; and Kimi-K2.7-Code. Some clients or plans expose only a subset.

### GPT-5 mini

Recognize `GPT-5 mini` as the Copilot label and `gpt-5-mini` as the API ID. Do not apply this profile merely because another model contains “mini.”

- Use it for well-defined coding, writing, explanation, and interactive debugging tasks where latency or volume matters.
- State one bounded outcome, only the relevant context, explicit constraints, the output shape, and observable acceptance checks.
- Split broad or loosely connected work into separate prompts. Add a short example only when formatting or classification remains unreliable.
- Prefer precise instructions over long personas, repeated reminders, or elaborate planning scaffolds.
- On the API, test `reasoning_effort` and `verbosity` separately from prompt wording. Start with lower reasoning for simple work and increase it only when the fixed tests improve. Do not assume Copilot exposes the same controls.
- Record API and Copilot results separately. Their surrounding instructions, context selection, tools, and available settings differ.

### GPT-5.4 mini

Recognize `GPT-5.4 mini` as the Copilot label and `gpt-5.4-mini` as the API ID. Treat it as a distinct model from GPT-5 mini.

- Use it for targeted edits, codebase search and navigation, front-end generation, debugging loops, computer use, and narrow parallel subagent tasks.
- State the bounded subtask, relevant repository paths or search target, permitted tools, required evidence, acceptance command, and stop condition.
- For exploration, ask it to report exact files and symbols before proposing changes. For implementation, require inspection before editing and the smallest relevant verification afterward.
- Keep planning, cross-system architecture, and final judgment with a larger model when one prompt cannot be made narrow without losing essential context.
- On the API, test `reasoning_effort` from `none` or `low` for simple search/edit work toward `medium`, `high`, or `xhigh` only when fixed tests justify the added latency. Do not assume Copilot exposes every API setting.
- Track navigation precision, unnecessary file changes, tool-call errors, verification success, latency, and token use in the Ralph ledger.

### Other GPT and Codex

- Put outcome, repository context, constraints, and completion tests in that order.
- Use GPT-5.4/5.5 or Sol for deep debugging and architecture; Luna for small repetitive work; Terra for balanced agent work.
- Use GPT-5.3-Codex for agentic implementation. Name relevant paths and executable checks without scripting every tool call.
- Set reasoning level in Copilot when available. Do not pad the prompt with requests to reveal reasoning.

### Claude

- Give clear, explicit instructions and say what the output should do rather than only what it must avoid.
- Explain why a constraint matters when that helps generalization. Keep examples consistent with desired behavior.
- Use XML tags for distinct context, task, constraints, and examples when boundaries are otherwise ambiguous.
- Use Haiku for narrow fast tasks, Sonnet for general coding/agents, and Opus for difficult reasoning. For Fable long-horizon work, specify acceptance tests, permit upfront planning and independent parallel tools, and require checking the pre-existing test state before debugging.

### MAI-Code-1-Flash and Raptor mini

- Use a concise goal, relevant code, explicit output, and one small task at a time.
- Prefer these for quick completions, explanations, or repetitive edits. Move multi-layer architecture work to a deeper model.
- Re-test MAI prompts periodically because GitHub describes the checkpoint as continuously improving.

### Kimi-K2.7-Code

- Use clear detailed instructions, delimiters, steps, examples, desired length, and reference text.
- Summarize or filter stale history in long conversations. Keep autonomous coding acceptance tests concrete.

## Official Sources

- Google Gemini models: https://ai.google.dev/gemini-api/docs/models
- Google Gemini API pricing and free-tier matrix: https://ai.google.dev/gemini-api/docs/pricing
- Google Gemini prompt strategies: https://ai.google.dev/gemini-api/docs/prompting-strategies
- Google Gemini 3 developer guide: https://ai.google.dev/gemini-api/docs/gemini-3
- Google Gemini 3.5 Flash guide: https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5
- Google Gemini 3.1 Flash-Lite guide: https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite
- Google Gemini thinking controls: https://ai.google.dev/gemini-api/docs/thinking
- Gemini Apps plans, models, context, and thinking levels: https://support.google.com/gemini/answer/16275805
- GitHub Copilot supported models and plans: https://docs.github.com/en/copilot/reference/ai-models/supported-models
- GitHub Copilot model comparison: https://docs.github.com/en/copilot/reference/ai-models/model-comparison
- GitHub Copilot prompting: https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering
- OpenAI GPT-5 mini model: https://developers.openai.com/api/docs/models/gpt-5-mini
- OpenAI GPT-5 developer guidance: https://openai.com/index/introducing-gpt-5-for-developers/
- OpenAI GPT-5.4 mini guidance: https://openai.com/index/introducing-gpt-5-4-mini-and-nano/
- Anthropic Claude prompting: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices
- Moonshot Kimi prompting: https://platform.moonshot.ai/docs/guide/prompt-best-practice
