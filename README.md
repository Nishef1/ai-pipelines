# AI Pipelines

Composable Agent Skills for getting useful work done with AI agents without turning every task into a giant framework.

The repository currently contains two layers:

| Skill | Role | Use it for |
| --- | --- | --- |
| [`task-execution`](skills/task-execution/SKILL.md) | Default execution harness | Any actionable request: plan, build, fix, review, investigate, refactor, write, verify, or ship work |
| [`design-pipeline`](skills/design-pipeline/SKILL.md) | UI/UX domain pipeline | Material web design, redesign, interface review, reference-grounded implementation, and rendered visual verification |

## Composition model

The skills are designed to compose rather than compete.

```text
User request
    ↓
task-execution
Goal / Target / Plan / Evidence / Stop
    ↓ when a specialty is material
Domain skill
    ↓
returns domain decisions + evidence
    ↓
task-execution
triage / next move / finish line
```

For a material UI task, `task-execution` is the host execution layer and `design-pipeline` is the design authority. The host owns the finite target, planning closure, global evidence state, prioritization, and stopping. The domain skill owns design classification, craft decisions, design-specific routing, and rendered visual evaluation.

Neither skill requires the other to work. There is no shared runtime, daemon, MCP server, or proprietary state format.

## Principles

- **Small core, progressive disclosure.** `SKILL.md` contains activation and the durable protocol; deeper material lives in `references/`.
- **One source of truth per concern.** Domain skills do not duplicate the host workloop, and the host does not pretend to be a domain expert.
- **Minimum useful process.** Simple work stays simple; rigor increases with ambiguity and consequence.
- **Evidence over self-report.** A tool existing, a command exiting `0`, or an agent saying `PASS` is not automatically proof.
- **Finite targets.** Findings are triaged against the current target; optional improvement does not keep the loop alive forever.
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
│       └── routing-cases.json
└── skills/
    ├── task-execution/
    │   ├── SKILL.md
    │   ├── agents/
    │   │   └── openai.yaml
    │   └── references/
    │       ├── break.md
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

## Evaluation

`evals/<skill>/routing-cases.json` contains activation/routing cases. These files are test corpora for skill selection and classification; they are not aesthetic CI gates and do not prove that a pipeline improves model quality.

Quality claims should be evaluated separately with repeated baseline-vs-skill runs on real tasks, using outcome-specific evidence rather than one global score.

## Adding another pipeline

A new skill belongs here only when it owns a distinct, reusable concern. Before adding one:

1. prove the concern is not already owned by an existing skill or reference;
2. define when it should and should not activate;
3. keep its domain rules independent of model/provider churn where practical;
4. add positive and negative routing cases;
5. make composition boundaries explicit;
6. avoid introducing a second source of truth for project state.

See [`AGENTS.md`](AGENTS.md) for repository-level maintenance rules.

## License

Repository scaffolding and `design-pipeline` are Apache-2.0. Individual skills may declare a different license in their own frontmatter; `task-execution` is MIT.