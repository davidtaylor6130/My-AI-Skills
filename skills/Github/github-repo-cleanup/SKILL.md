---
name: github-repo-cleanup
description: Audit and improve repository documentation, metadata, tracked files, ignore rules, licensing and issue hygiene using the project's native VCS and shared GitHub workflows. Use for repository cleanup or portfolio readiness. Exclude product-code refactors and release publication itself.
---

# GitHub Repository Cleanup

Fetch [the live-reference entry guide](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/using-references.md), then follow its shared context
and action policy. Use [the shared writing guide](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/writing-guide.md) for clear prose and factual
evidence. Audit the requested repository without assuming its language, platform or VCS.

## Review the relevant areas

Scale the audit to the project and requested cleanup. Inspect:

- **Hosted metadata:** description, topics, visibility and links. Propose accurate, project-specific
  values. Do not assume public visibility or change it merely for portfolio presentation.
- **Tracked files and ignore rules:** identify generated output, dependencies, editor artifacts,
  accidental data and sensitive material using the actual stack. Explain each proposed removal or
  untracking change; do not delete source/runtime assets or blanket-ignore all data/config files.
- **README and docs:** verify purpose, actual capabilities, setup, supported environment, architecture
  where useful, status and links against the repository. Keep its voice and established structure.
  Use verified product visuals only when graphical/interaction behaviour benefits from them; do not
  demand a logo, screenshots or a fixed number of bullets from every project.
- **Licence:** identify what exists. If absent or unclear, ask David to choose/confirm the licence
  and owner details before adding or replacing its text. Preserve the actual legal text.
- **Issue/release/branch hygiene:** inspect only the hosted records or history needed for specific
  findings. Recommend supported actions; do not infer that an old branch is disposable or an issue
  is fixed merely from a commit message.

Prepare reversible local cleanup within scope and validate the changed documentation/configuration
against the actual project. Preserve unrelated edits and do not automatically stage every finding.

## Reuse the shared workflows

- New reports or report changes use [the issue workflow](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/issue-workflow.md), including its labels
  and duplicate checks; a broad backlog/discovery review uses [Issue Sweep](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/github-issue-sweep/SKILL.md).
- Commit preparation uses [the commit workflow](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/commits.md).
- A cleanup PR uses [Create PR](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/github-create-pr/SKILL.md), including its shared format.
- Version/tag/release work uses [Version Tag Release](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/github-version-tag-release/SKILL.md),
  including David's versioning rules and [the release-notes format](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/release-format.md).
- Any remote metadata, tracker, branch or publication change uses the action policy and
  [publishing workflow](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/publishing.md). A cleanup request alone does not authorise them.

Report concrete local changes and validation, ready-to-review remote proposals, unresolved owner
choices and skipped items with reasons. Do not claim unused audits, independent review or publishing.
