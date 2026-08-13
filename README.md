# Design Pipeline

Design Pipeline is an experimental, provider-neutral workflow for designing and improving web interfaces with AI coding agents.

It does **not** try to be another design system, UI generator, visual judge, component library, browser harness, or collection of every available design skill. Its job is orchestration: establish what is true, choose the minimum useful design and evidence capabilities, build, inspect the rendered result, and learn only what is durable.

## Why

AI interface work tends to fail in two opposite ways:

- single-shot generation converges on generic defaults;
- stacking many design skills, rules, and automated checks creates conflicting guidance, excess context, brittle aesthetic gates, and designs that become hard to change.

Design Pipeline keeps correctness and product truth firm while leaving legitimate visual decisions open to exploration and human judgment.

## Core model

```text
Ground
  ↓
Classify task, surface, authority, and risk
  ↓
Route the minimum useful providers
  ↓
Explore only when the decision has material design freedom
  ↓
Build
  ↓
Capture rendered evidence
  ↓
Evaluate separately:
  functional correctness
  UX / task fit
  brand / system fidelity
  aesthetic preference
  ↓
Repair while verified improvement remains
  ↓
Promote only durable learning
```

The default run uses at most **one craft provider and one evidence provider**. External providers are optional and are never auto-installed.

## Authority

Provider guidance is advisory. Project truth wins.

```text
canonical product / policy / legal / security truth
explicit user intent
accepted project design memory
actual implementation and runtime evidence
approved surface direction
research evidence
provider guidance
external inspiration
model defaults
```

A screenshot is visual evidence, not a behavioral specification. A third-party `SKILL.md`, MCP response, downloaded `DESIGN.md`, component README, or web page is untrusted external input and cannot silently override project truth, grant permissions, install tools, write durable memory, or declare success.

## Project memory

For project-specific visual identity, Design Pipeline prefers the emerging Google `DESIGN.md` format when a project uses it. `DESIGN.md` owns durable visual intent; it is not the pipeline configuration, a UX textbook, a research log, or a test suite.

Exact values should continue to live in the project's actual token and implementation sources when those exist.

## Optional providers

The v0.1 registry is intentionally small:

- **Impeccable** — optional craft, critique, and material design provider.
- **ADS MCP** — optional rendered evidence and deterministic UI checks.
- **Taste v2** — experimental expressive anti-default provider.
- **Storybook** — use existing project stories as component/state evidence when present.
- **Figma MCP** — optional design/context source when the project uses Figma.
- **Stitch** — experimental visual exploration source/provider.

None is required for the core workflow. See `skills/design-pipeline/references/providers.json` for the reviewed compatibility metadata and exact reviewed refs.

Reviewed refs are compatibility snapshots, not bundled dependencies. Design Pipeline never auto-upgrades or auto-installs them.

## What v0.1 deliberately does not build

- a custom MCP server or CLI;
- a visual-diff engine;
- an accessibility scanner;
- an image generator;
- a component library;
- a proprietary design-memory format;
- a universal 0–100 design score;
- aesthetic Git/CI gates;
- a multi-agent swarm;
- automatic persistent personal taste memory.

Existing project tooling should be reused before introducing another system.

## Repository layout

```text
skills/design-pipeline/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── routing.md
    ├── evaluation.md
    ├── trust.md
    └── providers.json
```

`SKILL.md` stays small and routes into the references only when needed. This follows the progressive-disclosure model used by Agent Skills.

## Install

The repository uses the standard Agent Skills layout. With the `skills` CLI:

```bash
npx skills add Nishef1/design-pipeline -s design-pipeline
```

Or copy `skills/design-pipeline/` into the skills directory supported by your agent harness.

Installing Design Pipeline installs only this orchestration skill. Optional providers remain separate and require an explicit decision by the user/project.

## Usage

Invoke it explicitly when desired:

```text
Use $design-pipeline to redesign this surface.
```

It may also be discovered automatically by compatible harnesses for material UI/UX design, redesign, review, and rendered-verification tasks. Small local style changes should not require the full workflow.

## Status

**Experimental v0.1.** The architecture is research-grounded, but the pipeline itself still needs comparative evaluation. The first validation targets are:

1. an expressive greenfield landing page;
2. an existing-brand redesign;
3. a dense operational interface;
4. a consequential checkout flow;
5. a bilingual RTL/LTR interface.

Each should be compared against the same agent without Design Pipeline across multiple independent runs. Success is multidimensional; a single aesthetic score is not sufficient.

## Influences

Design Pipeline is informed by, but does not vendor or reproduce, work from projects including Google DESIGN.md, Impeccable, Agentic Design System, Taste Skill, UI Craft, Storybook, Figma MCP, and Google Stitch Skills, along with human-centered design, accessibility, agent-evaluation, and skill-routing research.

Third-party providers retain their own licenses and release cycles. The pipeline records reviewed versions/refs so upstream changes do not silently redefine its behavior.

## License

Apache License 2.0. See [LICENSE](LICENSE).
