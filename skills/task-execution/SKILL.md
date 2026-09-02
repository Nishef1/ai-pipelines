---
name: task-execution
description: "Default HOST for actionable work. Use for implementation, fixes, reviews, audits, investigations, plans, refactors, redesigns, and verification. Bind work to the narrowest justified target, plan only until material unknowns are bounded, make the smallest coherent change, judge with evidence capable of falsifying the claim, clean up temporary/obsolete artifacts, classify remaining findings against the current target, and stop when Required work is closed. Domain skills define what good looks like in their specialty. Product/work-control systems, repository delivery policy, and release policy remain authoritative for their own concerns."
license: MIT
metadata:
  version: 2.0.0
---

# Task Execution

The default **HOST** workloop for one finite current target.

Its job is not to create more process. Its job is to make the requested outcome true with the least process and code that preserve justified confidence.

```text
project / work control, when present
        ↓ selected target
TASK EXECUTION
UNDERSTAND → PLAN → BUILD → JUDGE → CLEAN → BREAK when useful → STOP
                         ↑                 |
                         └── bounded repair┘
```

Domain skills own specialty-specific quality and tools. Task Execution owns target framing, planning closure, execution discipline, evidence accounting, cleanup, target-relative triage, and stopping.

## 1. Calibrate rigor

Use the lowest rigor that can reliably close the target.

- **Micro** — obvious, narrow, low-risk work. Understand implicitly, change, run the smallest meaningful check, stop.
- **Standard** — normal bugs, features, reviews, refactors, multi-file work, and material UI changes. Use an explicit finite target and acceptance evidence.
- **Critical** — auth/authz, money, sensitive data, destructive state, migrations, concurrency, deployment/recovery, or comparable consequence. Make invariants and failure/recovery paths explicit and use stronger independent evidence where practical.

Do not turn simple work into ceremony merely because this skill is active.

## 2. Bind completion to the right scope

For material work establish:

```text
Target level: TASK | SLICE | FEATURE | MILESTONE | RELEASE
Current target:
Must become true:
Must remain true:
Must never happen:
Proof / judge:
Cleanup obligation:
Out of scope:
```

Use the narrowest justified level.

```text
TASK COMPLETE      ≠ FEATURE COMPLETE
SLICE COMPLETE     ≠ FEATURE COMPLETE
FEATURE COMPLETE   ≠ MILESTONE COMPLETE
MILESTONE COMPLETE ≠ RELEASE READY
```

`STOP` means no Required work remains for the current target.
`SHIP` is reserved for an explicitly evaluated RELEASE target that is actually release-ready.

Read `references/project-compass.md` when target level, finish-line definition, or project-level continuation is ambiguous.

## 3. Respect authority boundaries

Prefer, in order:

1. system/safety/tool constraints;
2. explicit current user intent;
3. canonical product/policy/security/legal/architecture/design sources;
4. authoritative work-control/spec state when adopted by the project;
5. actual implementation, contracts, schema, runtime, tests, and current repository state;
6. relevant domain guidance and current official documentation;
7. external examples/discussion.

Do not invent a second roadmap, backlog, scheduler, repository delivery policy, or source of product truth.

When an external tracker/orchestrator exists, consume its assigned target and return evidence; do not create a competing work graph.

Read `references/control-plane.md` when issue tracking, specs, external orchestration, long-running state, repository-delivery policy, or release control is involved.

## 4. UNDERSTAND — establish the task contract

Before building material work:

- inspect the strongest relevant project truth and the actual affected implementation;
- map enough sibling surface to avoid obvious blind spots;
- cheaply check whether the requested invariant already exists and works;
- resolve or explicitly surface material conflicts;
- distinguish facts from assumptions.

Do not rewrite working code simply to create activity.

Ask the user only when a genuinely unresolved product/authority choice materially changes the outcome and cannot be resolved from current truth.

## 5. PLAN — stop planning at closure

Planning closure exists when:

- the finite outcome is understood;
- material affected boundaries are mapped;
- important positive and negative requirements are known;
- no unresolved high-impact unknown currently makes implementation premature;
- at least one credible oracle can judge success.

Then build.

Do not keep browsing, brainstorming, or decomposing merely to increase confidence after planning closure.

For broad work, map breadth before diving deeply into one path.

## 6. BUILD — smallest coherent change

Prefer:

```text
existing mechanism
→ simplify/fix it
→ existing platform/framework capability
→ suitable existing dependency
→ smallest justified new implementation
```

Every changed hunk must trace to one of:

1. a current-target requirement;
2. a necessary dependency of that requirement;
3. cleanup caused by the same change.

Avoid speculative abstraction, duplicate helpers/state, future-proof frameworks, compatibility debris, and unrelated cleanup.

When repository mutation was requested and write access exists, modify the real repository. A patch is not the final deliverable unless the user requested one or direct write is genuinely unavailable.

Repository commit/push behavior follows active user/project policy. A normal source change does not by itself authorize production deploy/release publication, force-push, destructive remote data operations, purchases, or external communications.

## 7. TEST/PROBE POLICY — evidence, not test-count optimization

Do not treat test count or coverage growth as progress by itself.

Before adding a test, ask whether an existing verifier already proves the claim.

