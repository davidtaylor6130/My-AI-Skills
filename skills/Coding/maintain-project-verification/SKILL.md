---
name: maintain-project-verification
description: Audit and update an existing project verification skill and feature map against current source and live behaviour. Use automatically when verification instructions, selectors, commands, environment assumptions, or coverage may have drifted, after substantial product changes, or when a verification workflow fails independently of the product. Skip repositories without an existing verification skill; create one instead.
---

# Maintain project verification

## Inputs and workflow

Locate the existing verification skill, current source, feature map, and prior evidence. Compare the map with source and exercise every mapped feature where practical. Correct only harness or documentation drift inside the verification skill; never change product code to make its description pass. Report product regressions separately. Reuse current tools and run single-agent unless independent surface checks are materially cheaper.

## Verification and output

If changed, run the corrected harness. Return `clean`, `changed`, or `blocked`, with tested features, evidence, product regressions, and untested gaps. Preserve evidence and keep external or destructive actions gated.
