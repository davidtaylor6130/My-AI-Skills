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
Do not impose issue/PR titles, attribution blocks or generation footers on short repository
metadata, topics or licence text; preserve established README and changelog structures.

## Evidence and review

- Distinguish direct observation, user reports and hypotheses. A code comment or plausible code
  path is evidence to investigate, not proof that a runtime failure occurred.
- Tie checks and claims to the relevant revision, workload and environment when recorded. State
  the actual result and material failures or unrun checks. Do not invent tests, screenshots,
  performance measurements, acceptance or independent validation.
- Keep synthetic checks, real runtime/platform checks and user acceptance distinct. Passing tests
  do not establish independent review or David's acceptance.
- Name actual reviewers or reviewing models, recorded rounds, verdicts and how significant findings
  were handled. Label self-review as self-review. Pending review stays pending. If review history
  is unavailable, say `not recorded`; say no review occurred only when that fact is known.
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
facts are known, name those and mark the missing facts `not recorded`. When roles and environments
match, combine them into one accurate line. For a draft use `Prepared by`; use `Opened by`,
`Filed by` or `Published by` only when that action occurs. Preserve factual implementation and
review history when another model later edits the description.

End issues, PRs and release notes with a short `🤖 Generated with ...` line naming the tools actually
used for the artifact. Link tool names only when the product links are verified. This footer does
not replace model/app/harness attribution and must not imply the current tools made earlier work.

## Publication mechanics

Read [the shared publishing workflow](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/publishing.md) for exact Markdown files,
real newlines, image/video uploads, approval, verification and partial-failure recovery.
