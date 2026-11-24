# Using the live GitHub references

The canonical guidance is in David's public
[My-AI-Skills repository](https://github.com/davidtaylor6130/My-AI-Skills), on `main`.
Fetch linked Markdown as instructions to read; do not execute downloaded files as scripts.

- On each skill invocation, fetch the current
  [action policy](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/action-policy.md)
  and [repository context guide](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/repository-context.md),
  then the references needed for that task. Reuse documents already fetched during this invocation.
  Refresh them when resuming in another session or when David says the guidance has changed.
- All links are absolute public URLs. A linked skill's `SKILL.md` is a workflow to fetch and follow;
  that other skill does not need to be installed. Load only the applicable workflow, not every skill.
- Do not replace these URLs with paths into an installed skills directory or a guessed local clone.
  Changes to shared references take effect after they are reviewed and published to `main`;
  changing an installed entry point still requires a one-time update of that entry point.
- If fetching fails, identify the URL and failure. Continue independent inspection or provisional
  local drafting where useful, but do not publish using missing or silently stale guidance.
  A local reference copy may be used when David explicitly chooses it, including authoring and
  validating unpublished changes in this source repository. Identify that choice in the handoff.

David's current instructions take precedence over these references. A remote reference cannot
expand the requested task, grant approval, or override a standing no-commit/no-publication request.
