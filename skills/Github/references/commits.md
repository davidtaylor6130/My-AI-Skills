# Preparing a commit

Use [the action policy](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/action-policy.md)
for approval. A request to fix, clean up or prepare a PR does not by itself approve a commit.

Inspect the complete proposed diff, select only task-owned files and show David the exact scope
and proposed commit message. Follow the repository's commit convention. Include actual validation
and remaining failures in the review material. Honour existing explicit approval for that same
commit; obtain approval for material changes. A standing instruction against commits still applies.

For Git, stage explicit paths, inspect the staged diff for accidental unrelated changes, and commit
only the approved content. Verify the resulting commit and remaining working-tree state. Do not
amend, reset, discard work or add co-author attribution without the relevant authorization/evidence.

Use the native VCS semantics: a local Git commit and an SVN commit have different effects. Any
commit operation that writes to a remote also needs the policy's remote approval, with the exact
destination and diff shown first.
