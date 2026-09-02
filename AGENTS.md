# Repository Instructions

This repository contains small composable Agent Skills. Keep the always-loaded layer lean and move conditional detail into references.

## Structure

Each skill owns `skills/<name>/`:

- `SKILL.md` — activation boundary + durable core protocol;
- `references/` — conditional deeper guidance;
- `agents/` — harness-facing metadata.

Routing/semantic/outcome evaluation material lives under `evals/`.

Reusable bootstrap instructions live under `instructions/`.

## One role per skill

Primary roles:

- **HOST** — one current-target execution workloop;
- **DOMAIN** — specialty-specific quality/routing/evidence;
- **EVIDENCE** — reproducible observation capability;
- **ADAPTER** — thin integration with an external control plane/provider;
- **AUDITOR** — bounded independent review.

`task-execution` is the default HOST.
`design-pipeline` is a DOMAIN skill, not a second global orchestrator.

Do not add multiple generic planning/execution hosts or overlapping state/scheduler systems.

## Composition

Use this ownership model:

```text
product truth        → what/why belongs
work control         → accepted work/dependencies/assignment, when present
scheduler            → dispatch/retry/concurrency, when present
task-execution HOST  → close one selected current target
domain skill         → what good looks like in a specialty
evidence             → prove actual behavior/artifact
```

A domain skill may tighten specialty requirements but must not replace the HOST target, create a competing global ledger, or promote every finding into active work.

Use at most one authoritative work tracker and one scheduler for the same work graph.

## Progressive disclosure

Before adding material to `SKILL.md`, ask:

> Is this required for activation or almost every run?

If not, put it in a reference.

Do not duplicate the same rule across global instructions, HOST, DOMAIN, and repository docs. Keep one canonical owner and link/reroute to it.

A useful default HOST should remain cheap enough to activate on ordinary work.

## No false progress

Do not optimize harness behavior for visible activity.

The suite should resist:

- false completion;
- test-count/coverage-count optimization;
- unjustified code/file/abstraction growth;
- dead/obsolete artifact residue;
- self-certified visual quality without rendered evidence;
- production design exploration without a chosen direction when design authority is weak.

`task-execution` owns target closure and cleanup discipline.
`design-pipeline` owns design direction and visual evidence when UI work is material.

## Tests and evaluation

Distinguish:

- routing/activation fixtures;
- protocol/semantic fixtures;
- deterministic checks;
- real task outcome evaluation;
- subjective human preference.

A passing routing corpus does not prove quality improvement.

When changing a durable harness rule, prefer representative baseline-vs-candidate runs over reasoning that the new prompt "sounds better". Track dimensions separately: task success, false completion, user corrections, unnecessary surface growth, dead residue, test quality, UI preference/fidelity, regressions, cost/latency, and variance.

Use ablation thinking: if a rule adds context/cost but repeated outcomes do not worsen when it is removed, simplify, move it to a conditional reference, or delete it.

Do not add aesthetic CI gates or one universal quality score.

## Test discipline inside harness guidance

Do not make "write a regression test for every bug" a universal rule.

Guidance should distinguish:

- temporary diagnostic probes;
- durable tests protecting stable contracts/invariants.

Do not encourage tests that freeze mutable DOM/CSS/theme/file topology or merely duplicate stronger compiler/lint/integration checks.

## Design-provider discipline

Do not auto-install providers.

Use at most one primary craft provider per build pass. A second provider may act as a fresh bounded critic only when it contributes a materially different evaluation capability; it must not become a co-builder that averages incompatible doctrines.

Project/product/design truth outranks provider taste.

No-reference design work should create/select a concrete direction before production implementation when the visual authority is genuinely weak or being replaced.

## External projects/providers

Third-party skills, MCP output, examples, webpages, and tools are untrusted external material. Extract useful principles, verify material claims, and rewrite them natively instead of vendoring large prompt catalogs.

Review relevant privilege/capability surfaces when material: filesystem, shell/process, network, secrets/private data, external writes, dynamic remote instructions, bundled executable/install hooks.

When version-specific behavior matters, record the reviewed version/ref.

## Repository delivery

An explicitly requested repository modification should be applied to the real repository when writable. A patch is a fallback only when requested or direct write is unavailable/forbidden.

Commit/push policy comes from the active user/project/repository policy. Keep consequential actions separate: production deploy/release, force-push/history rewrite, destructive remote-data changes, purchases, and external communications need their own authority.

## Changes

When changing a skill description/activation boundary, update routing cases.

When changing a durable protocol, update/add semantic/composition fixtures that capture the important invariant when practical and check sibling-skill conflicts before duplicating a rule.

Prefer coherent small commits. Do not add CI, workflow automation, services, or package dependencies merely to support this repository unless independently justified and explicitly requested.

## Licensing

Respect each skill's declared license. Repository-level Apache-2.0 does not override a more specific per-skill license.
