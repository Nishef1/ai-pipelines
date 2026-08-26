# Routing

Use this reference when the task is large enough to benefit from an explicit design workflow.

The goal is not to invoke every available design capability. The goal is to select the **smallest set of capabilities that materially improves this task**.

## 1. First decide whether the full pipeline is warranted

Skip provider routing and use the host agent directly for work such as:

- a local spacing/color adjustment with an already-known target;
- a simple accessibility defect with an obvious repair;
- a one-component bug whose visual system is already established;
- a backend-only change;
- a mechanical rename/refactor with no design decision.

Use the pipeline when the task involves material visual direction, UX structure, a new surface, a redesign, a consequential workflow, a reference-driven visual target, a material UI change review, or a rendered quality review.

## 2. Determine the design freedom

### Preserve

Use when the existing identity is authoritative and the task is refinement/repair.

- do not replace typography, palette, shape language, or composition vocabulary without scope;
- do not run a visual-world tournament;
- use the existing implementation and design memory as the primary visual authority.

### Extend

Use for a new surface inside an established design world.

- keep the project identity fixed;
- explore information architecture or page composition only when several materially different structures are plausible;
- avoid turning one new page into a brand redesign.

### Replace

Use only when the user explicitly requests a redesign/new visual identity, or canonical project direction says the incumbent identity is no longer authoritative.

- preserve product truth, content truth, behavior, security, legal constraints, and native/expected interaction semantics;
- incumbent visuals become evidence/anti-reference, not a mandatory style to preserve;
- direction selection may precede implementation.

### Create

Use when no visual authority exists.

- derive direction from product, audience, context, content, and references;
- do not treat provider defaults as project truth.

## 3. Surface-aware routing

### Persuade

Examples: landing, campaign, marketing pricing, public launch page.

Priorities:

1. product/audience truth;
2. one dominant offer/outcome and primary action;
3. message and proof hierarchy, including source-message consistency when traffic context is known;
4. credible proof near the claims it supports and honest objection/risk handling;
5. memorable visual direction;
6. responsive/readable execution;
7. conversion clarity without dark patterns.

Optional craft routing:

- **Impeccable**: preferred supported provider for substantial direction/craft when compatible with project context.
- **Taste v2**: experimental; use only when anti-default creative pressure would materially help and the surface is within Taste's stated scope.
- **Stitch**: experimental; useful for visual exploration/variants when already available.

Do not automatically stack these providers. Do not import a landing-page provider's fixed fonts, spacing, radii, section templates, or motion recipes as project truth.

### Operate

Examples: dashboards, settings, admin, tools, checkout, seller/buyer workflows.

Priorities:

1. task completion and state truth;
2. information hierarchy and scanability;
3. familiar interaction semantics;
4. recovery/error prevention;
5. accessibility, localization, and responsive resilience;
6. restrained brand expression appropriate to consequence and frequency.

Optional craft routing:

- **Impeccable Operate-style guidance** may help for material work.
- **Taste v2 should normally remain off** because its documented scope excludes dashboards, data tables, and multi-step product UI.

For consequential surfaces, novelty and expressive motion never outrank correctness, state clarity, authorization/payment truth, recovery, or predictable interaction semantics.

### Read

Examples: docs, help, policy, long-form guides.

Focus on information architecture, typography, measure, navigation, semantic structure, localization, and reading comfort. Creative providers are usually unnecessary unless the reading experience itself is the design project.

### Experience

Examples: portfolios, galleries, showcases.

The artifact/content may lead the composition. Impeccable or experimental Taste can be useful when the task benefits from distinctive visual direction. Rich motion, spatial effects, or experimental media are valid only when they support the visual thesis and retain accessible/static fallbacks.

## 4. Reference intelligence

When a visual reference materially defines the task:

1. inspect project code, tokens, components, and assets first;
2. preserve authoritative project/user assets instead of approximating them;
3. use deterministic measurement of reference pixels when an existing/available tool can materially reduce ambiguity — palette relationships, contrast, geometry, density, crops — but do not add a new dependency just to satisfy this pipeline;
4. combine measurement with visual interpretation; neither replaces the other;
5. compare the actual browser render to the intended reference at comparable states/viewports;
6. if the reference belongs to another brand, extract reusable principles rather than copying protected identity, distinctive assets, or copy.

