# AI Pipelines

Composable Agent Skills for getting useful work done without turning every task into a giant framework.

| Skill | Role | Use it for |
| --- | --- | --- |
| [`task-execution`](skills/task-execution/SKILL.md) | HOST | Any actionable request: implement, fix, review, investigate, refactor, plan, or verify |
| [`design-pipeline`](skills/design-pipeline/SKILL.md) | DOMAIN | Material web UI/UX design, redesign, review, no-reference direction finding, and rendered visual verification |

## Harness v2 model

```text
Product / project truth
        ↓
Work-control plane, when present
        ↓ selected current target
ONE HOST: task-execution
UNDERSTAND → PLAN → BUILD → JUDGE → CLEAN → BREAK when useful → STOP
        ↓ only when a specialty is material
ONE DOMAIN owner
        ↓
real evidence: runtime / browser / tests / DB / logs
```

The goal is not maximum process. It is **minimum justified permanent surface + evidence strong enough to support the claim**.

## What v2 is designed to prevent

- false completion from green build/lint/test output;
- test-count/coverage-count optimization;
- unnecessary files, wrappers, helpers, abstractions, and compatibility debris;
- temporary probes/debug artifacts being left in the repository;
- old implementation/tests/config surviving after a replacement when nothing consumes them;
- material UI being self-certified without rendered evidence;
- production CSS becoming the place where an agent discovers the visual direction;
- several design providers steering the same build pass at once;
- endless audit loops after the finite current target is already closed.

## Test and cleanup discipline

`task-execution` distinguishes:

- **TEMPORARY PROBE** — diagnostic/reproduction evidence for the current task; normally removed before completion;
- **DURABLE REGRESSION TEST** — protects a stable contract/invariant and has a clear counterfactual fault it catches.

A new test is not automatically valuable because a bug was fixed. Prefer the strongest existing verifier before adding another one. Avoid tests that merely freeze mutable DOM/CSS/theme/file topology, mocks, or implementation details a legitimate refactor should be free to change.

See [`cleanup-and-tests.md`](skills/task-execution/references/cleanup-and-tests.md).

## Design without a user-provided reference

When material UI work has no strong reference and design authority is weak/incomplete, `design-pipeline` does not immediately patch production CSS.

It first creates/selects a concrete design direction:

```text
product truth
→ focused reference research when useful
→ 2–4 materially different Design DNAs
→ concrete mockups/scratch renders when practical
→ compare product fit / UX / craft / originality / implementation fit
→ select one direction
→ production build
→ real rendered capture
→ fresh bounded visual judge
```

See [`direction.md`](skills/design-pipeline/references/direction.md).

Use at most one primary craft approach/provider per build pass. A different provider may serve as a fresh critic only when it adds a materially different evaluation capability; it should not co-build an averaged design doctrine.

## Completion is scope-aware

```text
TASK COMPLETE
SLICE COMPLETE
FEATURE COMPLETE
MILESTONE COMPLETE
RELEASE READY
```

`STOP` means the current target has no remaining Required work.

`SHIP` is reserved for an explicitly evaluated RELEASE target that is actually release-ready. Local success never implies product/release readiness.

## Install

```bash
npx skills add Nishef1/ai-pipelines -s task-execution
npx skills add Nishef1/ai-pipelines -s design-pipeline
```

Install only the skills the project actually needs.

## Bootstrap instructions

Ready-to-copy concise instruction files live under [`instructions/`](instructions/):

- [`codex-global.md`](instructions/codex-global.md) — global Codex bootstrap;
- [`chatgpt-project.md`](instructions/chatgpt-project.md) — ChatGPT Project operating instructions.

These files intentionally route work into the HOST/DOMAIN skills instead of duplicating their whole protocols.

## Evaluation

Routing fixtures answer **which capability should activate**, not whether output quality improved.

Current evals include:

- `evals/task-execution/routing-cases.json`;
- `evals/task-execution/completion-cases.json`;
- `evals/design-pipeline/routing-cases.json`;
- `evals/harness-v2/composition-cases.json`.

Harness quality claims should use repeated baseline-vs-candidate runs on representative real tasks. Evaluate dimensions separately, for example:

- behavioral/task success;
- false-completion rate;
- human corrections required;
- unnecessary permanent files/code/tests;
- dead/obsolete residue;
- functional/accessibility/responsive regressions;
- UI pairwise preference and direction/reference fidelity;
- tool calls, latency/cost, and variance.

Do not use one global quality score or an aesthetic CI gate.

## Principles

- **One HOST.** `task-execution` owns one finite current target.
- **Domain ownership.** Specialty skills define what good looks like; they do not replace the HOST.
- **Progressive disclosure.** Core `SKILL.md` stays small enough to activate; conditional detail belongs in `references/`.
- **Evidence over self-report.** Exit 0, a generated PASS string, or a closed issue is not semantic proof by itself.
- **No provider stacking by default.** More agents/skills/providers are not automatically better.
- **No false progress.** Permanent complexity must trace to a real requirement.
- **Cleanup is part of completion.** Exploration and superseded paths should not silently accumulate.
- **Ablate harness rules.** If a rule adds context/cost but repeated outcomes do not worsen when it is removed, simplify or delete it.

## Repository layout

```text
ai-pipelines/
├── AGENTS.md
├── README.md
├── instructions/
│   ├── chatgpt-project.md
│   └── codex-global.md
├── evals/
│   ├── harness-v2/
│   │   └── composition-cases.json
│   ├── task-execution/
│   └── design-pipeline/
└── skills/
    ├── task-execution/
    │   ├── SKILL.md
    │   ├── agents/openai.yaml
    │   └── references/
    └── design-pipeline/
        ├── SKILL.md
        ├── agents/openai.yaml
        └── references/
```

## External control systems

This repository does not ship its own project tracker, roadmap database, spec framework, or scheduler.

```text
Product truth     → what belongs / why
Work control      → accepted work / dependencies / assignment
Scheduler         → dispatch / retry / concurrency
Task Execution    → close the selected target
Domain skills     → specialty quality
Evidence          → prove actual behavior
```

Prefer thin adapters over embedding another provider's project-management model inside the HOST.

## Adding another pipeline

Add a new skill only when it owns a distinct reusable concern. Assign one primary role: `HOST`, `DOMAIN`, `EVIDENCE`, `ADAPTER`, or `AUDITOR`. Define positive/negative activation, composition boundaries, and representative eval cases. Do not create a second source of truth for project state, work priority, or scheduling.

See [`AGENTS.md`](AGENTS.md) for repository maintenance rules.

## License

Repository scaffolding and `design-pipeline` are Apache-2.0. Individual skills may declare a more specific license; `task-execution` is MIT.
