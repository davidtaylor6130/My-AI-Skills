---
name: typescript-best-practices
description: Apply TypeScript-specific modelling, boundary validation, narrowing, exhaustiveness, and testing guidance when reading, reviewing, or editing .ts or .tsx code. Use automatically for TypeScript implementation and review, especially state models, API boundaries, shared types, reducers, registries, and complex unions. Skip language-agnostic questions and clear local JavaScript without TypeScript concerns.
---

# TypeScript best practices

## Workflow

Inspect existing schemas, functions, types, compiler settings, and tests first. Use discriminated unions for real variants, `unknown` for external input, validation at boundaries, exhaustive switches, and `satisfies` where useful. Derive types from existing schemas/functions when practical. Avoid optional-field bags encoding impossible states. Brand primitives only when same-shaped values are realistically confused. Allow narrow documented casts after validation or unavoidable interop. Prefer real test primitives over excessive mocks and structured diagnostics in shipped code.

## Verification and output

Make no abstraction when local code is already clear. Run the repository's focused type, test, lint, and behavioural checks. Report changed modelling decisions and evidence; never claim runtime safety from type checking alone. Escalate to architect only for structurally non-trivial boundaries.
