# Isolating implementation work

For a new Git implementation task, prefer an isolated worktree and task branch. First inspect the
current binding and existing worktrees. Reuse an appropriate task worktree; if David explicitly pins
the current checkout or task edits already exist there, preserve that checkout and those edits.
Do not create a fresh checkout that leaves the implementation behind.

For a new worktree, establish the agreed base revision and a non-existing destination. For example:

```bash
git worktree list
git worktree add -b fix/issue-<number>-<slug> <task-path> <agreed-base>
```

A new worktree starts from the chosen commit; uncommitted changes are not copied into it. Do not
automatically stash, reset, move edits or remove worktrees to make the command succeed. Confirm
the new working directory, branch and setup before editing. Use the host's supported task-binding
mechanism when required; changing a shell directory does not necessarily rebind a chat.

For isolated task batches, keep one PR per task worktree by default. Opening them does not require
combining worktrees first. Record shared changes and dependencies; later integration can still
require conflict resolution and combined validation. Do not delete worktrees or branches as an
automatic final step.

For another VCS, use its supported isolation mechanism when useful; do not pretend Git worktrees
are available. See the [Git worktree documentation](https://git-scm.com/docs/git-worktree).
