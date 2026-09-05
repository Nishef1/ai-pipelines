# Cleanup and Test Discipline

Use this reference when a task adds tests, helpers, fixtures, generated artifacts, or replaces an existing implementation.

## Why this exists

Agentic coding can create false progress through code/test growth: more helpers, mocks, fixtures, regression tests, wrappers, and compatibility paths can make the repository harder to change without proving more user value.

The goal is not minimal line count. The goal is **minimum justified permanent surface**.

## Temporary probe vs durable regression test

### TEMPORARY PROBE

A probe is diagnostic evidence for the current task. Examples:

- one-off reproduction script;
- temporary focused test used to isolate a bug;
- debug logging or instrumentation;
- scratch fixture/data;
- local browser script used only to inspect a state.

Keep it only while it helps diagnosis or verification. Remove it before completion unless it becomes a justified durable verifier.

### DURABLE REGRESSION TEST

Persist a test only when it protects a stable contract or historically meaningful failure mode.

Good durable targets include:

- user-visible workflow behavior;
- security/authorization boundaries;
- money/data invariants;
- protocol/API contracts;
- accepted accessibility behavior;
- a bug likely to recur because future changes can violate the same contract.

A durable test should answer:

```text
Contract protected:
Fault it catches:
Why existing verification is insufficient:
Counterfactual: if the fault returns, why does this test fail?
```

If those answers are weak, prefer a probe or an existing verifier.

## Usually weak regression tests

Do not persist a test merely to freeze:

- current CSS classes, DOM nesting, spacing/token values, or screenshot shape when the visual system is intentionally mutable;
- private helper call order or file topology;
- mocks that only restate the mocked implementation;
- compiler/type/lint guarantees already covered by the existing toolchain;
- generated artifacts whose source contract is already tested;
- incidental implementation details that a legitimate refactor should be free to change.

This does not ban unit tests. It rejects tests whose maintenance cost exceeds the stable contract they protect.

## Prefer stronger existing evidence

Before adding a new test:

1. inspect project verification commands and existing tests;
2. identify the exact claim to prove;
3. reuse the strongest existing verifier when it already exercises that claim;
4. add only the missing layer, preferably by extending an existing behavioral case.

A suite passing is useful only if it reaches the relevant scenario. Conversely, a one-off text, spacing, or configuration edit does not require a new test file when direct inspection and existing checks establish its outcome.

Before retaining a new test, check both directions: the protected fault should fail, while a legitimate behavior-preserving refactor should still pass. Use a small temporary fault injection when it materially clarifies this; do not build a mutation-testing framework. Keep valuable existing regression coverage unless its contract is obsolete or a stronger replacement demonstrably covers it. Test reduction is not a target either.

For boundary-heavy behavior, prefer an integration/behavioral check over many mock-heavy tests when practical.

## Red → green without permanent test inflation

A bug can use a temporary focused reproduction:

```text
reproduce failure
→ fix
→ rerun same reproduction successfully
→ decide whether the reproduction protects a durable contract
   ├─ yes: keep/refine as regression test
   └─ no: remove it
```

Do not assume every bug fix deserves a permanent new test file.

## Change-budget audit

After a coherent change, inspect permanent surface growth:

```text
files added:
files removed:
new dependencies:
new abstractions/helpers:
new durable tests/fixtures:
obsolete implementation removed:
net code growth:
```

These are diagnostics, not hard numeric gates.

Unexpected growth should trigger a question: **what stable requirement requires this permanent surface?**

If no good answer exists, simplify or delete it.

## Replacement/refactor cleanup

When a new path supersedes an old one, inspect direct consumers before completion and remove genuinely obsolete:

- modules/components;
- helpers/hooks;
- tests/fixtures;
- configuration and feature flags;
- imports/exports;
- docs/comments;
- generated or scratch artifacts.

Do not preserve dead compatibility paths before production unless a real consumer or accepted migration requirement needs them.

## Entropy sweeps

Do not turn every local task into a repository-wide cleanup.

Use:

- **task cleanup** — only changed/adjacent residue;
- **feature/milestone entropy sweep** — bounded stale paths, duplicate helpers, obsolete tests/config in that feature family;
- **release cleanup** — only release-relevant residue and accepted cleanliness criteria.

The existence of unrelated legacy debt is not a reason to keep the current task open.
