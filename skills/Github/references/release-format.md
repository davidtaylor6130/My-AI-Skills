# Release notes format

Read [the shared writing guide](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/writing-guide.md) for prose, evidence, review, factual model/app/harness
attribution and text publication. Preserve the project's version/tag scheme and release title,
such as `<version> — <short title>`; do not apply PR title syntax to versions or tags.

Release notes must cover:

1. **What the project is.** One sentence for someone landing here cold.
2. **Version numbering.** Briefly explain the scheme if it is non-standard.
3. **What's in this release.** Summarise meaningful changes in the selected release range, grouped
   by new features, fixes and removed/cleaned-up work as applicable. Do not claim unmerged or
   uncommitted work is included. Add actual product visuals only for graphical/interaction changes
   when useful; link existing verified PR evidence instead of repeating it where practical.
4. **Known issues.** Link relevant open GitHub issues. If the inventory could not be checked, state
   that limit rather than implying there are none. Distinguish reports from confirmed defects.
5. **Platform / environment.** Relevant OS, hardware and key dependencies, where recorded.
6. **Proof.** Record actual validation and results for the selected release revision, including
   version consistency, packaging/runtime checks when performed, and material failures or unrun
   checks. Linked PR checks establish only what they tested; do not relabel them as release checks.
7. **Review.** Use [the review workflow](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/review-workflow.md)'s compact agent/iteration summary and per-agent
   suggestion/implementation counts. Distinguish review of individual changes from review of this
   release candidate or its notes; complete required coverage before publication.
8. **Creation and publication.** Record implementation contributors/models and environments where
   known without attributing the whole release to the notes writer. Name the actual notes-preparing
   and publishing model, with each role's app/harness, on behalf of David Taylor. Combine matching
   roles; use `Prepared by` until publishing and mark unavailable history `not recorded`.

Keep the notes proportionate. Link detailed validation and provenance when available rather than
copying every PR body. Preserve an existing `CHANGELOG.md` format when adding the release entry;
do not paste GitHub-specific attribution blocks into it by default. Use [David's versioning rules](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/versioning.md)
for version selection and publication exceptions, and [the publishing workflow](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/publishing.md)
for exact notes, approval and verification. The release workflow owns target/tag preparation.
