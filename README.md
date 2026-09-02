# AI Pipelines

Composable Agent Skills for getting useful work done without turning every task into a giant framework.

Current patch: **2.0.1** (`VERSION` is the release source of truth for shipped core skills).

| Skill | Role | Use it for |
| --- | --- | --- |
| [`task-execution`](skills/task-execution/SKILL.md) | HOST | Any actionable request: implement, fix, review, investigate, refactor, plan, or verify |
| [`design-pipeline`](skills/design-pipeline/SKILL.md) | DOMAIN | Material web UI/UX design, redesign, no-reference direction finding, and rendered visual verification |

## Harness model

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

The goal is **minimum justified permanent surface + evidence strong enough to support the claim**.

Harness v2 is designed to resist false completion, test-count optimization, unnecessary files/abstractions, dead residue, self-certified UI, production-code design exploration without a direction, provider stacking, and endless audit loops.

## Test and cleanup discipline

`task-execution` distinguishes:

- **TEMPORARY PROBE** — diagnostic/reproduction evidence; normally removed before completion;
- **DURABLE REGRESSION TEST** — protects a stable contract/invariant and has a clear counterfactual.

A bug fix does not automatically justify another permanent test. Prefer the strongest existing verifier and delete superseded implementation/tests/config after a replacement when nothing still consumes them.

See [`cleanup-and-tests.md`](skills/task-execution/references/cleanup-and-tests.md).

## Design without a reference

When material UI work has no strong reference and design authority is weak/incomplete:

```text
product truth
→ focused reference research when useful
→ 2–4 materially different Design DNAs
→ concrete scratch/mockup renders when practical
→ compare product fit / UX / craft / originality / implementation fit
→ select one direction
→ production build
→ real rendered capture
→ fresh bounded visual judge
```

See [`direction.md`](skills/design-pipeline/references/direction.md).

Use at most one primary craft approach per build pass. Another provider may be a fresh critic, not a co-builder.

## Install

Global/user install when you want reusable skills:

```bash
npx skills add Nishef1/ai-pipelines -s task-execution
npx skills add Nishef1/ai-pipelines -s design-pipeline
```

For projects where deterministic availability matters, keep repo-scoped copies under `.agents/skills/` and pin their upstream release/commit. Comoira is an example of this pattern.

## Bootstrap instructions

Ready-to-copy bootstrap files:

- [`instructions/codex-global.md`](instructions/codex-global.md)
- [`instructions/chatgpt-project.md`](instructions/chatgpt-project.md)

They intentionally route into HOST/DOMAIN skills instead of duplicating the full protocols.

## Executable evaluation

Static fixture/version checks:

```bash
python scripts/harness_eval.py check
```

Reviewed optional-provider drift:

```bash
python scripts/harness_eval.py provider-drift
```

Real baseline-vs-candidate outcome summaries:

```bash
python scripts/harness_eval.py outcomes path/to/real-runs.json
```

The evaluator does **not** call a model or fabricate outcome data. Representative task runs must come from the actual agent/harness environment being compared. See [`evals/harness-v2/README.md`](evals/harness-v2/README.md) and [`outcome-runs.example.json`](evals/harness-v2/outcome-runs.example.json).

Evaluate dimensions separately: task success, false completion, user corrections, unnecessary permanent files/tests, residue, regressions, UI pairwise preference/fidelity, latency/cost, and variance. Do not reduce them to one universal score.

## Principles

- **One HOST.** One finite current target.
- **Domain ownership.** Specialty skills define what good looks like; they do not replace the HOST.
- **Progressive disclosure.** Core skills stay cheap enough to activate; conditional detail lives in references.
- **Evidence over self-report.** Exit 0 or generated PASS text is not semantic proof by itself.
- **No provider stacking by default.**
- **No false progress.** Permanent complexity must trace to a real requirement.
- **Cleanup is completion work.**
- **Ablate harness rules.** If a rule adds cost/context without repeatable outcome lift, simplify or remove it.

## Layout

```text
ai-pipelines/
├── VERSION
├── AGENTS.md
├── README.md
├── instructions/
├── scripts/
│   └── harness_eval.py
├── evals/
│   ├── harness-v2/
│   ├── task-execution/
│   └── design-pipeline/
└── skills/
    ├── task-execution/
    └── design-pipeline/
```

This repository does not ship a project tracker, shadow roadmap, scheduler, or universal design doctrine.

## License

Repository scaffolding and `design-pipeline` are Apache-2.0. Individual skills may declare a more specific license; `task-execution` is MIT.
