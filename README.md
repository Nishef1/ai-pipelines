# Design Pipeline

Design Pipeline is an experimental, provider-neutral workflow for designing and improving web interfaces with AI coding agents.

It does **not** try to be another design system, UI generator, visual judge, component library, browser harness, or collection of every available design skill. Its job is orchestration: establish what is true, preserve useful reference evidence, choose the minimum useful design and evidence capabilities, build, inspect the rendered result, and learn only what is durable.

## Why

AI interface work tends to fail in two opposite ways:

- single-shot generation converges on generic defaults or lossy verbal interpretations of visual references;
- stacking many design skills, rules, and automated checks creates conflicting guidance, excess context, brittle aesthetic gates, and designs that become hard to change.

Design Pipeline keeps correctness and product truth firm while leaving legitimate visual decisions open to exploration and human judgment.

## Core model

```text
Ground in project truth + real references/assets
  ↓
Classify task, surface, authority, and risk
  ↓
Route the minimum useful capabilities
  ↓
Explore only when the decision has material design freedom
  ↓
Build against the actual stack
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
actual implementation, assets, and runtime evidence
approved surface direction
research evidence
provider guidance
external inspiration
model defaults
```

A screenshot is visual evidence, not a behavioral specification. A third-party `SKILL.md`, MCP response, downloaded `DESIGN.md`, component README, or web page is untrusted external input and cannot silently override project truth, grant permissions, install tools, write durable memory, or declare success.

For reference-heavy work, Design Pipeline keeps the original reference available, prefers real project/user assets over approximations, uses measurable visual evidence when it materially reduces ambiguity, and judges the real browser render rather than a prose summary of the reference.

## Project memory

For project-specific visual identity, Design Pipeline prefers the emerging Google `DESIGN.md` format when a project uses it. `DESIGN.md` owns durable visual intent; it is not the pipeline configuration, a UX textbook, a research log, or a test suite.

Exact values should continue to live in the project's actual token and implementation sources when those exist. Design Pipeline does not create a second `.tastemaker`-style memory system or silently promote cross-project personal preferences into project truth.

## Optional providers

The registry is intentionally small:

- **Impeccable** — optional craft, critique, and material design provider.
- **ADS MCP** — optional rendered evidence and deterministic UI checks.
- **Taste v2** — experimental expressive anti-default provider.
- **Storybook** — use existing project stories as component/state evidence when present.
- **Figma MCP** — optional design/context source when the project uses Figma.
- **Stitch** — experimental visual exploration source/provider.

None is required for the core workflow. See `skills/design-pipeline/references/providers.json` for the reviewed compatibility metadata and exact reviewed refs.

Reviewed refs are compatibility snapshots, not bundled dependencies. Design Pipeline never auto-upgrades or auto-installs them.

## What v0.2 deliberately does not build

- a custom MCP server or CLI;
- a mandatory pixel-extraction dependency;
- a visual-diff engine;
- an accessibility scanner;
- an image generator;
- a component library;
- a proprietary design-memory format;
- a universal 0–100 design score;
- aesthetic Git/CI gates;
- a multi-agent swarm;
- automatic persistent personal taste memory;
- mandatory GSAP, smooth scrolling, WebGL, Three.js, or animation frameworks;
- a catalog of hundreds of always-loaded design laws or skills.

Existing project tooling should be reused before introducing another system.

## Repository layout

