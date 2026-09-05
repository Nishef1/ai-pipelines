# Evaluation

Use this reference for material design reviews, change reviews, and final verification.

Design quality is not one scalar. Keep evidence and verdicts separated so a strong visual impression cannot hide a functional or UX failure, and a deterministic lint score cannot pretend to settle subjective taste.

## 1. Four independent verdicts

### Functional correctness

Evaluate observable behavior and implementation truth:

- requested states exist and are reachable;
- controls perform the intended action;
- loading, empty, error, disabled, unknown, and destructive states are coherent where relevant;
- keyboard/focus/semantics work for supported interactions;
- responsive layouts do not break or hide required actions;
- localization and RTL/LTR do not corrupt meaning or order;
- runtime errors, overflow, inaccessible targets, and contradictory enabled/disabled cues are defects.

This dimension may use deterministic tools and automated evidence.

### UX / task fit

Evaluate whether the surface helps the intended user succeed:

- information architecture matches the task;
- system status and consequences are understandable;
- the next action is discoverable;
- recognition is preferred over unnecessary recall;
- consequential actions prevent/recover from errors appropriately;
- forms ask for necessary information and communicate validation/recovery clearly;
- density and disclosure match frequency, expertise, and consequence;
- the design does not use dark patterns or decorative trust signals as proof.

Distinguish heuristic/expert reasoning from user validation. If no real user evidence exists, label conclusions as heuristic or assumptions.

### Brand / system fidelity

Evaluate against the strongest accepted visual authority:

- approved `DESIGN.md` or equivalent project memory;
- canonical tokens and shared components;
- authoritative project/user assets;
- an explicitly approved redesign direction or comp;
- incumbent identity when the task is preserve/refine.

A redesign explicitly authorized to replace the old visual world should not be penalized for departing from the old look.

### Aesthetic preference

Treat aesthetic preference as subjective and context-dependent.

Prefer:

- pairwise comparison of materially different options;
- blinded A/B presentation when practical;
- explicit tradeoffs rather than universal 1–10 scores;
- human choice for identity-changing decisions.

A provider-local score may be useful diagnostic evidence, but never becomes Design Pipeline's global design score.

## 2. Diagnostic lenses

Use only the lenses relevant to the task. They help locate a problem; they are not independent truth scores that must be averaged.

- **Visual hierarchy** — entry point, eye flow, emphasis, primary/secondary/tertiary distinction.
- **Composition** — grouping, alignment, whitespace, balance, rhythm, reading order.
- **Typography** — scale, measure, legibility, hierarchy, language/script fit, token consistency.
- **Color** — contrast, semantic use, palette relationships, state differentiation.
- **Affordance** — whether actions look actionable and state/feedback is discoverable.
- **Information density** — whether content load and disclosure fit frequency, expertise, viewport, and task.
- **Specificity / originality** — whether the result expresses this product/direction rather than a generic template, without sacrificing task clarity.

Use concrete evidence and user impact. Avoid universal rules such as a mandatory number of colors, fonts, whitespace percentage, title/body ratio, or an obligatory visual "rule break" unless the project or brief establishes one.

## 3. Evidence hierarchy

For each finding, attach the strongest available evidence:

1. runtime interaction/result;
2. reproducible rendered state or story/fixture;
3. screenshot tied to a known state and viewport;
4. deterministic measurement tied to the relevant artifact, such as contrast or geometry;
5. DOM/style/source evidence;
6. heuristic reasoning;
7. aesthetic preference.

Do not present a lower-level inference as stronger evidence than it is.

## 4. Reference-driven evaluation

A screenshot, Figma frame, generated comp, or external site may establish visual intent such as composition, hierarchy, material, color relationship, typography character, density, and motion character.

For fidelity-sensitive work:

- keep the original reference available during evaluation instead of relying on a prose summary;
- prefer real project/user assets where they are authoritative;
- use measurable evidence such as palette/contrast/geometry when it answers a concrete question;
- compare the implemented browser render to the intended reference at comparable viewports and states;
- distinguish deliberate adaptation from accidental drift.

Reference evidence does **not** establish:

- authorization rules;
- payment or financial truth;
- persistence behavior;
- navigation semantics;
- server state transitions;
- error handling;
- data provenance.

Behavior must be verified from product/runtime authority.

## 5. Change-aware review

When reviewing a branch, pull request, or working-tree UI change, review **the change and its affected surfaces**, not an arbitrary snapshot of the whole repository.

### Resolve scope

State the intended target, base/head when relevant, files included, and meaningful exclusions. If no actual change can be resolved, do not invent a range and call it a review.

### Expand blast radius deliberately

Changed files are evidence, not necessarily the complete surface. Inspect direct consumers/callers/importers when a change can affect rendered behavior. Shared tokens, themes, primitives, and layout infrastructure may justify a wider expansion.

