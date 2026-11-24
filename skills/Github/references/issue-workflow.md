# Preparing and filing issues

Use [repository context](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/repository-context.md),
[the issue format](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/issue-format.md)
and [the action policy](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/action-policy.md).
Keep one issue per independently actionable problem or request.

## Establish evidence and duplicates

Read the report, relevant context and repository templates. Distinguish observed behaviour, user
reports and hypotheses. Gather useful reproduction or desired-outcome details without inventing
missing facts. A proposed issue can accurately state that reproduction is pending.

Search both open and closed issues with specific terms and read likely matches, including relevant
comments and linked work. Use focused queries and paginate when the result could be incomplete;
a title match alone does not prove identical scope. For example:

```bash
gh issue list --repo <owner/repo> --state all --search '<specific-search-terms>' --json number,title,state,url
```

Report whether the item is new, already tracked, a recurrence or needs more information. Recommend
linking, a comment, reopening or a separate regression report where supported. Do not perform those
tracker changes merely because a duplicate was found.

## Repository-owned labels

Read the destination repository's actual labels, their descriptions and relevant issue/template
conventions. Inspect the relevant labels even if the default list is truncated. Use at least one
fitting label for each new issue, unless David explicitly chooses otherwise.

Do not import a label vocabulary from another product or generate labels from a title's words.
Apply only existing labels whose meaning fits the report. If none fit, show the gap and ask David
to choose an existing label or review a specific new label name/description/colour. Creating or
changing a label is its own remote mutation; never silently create a supposedly standard label.
The title's `bug`/`feature` type is separate from the repository's exact label names.

GitHub labels belong to the repository in which they were created; see
[Managing labels](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels).

## Prepare, review and file

Show concrete titles, complete bodies, proposed labels, duplicate decisions and any attachments.
For a batch, present a bounded item list; David can approve that exact batch, select items or revise
them. Do not use a generic "file everything found" default as approval.

Use [the shared publishing mechanics](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/publishing.md)
for approval, Markdown files, media upload, verification and failure recovery. With `gh`, use
`--label` at creation and `--add-label` for an issue edit; verify supported flags before use.
Return the actual created/updated URLs and a concise list of skipped or unresolved items. No commit
or implementation is needed to file an issue. If fixing the report is requested too, follow the
[Fix Issue workflow](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/github-fix-issue/SKILL.md)
as that separate authorised scope.