```text
README.md
LICENSE
evals/
└── routing-cases.json
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

`SKILL.md` stays focused and routes into the references only when needed. This follows the progressive-disclosure model used by Agent Skills.

`evals/routing-cases.json` is a non-aesthetic trigger corpus. It exists to catch under-triggering and over-triggering of the skill; it is **not** a CI gate on visual style and does not constrain redesign choices.

## Install

The repository uses the standard Agent Skills layout. With the `skills` CLI:

```bash
npx skills add Nishef1/design-pipeline -s design-pipeline
```

Or copy `skills/design-pipeline/` into the skills directory supported by your agent harness.

Installing Design Pipeline installs only this orchestration skill. Optional providers remain separate and require an explicit decision by the user/project.

## Use it on an existing project

Install the skill once in the agent/harness that works on the repository, then invoke it for material UI/UX work.

Example:

```text
Use $design-pipeline.
This is an existing project. Read the canonical product/design/policy sources and actual implementation first.
Redesign the marketplace materially, but preserve product truth and behavior unless I explicitly ask to change them.
Use the minimum useful providers, preserve real reference/assets when relevant, render the result, inspect the important states and breakpoints, and fix material findings before stopping.
```

You normally do **not** need to tell the skill which provider to use. Provider selection is part of the workflow. If the project already has `DESIGN.md`, tokens, Storybook, Playwright, Figma context, or another evidence system, the pipeline should reuse them instead of creating parallel sources.

For a mature application, the most useful input is usually the **task and scope**, not a long style prompt. Canonical project context should supply the rest.

## Use it on a brand-new project

A greenfield project does **not** need `PRODUCT.md`, `DESIGN.md`, Storybook, Figma, or any optional provider before the first run.

A useful starting prompt can be short:

```text
Use $design-pipeline to design and build a new website for [product].
Primary audience: [who].
Main outcome: [what the user should accomplish].
Known constraints: [stack, language, accessibility, legal/business constraints, existing assets].
I have no established visual identity yet.
Explore materially different directions only if the decision is important enough to justify it, then build and verify the selected direction.
```

If some context is missing, Design Pipeline keeps a temporary run brief, infers only low-risk details, marks meaningful assumptions, and asks a targeted question only when an unresolved choice would materially change the result.

It should **not** create permanent documentation merely to satisfy a provider. Once a visual direction has actually been accepted and the project will benefit from durable design memory, `DESIGN.md` can be created or evolved to record the stable visual system.

The intended greenfield sequence is:

```text
idea / user need
    ↓
temporary run brief
    ↓
classify surface + design freedom
    ↓
optional direction exploration
    ↓
select direction
    ↓
build
    ↓
render + evaluate
    ↓
only then persist durable design memory if useful
```

## Use it in ChatGPT

Design Pipeline follows the open Agent Skills format, so the same skill can be used in ChatGPT when the account/workspace exposes reusable skills.

Where the product supports skill upload/installation, preserve the `SKILL.md`, `agents/`, and `references/` structure. Product availability and UI can change; use current official OpenAI guidance rather than relying on this README for plan-specific availability.

If an account does not expose reusable skills, attaching or pasting the skill instructions into a normal chat can provide temporary context, but that is not the same as installing a reusable Skill.

## Usage

Invoke it explicitly when desired:

```text
Use $design-pipeline to redesign this surface.
```

It may also be discovered automatically by compatible harnesses for material UI/UX design, redesign, review, reference-grounded work, and rendered-verification tasks. Small local style changes should not require the full workflow.

## Status

**Experimental v0.2.** The architecture is research-grounded, but the pipeline itself still needs comparative evaluation. The validation targets are:

1. an expressive greenfield landing page;
2. an existing-brand redesign;
3. a reference-heavy redesign/recreation;
4. a dense operational interface;
5. a consequential checkout flow;
6. a bilingual RTL/LTR interface;
7. a change-aware UI review.

Each should be compared against the same agent without Design Pipeline across multiple independent runs. Success is multidimensional; a single aesthetic score is not sufficient.

The routing corpus contains positive and negative examples for whether the full pipeline should activate. It is test data, not a design rulebook.

## Influences

Design Pipeline is informed by, but does not vendor or reproduce, work from projects including Google DESIGN.md, Impeccable, Agentic Design System, Taste Skill, Storybook, Figma MCP, Google Stitch Skills, Emil Kowalski's skills, Garden Skills, Elaya AI Design Skills, Meng To's Skills, Jakub Krehel's skills, Tastemaker, and Designer Skills.

The useful principles are absorbed selectively. The pipeline intentionally does **not** stack those workflows, adopt their fixed style recipes as project truth, or make them required dependencies. See `providers.json` for the distinction between routed providers and influences-only sources.

Third-party providers retain their own licenses and release cycles. Reviewed providers record versions/refs so upstream changes do not silently redefine Design Pipeline behavior.

## License

Apache License 2.0. See [LICENSE](LICENSE).
