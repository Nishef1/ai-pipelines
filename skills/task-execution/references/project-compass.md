# Project Compass

Use when the task belongs to a larger product/project and scope, priority, or stopping matters.

## Purpose

Separate the infinite product from the finite thing currently being closed.

```text
Product destination
      ↓
Authoritative priority / work control, when present
      ↓
Target Level → Current Target → Finish Line → Work Class → Next Move
```

## Target levels

Use the narrowest level justified by the actual request and authoritative project context:

- **TASK** — one bounded requested change or analysis.
- **SLICE** — one coherent portion of a larger feature/journey.
- **FEATURE** — an end-to-end capability with explicit feature-level acceptance.
- **MILESTONE** — a grouped product/project objective with its own exit criteria.
- **RELEASE** — a version/deployment target whose readiness is being judged.

Do not infer a higher target merely because the current work is nested inside it.

```text
TASK COMPLETE      ≠ FEATURE COMPLETE
SLICE COMPLETE     ≠ FEATURE COMPLETE
FEATURE COMPLETE   ≠ MILESTONE COMPLETE
MILESTONE COMPLETE ≠ RELEASE READY
```

## Work classes

Classify against the **Current Target**, not the imagined final product:

- **REQUIRED** — current target cannot honestly be met without it.
- **RECOMMENDED** — meaningful quality/risk improvement, not a blocker.
- **OPTIONAL** — useful but low leverage for the current target.
- **DEFERRED** — consciously postponed and visible.
- **IRRELEVANT** — no material current-target impact.

Finding is not work. Every new finding is triaged before becoming active scope.

## Finish Line

Prefer observable obligations, not percentages. Do not average critical and cosmetic dimensions into one readiness score.

Bad:

```text
project is 93% ready
```

Better:

```text
Target Level: MILESTONE
Current Target: Minimum Launch
Required remaining: 2
- interrupted-payment recovery
- production critical-flow verification
```

When Required remaining reaches zero and required evidence is current, the **Current Target** is met. Stop that execution loop. Remaining Recommended/Optional work can be reported without becoming blockers.

## Completion vocabulary

Match the label to the scope actually evaluated:

- `TASK COMPLETE`
- `SLICE COMPLETE`
- `FEATURE COMPLETE`
- `MILESTONE COMPLETE`
- `RELEASE READY`

`STOP` means no more Required work remains for the current target. It is valid at any target level.

`SHIP` is not a synonym for `STOP` or `COMPLETE`. It is a release action/recommendation and is permitted only when:

1. `Target Level = RELEASE`;
2. release-level Finish Line obligations were actually in scope;
3. relevant cross-feature/integration evidence is current;
4. unresolved release risks are explicitly accepted or non-blocking;
5. the user/project release policy permits shipping.

A local task may be perfectly complete while the feature, milestone, and product remain unfinished.

## Priority boundaries

Task Execution may classify and recommend work **within the Current Target**.

Project-wide product priority should come from explicit user/product strategy or the project's authoritative work-control source. Dependency readiness is not business value:

```text
READY ≠ IMPORTANT
UNBLOCKED ≠ NEXT PRODUCT PRIORITY
```

If no project-wide priority authority exists, offer a reasoned recommendation and label it as such. Do not invent a roadmap and present it as project truth.

## Next moves

At most three distinct choices when continuation matters:

```text
1. REQUIRED — action / why / current-target effect
2. RECOMMENDED — action / why / current-target effect
3. STOP — when the current target is met
```

If the Current Target is an explicit release and status is `RELEASE READY`, `SHIP release` may be the recommended action.

The user should not need to ask “what remains for this target?” But the skill must not pretend to know the product's next strategic priority when no authority establishes it.