A text summary such as "minimal Linear-like UI" is not a lossless representation of a reference and should not replace the reference when the real evidence remains available.

## 5. Motion routing

Motion usually does not need a separate provider.

Use the project's existing CSS/motion primitives when they can express the intended behavior. Before adding motion, determine:

- whether movement materially helps comprehension, feedback, spatial continuity, state indication, explanation, or justified delight;
- how frequently the interaction is encountered;
- whether it is interruptible or gesture-driven;
- whether it is consequential or latency-sensitive;
- how reduced-motion, touch/coarse pointers, cleanup, and static/final states behave.

A complex expressive motion provider is justified mainly for Persuade/Experience work where motion is part of the art direction. Do not introduce GSAP, a smooth-scroll engine, WebGL, or Three.js as a generic quality upgrade.

## 6. Craft-provider selection

Default maximum: **one craft provider in a pass**.

Choose a provider only if all are true:

- its documented scope includes the task;
- it adds a capability the native agent/project context does not already provide;
- its assumptions do not conflict with canonical project truth;
- using it does not require silently introducing a second source of truth;
- required permissions/dependencies are acceptable;
- its version/ref is reviewed in `providers.json` or the current version has been re-reviewed.

If no provider satisfies these conditions, use native design reasoning.

Do not route a repository merely because it contains good principles. Several design-skill repositories are recorded as **influences, not providers**, because their useful ideas have been absorbed while their full workflow would duplicate or conflict with Design Pipeline.

## 7. Evidence-provider selection

Prefer existing project evidence before adding tooling.

Order of preference is contextual, not absolute:

1. **Existing Storybook/stories** when they reproduce the relevant component states.
2. **Existing project browser/Playwright/fixture system** when it covers the surface and states.
3. **ADS MCP** when available and a structured rendered evidence run would materially improve verification.
4. **Host browser/screenshot tools** as a portable fallback.
5. **Manual user-provided captures** when the environment cannot render directly; state the limitation.

Default maximum: **one primary evidence provider per verification pass**. A secondary tool is justified only when it covers a different dimension, not to duplicate the same screenshot.

For reference-driven work, the evidence source should support comparable captures whenever possible; the goal is to judge the rendered artifact rather than only source code or remembered reference descriptions.

## 8. Divergence decision

Use multiple directions when the expected value of exploration exceeds the cost.

Usually yes:

- creating/replacing a visual identity;
- high-value expressive hero/landing direction;
- new page/flow with genuinely different information architectures;
- a visual concept where premature convergence would materially reduce quality.

Usually no:

- known defect repair;
- component implementation under a settled design;
- local polish;
- exact user-specified composition;
- low-risk changes where alternatives would only differ cosmetically.

When exploring, alternatives must change a meaningful structural or visual premise. Three variants of the same centered hero are one direction, not three.

Do not force structural novelty merely to be different from a previous build. Variety is valuable when it serves the brief; it is not a gate.

## 9. Human gates

Require or strongly prefer a human choice when:

- the project identity is being replaced;
- multiple directions have legitimate subjective tradeoffs;
- a consequential workflow would change information architecture or familiar interaction semantics;
- external references create meaningful IP/brand similarity concerns.

Do not manufacture a human gate for every small UI decision or require approval checkpoints when the user has already supplied enough authority to proceed.

## 10. Provider conflicts

When two provider rules conflict:

1. canonical project truth wins;
2. explicit current user intent wins over provider taste;
3. task/surface-specific safety and UX constraints win over generic anti-slop guidance;
4. use one provider's coherent method rather than blending incompatible doctrines;
5. if both remain plausible, expose the tradeoff rather than averaging them into a vague compromise.

## 11. No-provider path

A successful Design Pipeline run may use **zero external providers**.

The host agent should still:

- ground in canonical context and real references/assets;
- classify the task/surface;
- decide whether exploration is worthwhile;
- implement against the actual stack;
- gate motion by purpose/frequency rather than decoration;
- capture rendered evidence;
- evaluate separate quality dimensions;
- repair adaptively;
- report remaining uncertainty.