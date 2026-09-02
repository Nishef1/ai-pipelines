---
name: design-pipeline
description: "DOMAIN skill for material web UI/UX design, redesign, review, and visual verification. Use for meaningful visual direction, UX structure, new surfaces, consequential product UI, reference-driven work, or final rendered quality review. Ground in project truth, create/select a concrete direction before production code when references/design authority are weak, use at most one primary craft approach per build pass, verify the real rendered result, and keep functional/UX/brand/aesthetic verdicts separate. Not for backend-only work or trivial local style repairs."
license: Apache-2.0
metadata:
  version: 2.0.1
---

# Design Pipeline

A **DOMAIN** skill for material design quality, not a second execution host.

```text
task-execution HOST
        ↓ material UI concern
GROUND → CLASSIFY → DIRECTION → BUILD → CAPTURE → FRESH JUDGE → REPAIR
        ↓ evidence/findings
task-execution triage / cleanup / stop
```

This skill owns design classification, visual direction, craft routing, rendered evidence, and visual evaluation. Repository delivery, release readiness, and project-wide priority remain outside it.

## 1. GROUND in real truth

Resolve in this order:

1. canonical product/policy/legal/security/architecture truth;
2. explicit current user intent;
3. accepted project design memory such as `DESIGN.md`;
4. actual implementation, tokens/components/assets, and current rendered behavior;
5. approved surface-specific direction/reference;
6. current research/external inspiration;
7. optional provider guidance;
8. model defaults.

References/providers are evidence or inspiration, not authority over business behavior. A screenshot never defines authorization, payment, persistence, or state transitions.

## 2. CLASSIFY

### Change class
- **Greenfield** — no established visual authority.
- **New world** — identity is being created/replaced.
- **New surface** — new page/flow in an established world.
- **Refinement** — improve while preserving accepted identity/behavior.
- **Repair** — known local defect, little design freedom.
- **Review** — evaluate only unless implementation is requested.

### Surface mode
- **Persuade** — landing/marketing/pricing/campaign.
- **Operate** — dashboard/settings/admin/marketplace/checkout/workflow.
- **Read** — docs/help/policy.
- **Experience** — portfolio/gallery/showcase.

### Design authority
- **Established** — preserve unless replacement requested.
- **Incomplete** — preserve confirmed traits; direction work may be needed.
- **None** — create direction.
- **Replacement requested** — old look is evidence/anti-reference, not authority.

### Risk
- **Low** — cosmetic/local/reversible.
- **Normal** — ordinary product/marketing UI.
- **Consequential** — money, destructive actions, permissions, identity/auth, compliance, high error cost.

Consequential surfaces prioritize truth, recovery, accessibility, and familiar semantics over novelty.

## 3. Decide whether a DIRECTION phase is needed

Do not discover a materially uncertain visual world by repeatedly patching production CSS.

### Strong reference exists
Extract composition, hierarchy, density, typography character, palette/material relationships, imagery, and motion. Preserve project content/behavior and compare the real implementation against the reference at meaningful states/viewports. Copy principles, not another brand's protected identity/assets/copy.

### No reference, established design world
Derive from accepted design memory, strongest existing surfaces/components, and task/content/state requirements. Avoid unnecessary visual exploration.

### No reference + weak/incomplete/no authority
Before production implementation:

1. research only enough current references to expand the option space;
2. derive 2–4 materially different **Design DNAs**;
3. concretize promising directions as mockups/scratch renders/prototypes outside the permanent production path when practical;
4. compare product fit, UX, originality/specificity, craft, accessibility/localization/responsive viability, and implementation fit;
5. select one coherent direction;
6. persist only durable accepted design memory.

Three cosmetic variants of the same layout are one direction, not three. If visual generation is available, visible alternatives are preferable to asking a non-designer user to imagine textual options.

Read `references/direction.md` for no-reference/new-world work.

## 4. Route the minimum useful craft capability

Default to project-aware native reasoning when enough.

Use at most **one primary craft approach/provider per build pass**. Do not average several design doctrines.

- **Operate / consequential UI** — project design truth first; Impeccable-style Operate craft is preferred when current/reviewed and useful. Taste-style pressure is normally off.
- **Persuade** — choose one coherent approach; Impeccable or Taste-style anti-default exploration may be appropriate depending on the brief.
- **Experience** — expressive/Taste-style exploration may fit.
- **Read** — project/native typography and information architecture usually suffice.
- **Repair/trivial** — usually no provider.