Keep the expansion bounded and say what was not inspected. A hidden cutoff reads as false completeness.

### Read additions and removals

Inspect both sides of the diff. Removed focus styles, labels, states, responsive rules, localization hooks, or motion fallbacks can create regressions that are invisible in the final source alone.

### Classify findings

Use one status when it matters:

- **Introduced** — created by the change.
- **Regression** — something previously valid was weakened or removed by the change.
- **Pre-existing** — present in the affected code/surface but not caused by the change.

Do not turn touching a legacy file into an unsolicited whole-file audit. Pre-existing findings may be mentioned when important, but they should not silently redefine the requested change review or verdict.

### Hold the change to its intent

Compare the implemented change with its stated task/PR/issue intent. Missing loading/error/disabled/responsive/RTL/accessibility states can make a change incomplete even if the states that do exist look polished.

## 6. Motion evaluation

Before treating motion as polish, verify that it has a useful role.

Check:

- **Purpose** — feedback, spatial continuity, state indication, explanation, prevention of a jarring change, or justified delight.
- **Frequency** — high-frequency interactions should not become slower or tiring because of decorative motion.
- **Consequence** — important operational, financial, destructive, or identity flows prioritize clear immediate state over spectacle.
- **Mechanism** — the implementation uses the project's existing/cheapest adequate mechanism rather than a new framework by habit.
- **Interruption** — rapidly repeated or gesture-driven interactions remain coherent when interrupted/reversed.
- **Accessibility** — reduced-motion behavior exists and motion does not become the only carrier of meaning.
- **Performance/lifecycle** — expensive animation or WebGL work is bounded, cleaned up, paused when irrelevant, and has a usable static/final state.

Do not fail an interface merely because it is static. Motion is optional unless it serves an accepted requirement or materially improves the interaction.

## 7. Repair loop

Use an adaptive evidence loop rather than a fixed number of self-critiques:

```text
capture
  ↓
material finding?
  ├─ no → stop
  └─ yes
       ↓
     repair a coherent batch
       ↓
     recapture
       ↓
verified improvement?
  ├─ no → revert/rethink direction
  └─ yes → continue only if material findings remain
```

Stop when:

- no material issue remains for the current target;
- further changes are preference tradeoffs rather than defects;
- the latest pass did not improve the evidence;
- cost/iteration budget is reached;
- the direction is fundamentally wrong and should be re-selected instead of patched.

Ending a review loop is not proof of completion. If budget, capability limits, or an unsuccessful direction leaves material requirements open, return those gaps to the HOST as partial/blocked. Keep the stronger prior version when a later pass regresses it.

Do not use a hard-coded round count or a target score such as 10/10.

## 8. Severity

Use severity for actionability, not drama.

- **Blocker** — prevents task completion, creates unsafe/misleading behavior, or invalidates evaluation.
- **Major** — materially harms comprehension, accessibility, interaction, responsive use, or accepted direction.
- **Moderate** — clear quality issue with limited task impact.
- **Preference** — legitimate subjective alternative; requires choice, not auto-fix.

Aesthetic disagreement alone is not a blocker. But visibly missing an explicit visual requirement (such as the approved media-led composition or a requested expressive direction) is a fidelity gap, not something to dismiss as taste. A functional page alone does not close a redesign request.

## 9. Evaluating Design Pipeline itself

A beautiful demo is not evidence that the pipeline works.

Compare the same base agent/harness **with and without** Design Pipeline across multiple independent runs.

Initial scenario families:

1. expressive greenfield landing;
2. existing-brand redesign;
3. reference-heavy redesign/recreation;
4. dense operational surface;
5. consequential checkout/workflow;
6. bilingual RTL/LTR surface;
7. change-aware UI review;

Track separately:

- task/functional success;
- accessibility/responsive failures;
- UX/task-fit findings;
- brand/direction fidelity;
- reference fidelity where applicable;
- pairwise human aesthetic preference;
- routing correctness (including cases where no provider should be used);
- tool calls, latency, and token/cost overhead;
- number of human corrections;
- variance across runs.

Use several runs for comparative claims because agent execution is stochastic. Do not overfit the skill to one showcase project.

## 10. Keep evaluation partially independent

When practical, do not expose the full evaluation-only rubric to the building agent. Visible acceptance criteria belong in the task; evaluation-only probes can remain outside the build context so the pipeline is less likely to optimize for the checker rather than the actual user outcome.

Do not hide requirements that the user genuinely needs to know to build the feature correctly.

## 11. Reporting

Final reports should state:

- what was actually rendered/interacted with;
- which states/viewports were inspected;
- which reference evidence or deterministic measurements were actually used;
- which checks were automated vs judged;
- for change reviews, the reviewed scope and any material blast radius not inspected;
- unresolved assumptions or user-validation gaps;
- subjective decisions that remain preferences rather than correctness findings.

Never translate "not checked" into "passed".