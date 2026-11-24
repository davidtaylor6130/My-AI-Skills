# David's versioning rules

Use `X.Y.Z`. Choose the highest applicable change level and confirm the exact candidate with David:

- **X, major:** a substantial change to how users work with the application or an overall workflow
  overhaul. Do not decide this solely from API compatibility or a commit prefix.
- **Y, minor:** new capabilities that improve the workflow without overhauling it, or a release
  grouping multiple bug fixes into a meaningful minor update.
- **Z, patch:** a targeted bug-fix update without a new feature or workflow overhaul.

Reset lower components when incrementing a higher component. Mixed changes use the highest agreed
level. Do not automatically choose a first release or infer a bump merely from the number of commits.

## Local builds and published versions

Development/test builds carry a stage and sequence, for example `2.4.1-alpha.3` or `2.4.1-beta.2`.
Use the repository's build mechanism to compose those identifiers. Choose alpha/beta and the next
number from the actual build state rather than inventing them.

GitHub publication defaults to the approved plain `X.Y.Z` version. Keep an existing `v` tag prefix
only when it is the agreed repository convention. Do not accidentally publish development suffixes
in version identifiers, tags, release titles or released package/asset versions. Distinguish the
local build identifier from the intended public release identifier throughout validation.

Publishing an alpha/beta version is an exception only when David specifically requests that exact
version. Confirm the exact exception at version selection, check the validated candidate again
immediately before the tag push, and obtain a separate final confirmation before release publication
with the actual tag, notes and assets visible. A tag-only exception does not approve a later release.
Silence or a general release request is not a response. Other remote actions, including draft release
creation and asset uploads, still follow [the action policy](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/action-policy.md).

## Version inventory and release target

Discover all product-owned version sources: build/package metadata, root lockfile entries, app
constants, runtime/UI version displays, installers, packaging, tests and current-version docs.
Search for both declarations and the previous product version; inspect each match rather than
blindly replacing dependency versions or historical release notes. Include generated build suffixes
and release assets in the inventory.

Recheck after edits. Explain remaining old-version matches and verify enough of the build/runtime
and packaging to establish which version will actually ship. Record unrun checks as gaps. A release
identifier that disagrees with its app/package version is not ready to publish.

If a version change is needed, use [the commit workflow](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/commits.md)
and, when a PR is needed, [Create PR](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/github-create-pr/SKILL.md).
Wait for the approved integration into the agreed release branch. Do not auto-merge or tag a local
unmerged bump. Confirm the exact target revision and its remote availability before preparing the
release; a later README/version edit changes that candidate and requires renewed validation.
