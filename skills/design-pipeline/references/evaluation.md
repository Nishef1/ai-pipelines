# Evaluation

Use this reference for material design reviews and final verification.

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

## 2. Evidence hierarchy

For each finding, attach the strongest available evidence:

1. runtime interaction/result;
2. reproducible rendered state or story/fixture;
3. screenshot tied to a known state and viewport;
4. DOM/style/source evidence;
5. heuristic reasoning;
6. aesthetic preference.

Do not present a lower-level inference as stronger evidence than it is.

## 3. Reference images

A screenshot, Figma frame, Stitch output, generated comp, or external site may establish visual intent such as composition, hierarchy, material, color relationship, and typography character.

It does **not** establish:

- authorization rules;
- payment or financial truth;
- persistence behavior;
- navigation semantics;
- server state transitions;
- error handling;
- data provenance.

Behavior must be verified from product/runtime authority.

## 4. Repair loop

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

- no material issue remains;
- further changes are preference tradeoffs rather than defects;
- the latest pass did not improve the evidence;
- cost/iteration budget is reached;
- the direction is fundamentally wrong and should be re-selected instead of patched.

Do not use a hard-coded seven-round or one-round rule.

## 5. Severity

Use severity for actionability, not drama.

- **Blocker** — prevents task completion, creates unsafe/misleading behavior, or invalidates evaluation.
- **Major** — materially harms comprehension, accessibility, interaction, responsive use, or accepted direction.
- **Moderate** — clear quality issue with limited task impact.
- **Preference** — legitimate subjective alternative; requires choice, not auto-fix.

Aesthetic disagreement alone is not a blocker.

## 6. Evaluating Design Pipeline itself

A beautiful demo is not evidence that the pipeline works.

Compare the same base agent/harness **with and without** Design Pipeline across multiple independent runs.

Initial scenario families:

1. expressive greenfield landing;
2. existing-brand redesign;
3. dense operational surface;
4. consequential checkout/workflow;
5. bilingual RTL/LTR surface.

Track separately:

- task/functional success;
- accessibility/responsive failures;
- UX/task-fit findings;
- brand/direction fidelity;
- pairwise human aesthetic preference;
- routing correctness (including cases where no provider should be used);
- tool calls, latency, and token/cost overhead;
- number of human corrections;
- variance across runs.

Use several runs for comparative claims because agent execution is stochastic. Do not overfit the skill to one showcase project.

## 7. Keep evaluation partially independent

When practical, do not expose the full evaluation-only rubric to the building agent. Visible acceptance criteria belong in the task; evaluation-only probes can remain outside the build context so the pipeline is less likely to optimize for the checker rather than the actual user outcome.

Do not hide requirements that the user genuinely needs to know to build the feature correctly.

## 8. Reporting

Final reports should state:

- what was actually rendered/interacted with;
- which states/viewports were inspected;
- which checks were automated vs judged;
- unresolved assumptions or user-validation gaps;
- subjective decisions that remain preferences rather than correctness findings.

Never translate "not checked" into "passed".
