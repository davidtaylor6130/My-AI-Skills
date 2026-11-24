# Publishing text and visual evidence

Read [the action policy](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/action-policy.md)
before any remote write, including attachment upload. Prepare the complete text and files locally
first. These mechanics apply to issues, PRs, comments and release notes; they do not grant approval.
For a PR, first satisfy [the GitHub repository/root prerequisite](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/repository-context.md#github-publication-prerequisite); confirmed absence waits for a human
re-trigger, rather than automatic checks or publication of the missing root.
Complete the task's required reviews under [the review workflow](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/review-workflow.md) before publication effects.
Review blocked by usage limits stays pending; draft status does not bypass it.

## Markdown and exact text

Write the proposed UTF-8 Markdown to a unique temporary file with real newlines. Show David the
actual text and applicable metadata. Keep submission metadata and local handoff notes separate from
the body. Use a file-writing tool or a quoted heredoc rather than a
double-quoted shell string containing literal `\n`, backticks or command substitutions.

After approval, pass `--body-file <file>` for supported issue/PR/comment operations, or
`--notes-file <file>` for release notes. For example, with the confirmed repository and existing labels:

```bash
gh issue create --repo <owner/repo> --title '<approved-title>' --body-file <body-file> --label '<approved-label>'
```

Do not replace approved text with generated fill options or assume a command's dry-run mode is
side-effect-free. For a connector or browser, submit the same approved text through its supported
fields. Keep the prepared file until the published result has been checked.

## Draft and publication state

Show the intended state as part of the proposed artifact. For PRs, an approved draft maps to
`gh pr create --draft` or the connector's draft field; create a ready PR only when that state was
approved. Required review and validation must already be complete in either state. Promoting a
draft with `gh pr ready` or its equivalent is a separate remote action under
the action policy.

For releases, approval to create a draft does not approve publication. Use `--draft` unless David
has explicitly approved immediate publication of the exact candidate. With `gh`, creation must use
`--verify-tag` so a missing remote tag causes failure rather than automatic creation at the default
branch. That flag checks existence; the release workflow must also verify the tag's target revision.
After draft approval and that target check, for example:

```bash
gh release create <approved-tag> --repo <owner/repo> --verify-tag --draft --title '<approved-title>' --notes-file <notes-file>
```

Pass only the approved asset files. Release creation with assets involves separate draft, upload
and publication requests; without `--draft`, the CLI proceeds to publication. When preparing a
draft, verify its complete assets before a separately approved publication:

```bash
gh release edit <approved-tag> --repo <owner/repo> --verify-tag --draft=false
```

Recheck the remote tag target before publishing an existing draft. For a prerelease exception,
follow [the versioning confirmations](https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/skills/Github/references/versioning.md),
including the separate final publication confirmation. Connector/browser operations must enforce
the same approved state and existing-tag/target checks. See the
[release create manual](https://cli.github.com/manual/gh_release_create) and
[release edit manual](https://cli.github.com/manual/gh_release_edit).

## Images and recordings

A filesystem path or `file://` URL in posted Markdown is not an uploaded attachment. Select actual
product evidence, verify what each image shows and prepare meaningful alt text/state labels. Show
David the selected files and destination before uploading; attaching in a browser uploads the file
immediately, even if the issue/comment is not yet submitted.

### Required media preflight

Keep the local preview, upload input and published body distinct. Before approval, record the
selected files, their actual contents/checksums, alt text and intended body positions. A local
preview may display those local files, but label it as a preview awaiting upload. It is not a
GitHub-ready body. Do not treat opening that preview on this computer as remote image verification.

Before submission, inspect every Markdown image/link destination and HTML `src`/`href`, including
reference-style definitions. Each media reference must be either:

- An actual hosted URL that the intended GitHub reader can access; or
- A local image/video in a native CLI upload input, with that exact file also passed through the
  supported `--attach` operation described below.

Stop for any unmatched local reference. This includes `file://`, absolute home/volume/temp paths,
`~/...`, relative screenshot paths, sandbox/editor URLs and invented upload URLs. A relative path
is acceptable only when it deliberately identifies an existing tracked asset at the reviewed
GitHub revision and its rendered destination has been verified; never infer this from a local file.
Do not send local media references to a body-only connector or API: writing Markdown does not
upload files. Choose the attachment-capable CLI/browser route even when a body-only connector is
otherwise available.

### Native CLI when supported

Check the installed version and the exact command's help for `--attach`; do not assume the flag
exists. GitHub [introduced native attachments in `gh` 2.99.0](https://github.blog/changelog/2026-09-01-github-cli-media-in-issues-pull-requests-and-comments/). Confirm current host, token and repository
permission support using [GitHub's CLI attachment guide](https://docs.github.com/en/github-cli/github-cli/attaching-files-with-github-cli)
and the [command manual](https://cli.github.com/manual/gh_issue_create). Do not silently upgrade
software or request broader credentials as part of filing a report.

Use a dedicated upload-input Markdown file, for example `body-upload-input.md`, with the local
image in its intended position:

```markdown
![Observed error state](/absolute/path/repro.png)
```

After review completion and approval of the body, files and destination, include that exact path
as an attachment. For a PR, for example:

```bash
gh pr create --repo <owner/repo> --base <approved-base> --head <approved-head> --draft --title '<approved-title>' --body-file <upload-input-file> --attach /absolute/path/repro.png
```

Repeat `--attach` for multiple files. The CLI replaces matching local Markdown references with
uploaded URLs; an attachment not referenced in the body is appended. Prefer absolute paths so a
body file in a temporary directory cannot change relative-path resolution. Do not combine attachment
creation with `--web`, or use PR `--dry-run` as an upload preview.

This same-file pairing is required for every local image, not merely one example attachment. Use
the approved draft/ready state (`--draft` above is illustrative). Recheck the command's file/count
limits and supported media types. Attachments and reviewed text must remain the approved content;
substitution of the corresponding real upload URLs is the expected publication transformation.
Do not assume the CLI rewrites the local input file.

### Supported fallback

If a connector explicitly supports native attachment upload, use its documented operation. A tool
that merely writes the body or downloads images is not an uploader. Otherwise, use GitHub's
authenticated browser editor: after upload approval, attach the file, wait for upload completion and
retain the generated URL/Markdown. Submit the approved artifact or place those real URLs into the
body file for the approved API/CLI submission. Check the final rendered placement.

Wait until every selected upload has completed; an uploading placeholder is not a usable URL.
Save a final publication Markdown file containing the generated hosted URLs before a body-only
API/connector submission. Never substitute a guessed URL or the source's local path.

If authenticated upload is unavailable, keep the local evidence ready and report the upload gap.
Ask David to attach it or choose a supported route; do not publish broken local-path images. Do not
work around the gap by pushing an attachments branch, creating a release/gist, uploading to a third
party or using undocumented endpoints without a specifically reviewed plan and approval.

Uploaded public-repository files are publicly accessible. Check current file-type/size limits and
browser instructions in [GitHub's attachment documentation](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/attaching-files).
Do not claim an upload was tested merely because these instructions were read.

## Verification and partial failures

Verify the resulting URL, repository, title/body, labels, refs or tag as applicable. Inspect rendered
Markdown and each media asset as an intended reader; there must be no unresolved local paths or
incomplete upload placeholders. Preserve factual preparing/opening/publishing attribution.

Fetch the actual published body and save it locally as `published-body.md`, containing the hosted
URLs. Compare its text and image ordering against the approved body and file mapping; allow only
the expected attachment URL substitutions. Inspect the rendered images and open each uploaded
asset with the access expected of a reader (without authentication for a public repository).
Validate the final destinations, not just a filename or an HTTP success page. Do not report
completion while an asset is broken, missing, reordered incorrectly or still points to this
computer. If a tool cannot verify rendering/access, keep that verification pending.

A non-zero exit does not prove nothing was written. In particular, `gh` can create an issue/PR with
successful uploads and print its URL even when later attachments fail. Inspect that URL and remote
state before retrying. Identify exactly which assets or fields are missing and prepare an approved
repair of the existing artifact instead of creating a duplicate. Reuse approval only for the same
reviewed action and scope; material repairs need renewed review under the action policy.

For a failed release command, inspect the existing tag, draft/published state and uploaded assets
before retrying. Keep an incomplete draft unpublished and prepare the missing-asset repair for
approval. Do not publish, recreate the release or move its tag as an automatic recovery step.
