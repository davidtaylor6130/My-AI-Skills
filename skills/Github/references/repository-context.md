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

## GitHub publication prerequisite

On a human-triggered PR invocation, verify that the intended GitHub repository and root/base
branch or required base revision exist and are accessible at the agreed destination. Do not
mistake the local checkout's existence for an available GitHub root. If access fails, distinguish
confirmed absence from an authentication/permission gap; do not claim a private repository is
missing solely from an unauthorised response.

If the repository or intended root/base is absent, keep the candidate and PR draft local in an
awaiting-root state. Report exactly what is missing and wait for a human to re-trigger after it
is on GitHub. Do not poll, schedule checks or resume automatically for this condition. Do not
create the repository, push the missing root/base, change visibility or retarget the PR as a
workaround. The separately approved task-head push can proceed only once this prerequisite is met.

When the human re-triggers, check the destination, base and candidate again before continuing.
This human-triggered wait is distinct from automatic resumption after a reviewer's usage reset.