A second provider may act only as a **fresh critic**, not co-builder, when it adds materially different judgment.

Provider compatibility/reviewed refs live in `references/providers.json`. If the recorded provider ref has drifted, do not rely on version-specific behavior until re-reviewed. Never auto-install or auto-update a provider merely because it is newer.

## 5. BUILD one coherent direction

Use the project's real stack and state model.

- reuse accepted tokens/components/primitives when they still serve the chosen direction;
- if replacement is requested, do not preserve incumbent styling merely because it exists;
- prefer existing production interaction primitives over parallel hand-rolled dialogs/menus/comboboxes/toasts;
- treat accessibility, RTL/LTR, localization, responsive transformation, real/long content, and relevant loading/empty/error/unknown/permission states as correctness;
- do not add animation/component dependencies solely because a reference/provider uses them.

### Persuade
Make audience, outcome, proof, and primary action legible. Do not fabricate metrics, testimonials, badges, guarantees, or social proof.

### Operate
Optimize task completion, state truth, hierarchy, scanability, predictable affordances, error prevention/recovery, and appropriate density.

### Motion
Optional. Use for feedback, continuity, state, explanation, or justified delight. High-frequency/consequential actions generally need less motion. Reduced-motion must preserve comprehension.

## 6. CAPTURE rendered evidence

Source inspection is preflight, not visual proof.

For material visual claims, inspect the real rendered artifact through the strongest existing route, roughly:

1. representative project fixture/Storybook if already present;
2. project browser/Playwright harness;
3. reviewed external evidence provider when it fills a real gap;
4. available browser/screenshot capability;
5. user capture only when direct rendering is unavailable, with the limitation stated.

Capture only material states/viewports. Include as relevant:

- mobile/tablet/desktop;
- Persian/English and RTL/LTR;
- supported light/dark modes;
- real/long content;
- loading/empty/error/disabled/permission/unknown;
- keyboard/focus/touch;
- zoom/reflow.

Build/lint/type/test success does not prove visual quality.

## 7. FRESH JUDGE

For material redesign/review, use a fresh bounded review context when practical and useful. It must inspect rendered evidence rather than trust builder narration.

Keep verdicts separate:

1. **Functional correctness** — behavior/states/semantics/runtime.
2. **UX/task fit** — comprehension/hierarchy/affordance/recovery/workload.
3. **Brand/system fidelity** — accepted authority or approved new direction.
4. **Aesthetic quality/preference** — coherence/craft/originality/specificity/character.

Do not collapse these into one fake universal score.

Useful lenses: hierarchy; composition/grouping/alignment/rhythm; typography/script fit; color/contrast/state meaning; affordance/feedback; density/disclosure; originality/product specificity; responsive transformation; real-content resilience.

The judge asks whether the current target is materially deficient, not whether infinite polish remains possible.

Read `references/evaluation.md` for substantial final reviews.

## 8. REPAIR adaptively, then stop

If Blocker/Major findings exist:

```text
finding + evidence
→ coherent repair batch
→ recapture affected render
→ re-judge affected dimensions
```

If the chosen direction itself is wrong, return to direction selection instead of stacking CSS patches.

Stop when no material current-target finding remains, remaining differences are legitimate preference tradeoffs, or another pass yields no meaningful improvement. Do not chase a numeric 10/10 or a fixed loop count.

## 9. Avoid design-code sediment

Before handoff, identify/remove task-caused scratch mockups, temporary assets, abandoned variants, obsolete components/styles, stale tests/fixtures, and superseded paths.

A redesign that replaces a path should normally delete the old implementation after verifying consumers.

Do not create brittle tests whose purpose is to freeze current theme, exact DOM nesting, class names, token values, or screenshot shape unless the project explicitly defines that artifact as a stable contract.

Persist design memory conservatively: durable accepted grammar/identity only, not rejected variants, provider prompts, run screenshots, or one-off page decisions.

## 10. Report to the HOST

Return concise evidence:

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
Temporary/obsolete design artifacts:
```

Never claim a visual check passed when no rendered evidence was inspected.

> Do not let model defaults or production CSS become the design process. Ground in product truth, create/select a concrete direction when needed, build one coherent thesis, judge the real render with fresh bounded evaluation, and remove exploration residue.
