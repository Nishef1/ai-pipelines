---
name: design-pipeline
description: "DOMAIN skill for material web UI/UX design, redesign, review, and visual verification. Use when the task involves meaningful visual direction, UX structure, a new surface, consequential product UI, reference-driven work, or a final rendered quality review. Ground in project truth, determine whether design authority/reference is sufficient, create or compare concrete directions before production code when needed, route at most one craft approach per build pass, verify the real rendered result, and keep functional/UX/brand/aesthetic verdicts separate. Not for backend-only work or trivial local style repairs."
license: Apache-2.0
metadata:
  version: 2.0.0
---

# Design Pipeline

A **DOMAIN** skill for design quality. It is not a second global execution host.

When `task-execution` is active, both share one Current Target and Task Contract:

```text
task-execution HOST
        ↓ material UI concern
design-pipeline DOMAIN
GROUND → CLASSIFY → DIRECTION → BUILD → CAPTURE → FRESH JUDGE → REPAIR
        ↓ evidence/findings
task-execution triage / cleanup / stop
```

Design Pipeline owns design classification, visual direction, craft routing, design-specific evidence, and rendered evaluation. It does not own project-wide priority, repository delivery policy, release readiness, or a competing global ledger.

## 1. Ground in real project truth

Resolve, in order:

1. canonical product/policy/legal/security/architecture truth;
2. explicit current user intent;
3. accepted project design memory such as `DESIGN.md`;
4. actual implementation, tokens/components/assets, and current rendered behavior;
5. approved surface-specific direction/reference;
6. current research and external inspiration;
7. optional provider guidance;
8. model defaults.

External screenshots/sites/providers are evidence or inspiration, not authority over product behavior.

A visual reference specifies appearance and composition, not authorization, payment, persistence, state transitions, or other consequential behavior.

## 2. Classify the design task

### Change class

- **Greenfield** — no established UI/design authority.
- **New world** — visual identity is being created or explicitly replaced.
- **New surface** — new page/flow inside an established world.
- **Refinement** — improve an existing surface while preserving accepted identity/behavior.
- **Repair** — known defect with little design freedom.
- **Review** — evaluate without implementation unless asked.

### Surface mode

- **Persuade** — landing, marketing, public pricing/campaign.
- **Operate** — dashboard, settings, admin, marketplace, checkout, workflow.
- **Read** — docs/help/policy.
- **Experience** — portfolio/gallery/showcase.

### Design authority

- **Established** — preserve unless replacement requested.
- **Incomplete** — preserve confirmed traits; direction work may be needed.
- **None** — create a visual direction.
- **Replacement requested** — old look becomes evidence/anti-reference, not authority.

### Risk

- **Low** — cosmetic/local and reversible.
- **Normal** — ordinary product/marketing UI.
- **Consequential** — money, destructive action, permissions, identity/auth, compliance, or high error cost.

Consequential surfaces prioritize state truth, recovery, accessibility, and familiar semantics over novelty.

## 3. Decide whether direction work is required

Do **not** discover visual direction inside production code when the visual world is materially uncertain.

### A. Strong reference exists

Use the reference as visual evidence:

- inspect project source/assets before guessing from pixels;
- preserve real user/project assets where authoritative;
- extract composition, hierarchy, density, typography character, palette relationships, imagery, and motion character;
- compare the implemented render to the reference at meaningful viewports/states;
- copy principles, not another brand's protected identity/assets/copy.

### B. No reference, established design world

Derive the direction from:

- accepted `DESIGN.md`/equivalent;
- the strongest existing surfaces/components;
- product task/content/state requirements.

Avoid unnecessary visual-world exploration. Refine/extend coherently.

### C. No reference and design authority is incomplete/weak/none

Run a **Design Direction Phase before production implementation**.

1. research only enough current references/products to expand the option space;
2. derive 2–4 materially different **Design DNAs**, not adjective-only themes;
3. concretize promising directions as mockups/scratch renders/prototypes outside the permanent production path when practical;
4. compare directions against product fit, UX, originality, craft, accessibility, and implementation reality;
5. select one direction before production build;
6. persist only durable accepted design memory, not the exploration log.

A Design DNA should describe concrete choices such as:

```text
information hierarchy
macro-layout / reading flow
density and whitespace strategy
typography character and scale relationships
color/material role
imagery/icon direction
shape/border/depth language
interaction/motion character
what makes this product-specific
```

Three variants of the same centered-card layout are one direction, not three.

Read `references/direction.md` when the user has no reference, the current design feels generic, or a new/replacement visual world is in scope.

## 4. Route the minimum useful craft capability

Default: native project-aware design reasoning is allowed.

Use at most **one primary craft approach/provider per build pass**. Do not stack multiple design doctrines merely for more quality.

Guidance:

- **Operate / consequential product UI** — prefer project design truth and an Impeccable Operate-style craft pass when available and useful. Taste-style anti-default pressure is normally off.
- **Persuade** — choose one coherent craft direction. Impeccable is a strong default for product-aware craft; Taste-style pressure can be used instead when the brief needs expressive anti-default exploration.
- **Experience** — expressive craft/Taste-style exploration may be appropriate.
- **Read** — project/native typography and information architecture usually suffice.
- **Repair/trivial work** — usually no provider.

