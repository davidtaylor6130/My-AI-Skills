# GitHub writing and attribution

Use these rules for issues, pull requests and release notes unless David requests another format.
Repository templates may add required fields. Keep the common facts while adapting the structure
to the artifact. These writing rules do not grant permission to publish or change GitHub state.

## Clear, proportionate prose

Lead with the concrete problem, requested outcome or delivered behaviour. Write for someone who
has not read the originating conversation. Use short, active sentences and familiar words. Avoid
promotional claims, dramatic punctuation, canned transitions and closing thanks or summaries.
Use bullets or a table only when they make distinct facts easier to assess. Omit empty sections.

Apply this prose style to cleanup reports and README edits while respecting the project's voice.
Do not impose issue/PR titles or attribution blocks on short repository
metadata, topics or licence text; preserve established README and changelog structures.

## Evidence and review

- Distinguish direct observation, user reports and hypotheses. A code comment or plausible code
  path is evidence to investigate, not proof that a runtime failure occurred.
- Tie checks and claims to the relevant revision, workload and environment when recorded. State
  the actual result and material failures or unrun checks. Do not invent tests, screenshots,
  performance measurements, acceptance or independent validation.
- Keep synthetic checks, real runtime/platform checks and user acceptance distinct. Passing tests
  do not establish independent review or David's acceptance.
- Use [the review workflow](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/review-workflow.md) for agent/iteration counts, per-agent
  suggestions and implemented changes, reviewer selection, follow-up rounds and usage-limit waits.
  Keep self-review separate. Missing required review blocks publication; it is not just a body caveat.
- Use visual evidence only for graphical or visible interaction behaviour when it helps assess
  the report or change. Use actual product captures, label states and give GitHub readers accessible
  assets. Identify user-supplied captures. Never present a mockup or style reference as product
  evidence. State a relevant visual verification gap when a capture cannot be obtained.

## Factual attribution

Use recorded thread/run metadata, implementation history and review receipts. Name the actual model
directly when it acts on behalf of David Taylor; do not substitute the generic label "AI assistant".
The model identity, host app and harness are separate facts. Never default to T3 Code, Codex,
Claude Code or the current model for work performed elsewhere. Unknown facts stay `not recorded`.
Record reasoning effort only when recorded and useful.

Record roles separately when contributors or environments differ:

- **PR:** implementation model/environment and PR-preparing/opening model/environment.
- **Issue:** the report's source and issue-drafting/filing model/environment. Filing a report does
  not mean the model observed it, reproduced it or implemented a fix.
- **Release:** implementation contributors where recorded and the notes-preparing/publishing
  model/environment. Preparing notes does not establish authorship of all released changes.

For each model's environment, name the actual host app when applicable and the harness. For a
standalone CLI with no host app, write `using <actual harness>`; do not invent an app. If only some
facts are known, name those and mark the missing facts `not recorded` in the applicable field.
Scope attribution to this change. Omit commentary about inherited/shared base work, ownership
exclusions or why another task's work is not attributed; it does not belong in the artifact.

When the model, host app and harness match across implementation and PR preparation/opening, use
one `Created with` line for both roles, on behalf of David Taylor. Do not repeat the same identity
under another heading. When they differ, use `Created with` for implementation and a separate
`PR prepared by` or `PR opened by` line for the actual PR role. A local draft is prepared; a GitHub
draft PR has still been opened. Likewise combine matching preparation/filing or notes/publication
roles; use `Filed by` or `Published by` only after the action. Preserve actual task contributor and
review history when another model later edits the description.

Keep attribution in these role lines. Do not add a separate `Generated with` or tools-used footer.

## Publication mechanics

Read [the shared publishing workflow](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/publishing.md) for exact Markdown files,
real newlines, image/video uploads, approval, verification and partial-failure recovery.
