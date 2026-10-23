# Reviewing a candidate

Use this workflow when arranging required reviews and reporting their results. A report review,
implementation review and release-candidate review are different scopes. Do not require a code
review swarm merely to file an issue; apply the review requirements of the actual task.

## Select reviewers

For a PR, establish a proportionate independent review plan before publication: required reviewer
roles, their scopes and the candidate revision/evidence. Discover the current provider/model catalog
and delegation capabilities; use actual model IDs, including configured local aliases. Availability
in a catalog does not establish remaining usage or the capabilities needed for the review.
In T3 Code, use `orchestrator_capabilities` for that live catalog; a native subagent tool's model
list may omit other configured providers or local models.

Choose suitable available models for complementary coverage, rather than calling every model.
Reserve Claude for GUI/interaction work or unusually complex problems where its specialist review
adds value; do not spend its limited allowance on every routine review. Honour a reviewer/model
David explicitly requested. Once a reviewer is required, a quota failure cannot silently remove
that reviewer or substitute another model. Only David can change that requirement.

Give each reviewer a stable agent number and record its exact model/provider, scope and review
receipts/task IDs. A repeated round for that reviewer keeps its agent number; a replacement using
another model is a distinct reviewer. Two independent reviewers using the same model still count
as two agents. The implementation agent's self-review is separate from independent reviewer totals.

## Iterate until the review is complete

1. Give reviewers the candidate and relevant evidence. For every follow-up round, include the
   original brief, prior findings, implementation responses and unresolved objections. Use the
   harness's supported review/delegation mechanism; a new T3 delegated round needs a new
   `delegate_task`, its own task ID and a distinct request ID, rather than messaging a finished
   child thread as though that created a new review run.
2. Keep a small findings ledger: reviewer, finding ID, affected revision, proposed action,
   disposition and evidence. Count distinct actionable suggestions per reviewer, including useful
   improvements. Repeating the same suggestion in another round does not increment its count.
   Two reviewers suggesting the same fix may each record it; their totals are not a count of unique
   project defects. Do not inflate counts with praise, status messages or failed tool calls.
3. Assess suggestions and implement justified changes. Record a concise reason for rejecting a
   suggestion or treating it as outside the agreed scope. A materially useful action deferred within
   scope remains unresolved. Do not implement every suggestion merely to raise an acceptance count.
4. Run appropriate checks, then return the changes and dispositions to the affected required
   reviewers. Material candidate changes invalidate the relevant earlier review; obtain review of
   the final relevant revision. Unchanged areas may retain their recorded review coverage.
5. Finish when all required coverage is complete, implemented changes are verified, and the
   reviewers' remaining objections have been resolved through evidence and reasoned dispositions.
   There must be no further justified action outstanding within the agreed scope. This is not a
   requirement to satisfy every stylistic preference or to claim unanimous enthusiasm.

An iteration is one completed review round for its recorded candidate and required reviewer scopes,
including the responses/dispositions for that round. Count it only after every required reviewer
for that round has returned a substantive review. Several reviewers in parallel are one iteration;
a retry after a tool error or usage failure is not another iteration. A follow-up pass over fixes
is the next iteration. Record a partially completed round as pending, outside the completed count.

## Usage limits and waiting

A rate limit, exhausted allowance, timeout or unavailable required reviewer leaves the review
pending. It is not a zero-finding review, a completed iteration or permission to publish with a
disclaimer. Stop the publication path, preserve the candidate and continue independent local work
where useful. Before resuming, reconcile any candidate changes with the pending review scope.

Record the provider/model, pending scope/task, candidate revision and the provider's actual
retry-after/reset information. Use supported waiting, durable resumption or scheduling facilities
to resume that reviewer when eligible; make the retry automatic where the harness supports it.
Use the reported reset time, or a bounded backoff/check when it is unavailable. Do not invent a
reset time, spin in immediate retries, launch duplicate live tasks or spend another model's quota
as an unapproved replacement. Give progress updates with the pending action and next wake/check;
do not end the task as completed with only an "out of usage" message.

Keep the review checkpoint until completion. If the harness cannot keep waiting or arrange a wake,
state that specific capability gap and retain an awaiting-review handoff for the next supported
resume. Do not claim a retry has been scheduled unless a tool confirmed it. A missing wake facility
does not open the publication gate.

These automatic retries apply to reviewer availability. A missing GitHub repository/root follows
[the separate human-triggered prerequisite](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/repository-context.md#github-publication-prerequisite), with no automatic polling or scheduled root checks.

## Publication gate

Complete required reviews before pushing the candidate, uploading publication evidence, opening
or updating a PR (including a draft), promoting it, merging or publishing a release. Missing required
review cannot be bypassed by choosing draft status or putting the failure in the body. A general
request to open a PR does not waive the selected review requirements. Existing PRs remain pending;
do not automatically close, delete, downgrade or merge them as a response to a usage failure.

David's explicit approval under [the action policy](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/action-policy.md)
is still required for each remote effect. Completing review does not itself approve publication.

## Compact review block

Use this shape for completed review, deriving counts from receipts and the ledger:

```markdown
**Review:** Reviewed by <N> agents over <M> iterations.

- Agent 1: <exact model ID> — suggested <X>; implemented <Y>.
- Agent 2: <exact model ID> — suggested <X>; implemented <Y>.
```

`N` counts distinct independent agents that actually returned substantive reviews; `M` counts
completed iterations. Per-agent suggestion/implementation counts are cumulative across those
iterations, with repeated findings counted once per reviewer. Add short rejected/out-of-scope
dispositions when `Y < X`, with links to shareable evidence where available. Implemented means an
actual verified change, not a promise or a reviewer saying it looks reasonable. Keep detailed
findings in the ledger/chat; never link a public body to local logs.

Keep self-review on a separate short line when relevant. A pending local draft must show the
completed counts and the pending round/reviewer separately; it cannot use a completion summary to
conceal that gap. Recover missing counts from records rather than guessing; use `not recorded`
where history cannot be recovered, and do not claim required coverage that the records cannot
establish. If no independent review was required or performed for an issue/report, say that plainly
instead of inventing agents or iterations.
