# Design Direction Without a Strong Reference

Use this when material UI work lacks a strong user-provided reference and the project's design authority is incomplete, weak, or being replaced.

## Goal

Prevent production code from becoming the place where the agent discovers what the product should look like.

The output of this phase is a **chosen design direction**, not a pile of production CSS.

## 1. Gather only decision-relevant context

Inspect:

- product purpose and primary task;
- audience and experience level;
- current content/state requirements;
- existing accepted design traits worth preserving;
- strongest current surfaces and anti-examples;
- relevant competitors/references only when they expand the option space.

Do not research ceremonially. Stop when references cease to add a materially different direction.

## 2. Extract principles, not brand copies

For each useful reference, identify structural signals such as:

- macro-layout and reading flow;
- density and grouping;
- hierarchy strategy;
- typography character;
- imagery/media role;
- palette/material relationships;
- control treatment;
- motion/interaction character;
- what makes the design memorable or product-specific.

Do not copy another brand's protected identity, assets, wording, or distinctive composition wholesale.

## 3. Produce materially different Design DNAs

Default to 2–4 directions when genuine design freedom exists.

A direction should change a meaningful premise, for example:

- product-led dense marketplace vs editorial discovery;
- utilitarian operations console vs calm guided workflow;
- media-led showcase vs information-led comparison.

Each Design DNA should specify:

```text
Name / thesis:
Primary user perception:
Information hierarchy:
Macro-layout / eye flow:
Density / whitespace:
Typography:
Color / material:
Imagery / icon language:
Shape / depth / borders:
Motion / feedback:
Product-specific signature:
Key tradeoff:
```

Avoid adjective-only directions such as "modern", "premium", or "clean" without structural consequences.

## 4. Concretize before production

When practical, make promising directions visible as scratch artifacts:

- generated mockup/image;
- isolated HTML prototype;
- design tool frame;
- disposable route/fixture clearly outside the permanent production path.

Do not create three production implementations just to compare them.

If visual generation is available, prefer showing the user concrete variants side-by-side over asking them to imagine textual descriptions.

Human selection is especially valuable when the tradeoff is genuinely subjective. The user does not need to be a designer; choosing among visible alternatives is enough.

## 5. Select with separate criteria

Compare directions on separate dimensions:

- product/task fit;
- UX clarity and recovery;
- originality / specificity;
- craft/coherence;
- accessibility/localization/responsive viability;
- implementation fit and cost;
- accepted brand/design continuity where relevant.

Do not average them into one fake universal score.

A direction that looks distinctive but harms a consequential workflow should lose to a clearer operational direction.

## 6. Production handoff

Before implementation record only the chosen direction's durable consequences:

```text
Chosen direction:
What remains fixed:
What may change:
Key composition rules:
Key visual signature:
Required responsive/state behavior:
Reference/mockup evidence:
```

Then implement one coherent direction.

## 7. Persist sparingly

After the user accepts a direction and it proves useful across more than one equivalent surface, promote only durable identity/behavior grammar into project design memory.

Do not persist:

- rejected variants;
- run-specific screenshots;
- provider prompts;
- temporary measurements;
- one-off page decisions that are not system rules.

## Anti-patterns

- production CSS as visual brainstorming;
- stacking several design providers into one averaged style;
- "anti-slop" prohibitions with no positive direction;
- three cosmetic variants of the same layout;
- treating one model-generated mockup as established project truth;
- forcing every project into the same fonts, radii, gradients, or motion recipes.
