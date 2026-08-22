---
name: analyse-logs
description: Analyse command, build, test, CI, application, and SVN/Subversion logs; separate root causes from cascades; distinguish expected warnings or errors from unexpected failures; and issue an evidence-based approval verdict. Use when a user asks to inspect logs, explain warnings or errors, validate an SVN operation, decide whether noisy output is safe, or approve a run.
---

# Analyse Logs

Analyse supplied output without changing files or rerunning destructive commands. Ask for missing evidence only when it prevents a reliable verdict.

## Workflow

1. Capture the command, exit code, timestamp, environment, and whether the log is complete. Mark absent items as unknown.
2. Read the full log before classifying individual lines. Preserve exact file paths, line numbers, error codes, test names, and revision numbers.
3. Group repeated messages and cascades under the earliest actionable cause. Do not count one failure many times.
4. Classify each group as unexpected error, unexpected warning, expected noise, or informational.
5. Issue one verdict using the rules below.

## Expected Noise

Treat a warning or error as expected only when at least one of these supports it:

- The user supplied an explicit allowlist or baseline.
- Project configuration or tests document it.
- Authoritative tool documentation says it is normal for this exact operation.
- A preceding, successful control run contains the same stable message.

Never call a message expected merely because it repeats, looks familiar, or the command continued. State the supporting evidence and residual risk. Keep unmatched warnings and errors unexpected.

For SVN output, distinguish routine notifications from conflicts and failures. Treat `C`, tree conflicts, obstructed paths, authentication or authorization failures, repository UUID mismatches, lock failures, out-of-date commits, checksum errors, and non-zero exits as blocking unless evidence proves otherwise. Record revision, URL, working-copy root, externals, and mixed-revision state when present.

## Verdict Rules

- `APPROVED`: The run completed successfully, evidence is complete, and no unexpected warnings or errors remain.
- `APPROVED WITH EXPECTED NOISE`: The run completed successfully and every warning or error is explicitly supported as expected.
- `NOT APPROVED`: Any unexpected error, failed test, conflict, unsafe partial operation, integrity risk, or unexplained non-zero exit remains.
- `INCONCLUSIVE`: The exit status, completion marker, relevant log section, or other decisive evidence is missing.

Do not convert `INCONCLUSIVE` to approval. Do not approve solely from a final “success” line when earlier failures were not reconciled.

## Output

Use this exact structure:

```markdown
## Verdict

Approval: APPROVED | APPROVED WITH EXPECTED NOISE | NOT APPROVED | INCONCLUSIVE
Reason: <one sentence>
Evidence: <exit code, completion marker, revision/test summary, or missing evidence>

## Unexpected errors

- <root cause and exact evidence, or “None”>

## Unexpected warnings

- <warning, impact, and exact evidence, or “None”>

## Expected warnings and errors

| Message/code | Why expected | Evidence | Residual risk |
|---|---|---|---|
| ... | ... | ... | ... |

## Notes

- <cascades, SVN state, omissions, and assumptions>

## Next action

<smallest action that resolves the blocker, or “None”>
```