A second design system/provider may be used only as a **fresh evaluator/critic lens**, not a co-builder, when it supplies materially different judgment. Its findings still require evidence and target-relative triage.

Provider metadata and compatibility live in `references/providers.json`. Route by capability, not popularity.

## 5. Build against the chosen direction

Use the project's actual stack and state model.

- reuse accepted tokens/components/primitives when they still serve the chosen direction;
- if replacement is explicitly requested, do not preserve incumbent styling merely because it exists;
- do not infer business logic or permissions from visual references;
- prefer production-quality existing interaction primitives over parallel hand-rolled dialogs/menus/comboboxes/toasts/virtualization;
- keep accessibility, RTL/LTR, localization, responsive transformation, real content, and relevant loading/empty/error/unknown/permission states inside correctness;
- do not add animation/component dependencies solely because an external reference/provider uses them.

### Persuade surfaces

Make the audience/outcome/primary action legible. Keep proof near claims. Avoid fabricated metrics, testimonials, badges, guarantees, or social proof.

### Operate surfaces

Optimize task completion, state truth, information hierarchy, scanability, predictable affordances, error prevention/recovery, and density appropriate to frequency/expertise.

### Motion

Motion is optional. Add it only for feedback, continuity, state indication, explanation, or justified delight. High-frequency/consequential actions should generally use less motion. Reduced-motion behavior must preserve comprehension.

## 6. Capture rendered evidence

Source inspection is preflight, not visual proof.

For material visual claims, capture/inspect the real rendered artifact through the best existing evidence source:

1. project Storybook/fixtures when representative;
2. project browser/Playwright harness;
3. reviewed external evidence provider when it fills a real gap;
4. host browser/screenshot capability;
5. user-provided captures only when direct rendering is unavailable, with the limitation stated.

Capture only states/viewports material to the current target.

Typical dimensions when relevant:

- mobile / tablet / desktop;
- Persian/English and RTL/LTR;
- light/dark supported modes;
- long/real content;
- loading/empty/error/disabled/permission/unknown states;
- keyboard/focus/touch behavior;
- zoom/reflow.

A build/lint/test pass does **not** prove aesthetic or layout quality.

## 7. Use a fresh bounded visual judge

For material redesigns/reviews, use a fresh review context when practical. The judge must inspect rendered evidence rather than trust the builder's self-description.

Keep four verdicts separate:

1. **Functional correctness** — behavior, states, semantics, runtime defects.
2. **UX / task fit** — comprehension, hierarchy, affordance, recovery, workload.
3. **Brand / system fidelity** — accepted design authority or approved new direction.
4. **Aesthetic quality/preference** — coherence, craft, originality/specificity, visual character.

Do not collapse these into one numeric score.

The visual judge asks whether the current target is materially deficient, not whether infinite polish remains possible.

Useful diagnostic lenses:

- hierarchy;
- composition/grouping/alignment/rhythm;
- typography/script fit;
- color/contrast/state meaning;
- affordance/feedback;
- information density/disclosure;
- originality/product specificity;
- responsive transformation;
- real-content resilience.

Read `references/evaluation.md` for reviews/final verification.

## 8. Repair adaptively

If the judge finds Blocker/Major issues:

```text
finding + evidence
→ coherent repair batch
→ recapture affected render
→ re-judge affected dimensions
```

Stop when:

- no material finding remains for the current target;
- remaining differences are legitimate preference tradeoffs;
- another pass produces no meaningful improvement;
- the chosen direction is wrong, in which case return to direction selection rather than stacking patches.

Do not run a fixed number of self-critique loops or chase 10/10.

## 9. Avoid design-code sediment

Exploration should not leave permanent production residue.

Before handing back to the HOST, identify scratch mockups, obsolete components/styles, temporary assets, abandoned variants, old replacement paths, and stale tests/fixtures created by the design task so the host cleanup phase can remove them.

A redesign that replaces a path should normally delete the superseded implementation after verifying consumers.

Do not create brittle tests whose only purpose is to freeze the current theme, exact DOM nesting, class names, token values, or screenshot shape unless the project explicitly declares that artifact a stable contract.

## 10. Learn conservatively

Do not persist every successful choice as a permanent rule.

Separate:

- **project memory** — durable accepted design grammar/identity;
- **run memory** — references, rejected variants, screenshots, temporary findings;
- **personal preference** — cross-project taste, outside this skill's project truth.

Persist durable design memory only when the project benefits from it and the direction is accepted/repeated enough to justify it.

## 11. Report to the HOST

Return concise domain evidence:

```text
Design class / surface / authority:
Direction used:
Craft capability actually used:
Rendered states/viewports inspected:
Functional findings:
UX findings:
Brand/system findings:
Aesthetic/preference findings:
Material unverified areas:
Temporary/obsolete design artifacts to clean:
```

Never claim a visual check passed if no rendered evidence was inspected.

## Core invariant

> Do not let the model's default aesthetic or production CSS be the design process. Ground in product truth, create/select a concrete direction when references are missing, build one coherent visual thesis, judge the real rendered artifact with fresh bounded evaluation, remove exploration residue, and return only material findings to the execution host.
