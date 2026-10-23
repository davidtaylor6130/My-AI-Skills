# Repository context

Gather enough context for the requested task. Do not dump a fixed number of commits or the whole
issue backlog before knowing why they matter.

1. Confirm the working directory, project and intended GitHub destination. Read applicable project
   instructions, the README and relevant contribution, issue/PR templates and release guidance.
2. Detect the actual version-control system and working-copy state. Use its native tools to inspect
   local changes, revisions, branches/workspaces and remote mappings. Do not assume every project
   uses Git, that its branch is `main`, or that its checkout is clean. Preserve unrelated work.
3. Establish the task's scope and evidence: the referenced report, affected behaviour, proposed diff,
   release range or cleanup area. Read the history, tests, docs and hosted records that answer those
   questions. Expand the search when findings justify it, not to satisfy an arbitrary inventory.
4. Discover available tooling before choosing commands. Prefer a suitable connected GitHub tool;
   use `gh`, authenticated browser access or another supported interface when needed. Check only
   the capabilities and authentication required for the next hosted operation. Never print tokens.
5. Use explicit repository identifiers for hosted operations, especially when working outside a Git
   checkout. Public read-only information may not require authentication. Missing hosted access does
   not block local inspection or drafting; report exactly which verification remains unavailable.

GitHub issues can track a project whose local source uses another VCS. Git worktrees, Git branches
and GitHub PRs require the corresponding Git/hosted refs; do not run Git commands against an SVN
working copy or invent a migration. Use the supported equivalent or explain the specific gap.

Keep a short record of the relevant repository, revision/workspace, environment, checks and
contributor metadata. Reuse it for evidence and attribution rather than reconstructing facts later.
Use [the action policy](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/action-policy.md)
for all approval decisions.
