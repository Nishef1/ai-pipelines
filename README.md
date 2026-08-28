# AI Pipelines

Composable Agent Skills for getting useful work done with AI agents without turning every task into a giant framework.

The repository currently contains two layers:

| Skill | Role | Use it for |
| --- | --- | --- |
| [`task-execution`](skills/task-execution/SKILL.md) | HOST execution harness | Any actionable request: plan, build, fix, review, investigate, refactor, write, or verify work |
| [`design-pipeline`](skills/design-pipeline/SKILL.md) | DOMAIN UI/UX pipeline | Material web design, redesign, interface review, reference-grounded implementation, and rendered visual verification |

## Composition model

The skills are designed to compose rather than compete.

```text
Product / strategy authority
        ↓
Work-control plane, when present
priority / dependencies / assignment
        ↓
task-execution
Target Level / Current Target / Plan / Evidence / Stop
        ↓ when a specialty is material
Domain skill
        ↓
returns domain decisions + evidence
        ↓
task-execution
current-target triage / completion
```

For a material UI task, `task-execution` is the host execution layer and `design-pipeline` is the design authority. The host owns the finite target, planning closure, current-target evidence, target-relative triage, and stopping. The domain skill owns design classification, craft decisions, design-specific routing, and rendered visual evaluation.

Project-wide strategy/priority, an authoritative issue graph, and external scheduling stay with the project/work-control system that owns them. `Ready` work is not automatically the highest-value product work.

Neither skill requires the other to work. There is no shared runtime, daemon, MCP server, proprietary project-state format, or built-in tracker.

## Completion is scope-aware

`task-execution` deliberately separates completion levels:

```text
TASK COMPLETE
SLICE COMPLETE
FEATURE COMPLETE
MILESTONE COMPLETE
RELEASE READY
```

`STOP` means the current execution target has no remaining Required work. It can happen at any level.

`SHIP` is reserved for an explicitly evaluated `RELEASE` target. Finishing a local task, slice, feature, or milestone must not be reported as product/release readiness.

## Principles

- **Small core, progressive disclosure.** `SKILL.md` contains activation and the durable protocol; deeper material lives in `references/`.
- **One source of truth per concern.** Domain skills do not duplicate the host workloop, and the host does not pretend to be a product tracker or domain expert.
- **One control plane per concern.** Avoid a shadow roadmap/state tracker and avoid two schedulers for the same work graph.
- **Minimum useful process.** Simple work stays simple; rigor increases with ambiguity and consequence.
- **Evidence over self-report.** A tool existing, a command exiting `0`, a closed ticket, or an agent saying `PASS` is not automatically proof.
- **Finite targets.** Findings are triaged against the current target; optional improvement does not keep the loop alive forever.
- **Scope-matched completion.** Local evidence cannot justify higher-level completion claims.
- **No provider stacking by default.** External skills and tools are optional capabilities, not automatic authority.
- **No silent scope growth.** Discovery can reveal work; it cannot silently promote every finding into a blocker.

## Repository layout

```text
ai-pipelines/
├── AGENTS.md
├── LICENSE
├── README.md
├── evals/
│   ├── design-pipeline/
│   │   └── routing-cases.json
│   └── task-execution/
│       ├── routing-cases.json
│       └── completion-cases.json
└── skills/
    ├── task-execution/
    │   ├── SKILL.md
    │   ├── agents/
    │   │   └── openai.yaml
    │   └── references/
    │       ├── break.md
    │       ├── control-plane.md
    │       ├── discover.md
    │       ├── evidence.md
    │       ├── judge.md
    │       └── project-compass.md
    └── design-pipeline/
        ├── SKILL.md
        ├── agents/
        │   └── openai.yaml
        └── references/
            ├── evaluation.md
            ├── providers.json
            ├── routing.md
            └── trust.md
```

## Install

Install only the skills you want:

```bash
npx skills add Nishef1/ai-pipelines -s task-execution
npx skills add Nishef1/ai-pipelines -s design-pipeline
```

For general project work, install `task-execution` first. Add `design-pipeline` when material UI/UX work is part of the project.

## Working with project control systems

This repository does not ship its own issue tracker, project-state database, spec framework, or multi-agent scheduler.

If a project already uses one, integrate through its real capabilities and keep ownership clear:

```text
Product truth     → what belongs / why
Work control      → accepted work / dependencies / assignment
Scheduler         → dispatch / retry / concurrency
Task Execution    → close the selected target
Domain skills     → specialty quality
Evidence          → prove actual behavior
```

Prefer thin provider adapters over embedding provider-specific project-management behavior in `task-execution`.

## Evaluation

`evals/<skill>/routing-cases.json` contains activation/routing cases. These files are test corpora for skill selection and classification; they are not aesthetic CI gates and do not prove that a pipeline improves model quality.

`evals/task-execution/completion-cases.json` captures scope/completion invariants such as “task complete does not mean ship” and external-control-plane boundaries. It is a semantic fixture, not a release-readiness engine.

Quality claims should be evaluated separately with repeated baseline-vs-skill runs on real tasks, using outcome-specific evidence rather than one global score.

## Adding another pipeline

A new skill belongs here only when it owns a distinct, reusable concern. Before adding one:

1. prove the concern is not already owned by an existing skill or reference;
2. assign a primary role: `HOST`, `DOMAIN`, `EVIDENCE`, `ADAPTER`, or `AUDITOR`;
3. define when it should and should not activate;
4. keep its rules independent of model/provider churn where practical;
5. add positive and negative routing/semantic cases where appropriate;
6. make composition boundaries explicit;
7. avoid introducing a second source of truth for project state, work priority, or scheduling.

See [`AGENTS.md`](AGENTS.md) for repository-level maintenance rules.

## License

Repository scaffolding and `design-pipeline` are Apache-2.0. Individual skills may declare a different license in their own frontmatter; `task-execution` is MIT.