Any new diagnostic check is one of:

- **TEMPORARY PROBE** — helps reproduce/diagnose the current task and should normally be removed before completion.
- **DURABLE REGRESSION TEST** — protects a stable user-visible contract, invariant, protocol, security boundary, or historically important failure mode.

A durable test must have a clear counterfactual: if the protected fault returns, the test should fail for the right reason.

Do not persist tests that merely freeze current DOM/CSS shape, internal helper structure, implementation details, mocks, token values, class names, or behavior already guaranteed by stronger existing checks unless the project explicitly treats that shape as contract.

Prefer real behavior/integration evidence over mock-heavy duplication when the boundary matters.

For bugs, use the same reproduction before and after the fix when practical.

Read `references/evidence.md` and `references/cleanup-and-tests.md` for substantial verification or test-heavy work.

## 8. JUDGE — prove the claim, not the command

JUDGE is logically separate from BUILD.

For each Required claim:

1. choose the cheapest credible oracle capable of falsifying it;
2. run/inspect that oracle;
3. confirm the intended scenario actually ran;
4. inspect semantic output, not just exit code, availability, or a generated PASS string;
5. record material coverage limits.

Prefer evidence close to reality:

```text
runtime/user-visible behavior
→ integration/state test
→ deterministic structural/static check
→ rendered state tied to viewport/data
→ source inspection
→ heuristic reasoning
```

Use the modality appropriate to the claim. A visual claim needs rendered visual evidence; a payment/auth claim needs authoritative state/boundary evidence.

Evidence invalidated by later relevant changes becomes STALE.

Never report an unrun check as passed.

## 9. CLEAN — leave less residue, not more

Before completion perform a bounded artifact cleanup for the changed surface.

Check for:

- temporary probes/debug scripts/logging;
- generated scratch files and one-off fixtures;
- superseded implementation paths, dead components/helpers, obsolete tests, stale imports/config;
- wrappers/abstractions introduced during exploration that are no longer necessary;
- comments/docs that describe behavior removed by this change.

For redesigns/refactors/replacements, deletion is expected when the new path supersedes the old one. Do not keep obsolete behavior merely because removing it feels risky; verify consumers and delete it when genuinely unused.

Use a **change-budget audit** as a diagnostic, not a numeric gate:

```text
files added/removed
affected files
net code growth
new dependencies
new abstractions
new durable tests
obsolete path removed?
```

Unexpected growth should trigger explanation/simplification, not automatic failure.

Read `references/cleanup-and-tests.md` when the task creates multiple files/tests/helpers or replaces an existing implementation.

## 10. BREAK — bounded independent challenge

Use a fresh review context when available and useful for material/high-risk work or subjective design evaluation.

BREAK asks only whether the current target is falsely considered complete. It is not a project-wide bug hunt.

A confirmed defect needs concrete evidence such as:

- reproducible failure;
- contradiction with authoritative truth;
- directly observable counterexample;
- violated invariant/acceptance clause.

A plausible concern without evidence is a risk/question, not automatically Required work.

If a material defect appears: diagnose → bounded repair → re-JUDGE affected claims → CLEAN affected residue → fresh BREAK only if useful.

Read `references/break.md` for substantial or critical passes.

## 11. Findings are not automatically work

Classify findings against the current target:

- **REQUIRED** — target cannot honestly be met without it.
- **RECOMMENDED** — meaningful improvement, not a blocker.
- **OPTIONAL** — useful but low leverage.
- **DEFERRED** — intentionally postponed and visible.
- **IRRELEVANT** — no material impact on this target.

Do not silently expand scope. More possible improvement does not mean the current target is unfinished.

## 12. Domain skills remain authoritative

Load a domain skill only when the specialty is material.

Examples:

- material UI/UX → `design-pipeline`;
- security/auth/payment → applicable security guidance/skill;
- database/migration → applicable DB domain guidance;
- deployment/recovery → applicable operations/deployment guidance.

Use one HOST. Do not stack competing generic execution/planning hosts.

When a domain skill is active:

- share the same current target and task contract;
- let the domain skill decide what good looks like and which specialty evidence matters;
- return its findings/evidence to this host for target-relative triage;
- do not let it silently widen the target.

## 13. Long/resumable work

Persist task-local gates only when conversation fragility or orchestration justifies it. Reuse an existing project convention when available.

A gate ledger is an evidence cache for the current target, never a shadow roadmap/backlog.

Read `references/evidence.md` for gate freshness/locality and `references/control-plane.md` for scheduler/work-control boundaries.

## 14. Completion predicate

The target is complete only when all are true:

```text
Required obligations = 0
AND required evidence is current
AND cleanup obligation is satisfied
AND material changed hunks are accounted for
AND repository delivery obligations are satisfied or a real blocker is reported
```

Then STOP.

Do not run another broad audit because more improvement is theoretically possible.

For material final reports distinguish:

```text
Checked:
Sampled:
Inferred:
Not checked:
```

Never let the completion label exceed the evidence scope.

## Core invariant

> Close the user's finite current target with the smallest coherent change and strongest proportionate evidence, without manufacturing progress through extra code, tests, files, abstractions, or endless review. Clean up exploration residue, challenge false completion, and stop when the target is actually met.
