---
name: task-execution
description: "Default HOST for actionable work. Use for implementation, fixes, reviews, audits, investigations, plans, refactors, redesigns, and verification. Bind work to the narrowest justified target, plan only until material unknowns are bounded, make the smallest coherent change, judge with evidence capable of falsifying the claim, clean temporary/obsolete artifacts, classify remaining findings against the current target, and stop when Required work is closed. Domain skills define specialty quality."
license: MIT
metadata:
  version: 2.0.2
---

# Task Execution

The single default **HOST** for one finite current target.

```text
project/work control, when present
        ↓ selected target
UNDERSTAND → PLAN → BUILD → JUDGE → CLEAN → BREAK when useful → STOP
                         ↑                 |
                         └── bounded repair┘
```

Use the least process and permanent code that can close the target with justified confidence. Domain skills own specialty quality; this skill owns target framing, planning closure, execution discipline, evidence accounting, cleanup, triage, and stopping.

## 1. Calibrate rigor

- **Micro** — obvious, narrow, low-risk work. Inspect relevant context, change, run the smallest meaningful check, stop.
- **Standard** — normal bugs, features, reviews, refactors, multi-file work, material UI.
- **Critical** — auth/authz, money, sensitive data, destructive state, migrations, concurrency, deployment/recovery. Make invariants/failure paths explicit and use stronger evidence.

Do not turn simple work into ceremony because this skill is active.

## 2. Bind completion to the current target

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

Use the narrowest level that covers the **whole explicit request**, not the easiest subset. For multi-part work, map each requested outcome to an obligation before building; use the existing plan or task notes, not a new tracking system. A completed slice is progress: continue through the remaining authorized obligations. Local completion never implies a higher level.

`STOP` = no Required work remains for the current target.  
`SHIP` = only an explicitly evaluated RELEASE target that is actually release-ready.

Read `references/project-compass.md` only when target level or finish-line scope is genuinely ambiguous.

## 3. Respect authority

Follow:

1. system/safety/tool constraints;
2. explicit current user intent;
3. applicable repository instructions and canonical product/policy/security/legal/architecture/design sources;
4. authoritative work-control/spec state when adopted;
5. actual source/contracts/schema/runtime/tests/current repository state;
6. relevant domain guidance and current official docs;
7. external examples/discussion.

Resolve material conflicts; do not silently choose the convenient source. Do not invent a second roadmap, backlog, scheduler, repository-delivery policy, or product truth.

## 4. UNDERSTAND

Before material work:

- inspect the strongest relevant project truth and actual affected implementation;
- map enough sibling surface to avoid obvious blind spots;
- cheaply check whether the requested capability/invariant already exists and works;
- distinguish facts from assumptions and revalidate stale issues/TODOs against current state;
- ask only when a genuinely unresolved product/authority choice materially changes the outcome.

Do not rewrite working code to create activity.

## 5. PLAN until closure, then build

Planning closes when:

- the finite outcome and material affected boundaries are understood;
- important positive/negative requirements are known;
- no high-impact unknown currently makes implementation premature;
- at least one credible oracle can judge success.

Then BUILD. Do not keep browsing, brainstorming, or decomposing merely to increase confidence.

## 6. BUILD the smallest coherent change

Prefer:

```text
existing mechanism
→ simplify/fix it
→ existing platform/framework capability
→ suitable existing dependency
→ smallest justified new implementation
```

Every changed hunk must serve the target, a necessary dependency, or cleanup caused by the same change.

Avoid speculative abstractions, duplicate helpers/state, compatibility debris, future-proof frameworks, unrelated cleanup, and hypothetical-scale infrastructure.

When repository mutation was requested and write access exists, modify the real repository. Commit/push/release behavior follows active repository policy. Ordinary code changes do not authorize production deploy, destructive remote-data changes, force-push/history rewrite, purchases, or external communications.

## 7. Tests and probes are evidence, not output volume

Before adding a test, identify the missing evidence and check whether an existing verifier exercises that scenario. A reversible low-impact edit usually needs an existing check or direct inspection, not a new permanent test. Read `references/cleanup-and-tests.md` before adding durable test machinery or replacing a tested path.

Classify new checks as:

- **TEMPORARY PROBE** — reproduction/diagnostic aid; normally remove before completion.
- **DURABLE REGRESSION TEST** — protects a stable user-visible contract, invariant, protocol, security boundary, or historically important failure mode.

A durable test needs a clear counterfactual: if the protected fault returns, it fails for the right reason.

Do not preserve tests merely to freeze mutable DOM/CSS/theme/token values, class/file/helper structure, mocks, implementation details a legitimate refactor may change, or behavior already guaranteed by stronger checks.

Prefer behavior/integration evidence over mock-heavy duplication when the boundary matters. For bugs, use the same reproduction before/after when practical.

Do not weaken a test or expected result merely to turn a failure green; resolve whether implementation or the accepted contract is wrong. After sufficient checks pass, broaden verification only for a concrete unresolved risk or required gate.

## 8. JUDGE the claim, not the command

For each Required claim:

1. choose the cheapest credible oracle capable of falsifying it;
2. run/inspect it;
3. confirm the intended scenario actually ran;
4. inspect semantic output, not just availability, exit 0, or generated PASS text;
5. record material coverage limits.

Use the modality appropriate to the claim: runtime/behavior for behavior, authoritative state for money/auth, rendered evidence for visual claims.

Evidence invalidated by later relevant source/config/schema/provider changes becomes **STALE**. Never report an unrun check as passed.

Read `references/evidence.md` for substantial verification and `references/control-plane.md` for release/exact-candidate or external-orchestrator concerns.

## 9. CLEAN the changed surface

Before completion, remove task-caused residue:

- temporary probes/debug scripts/logging;
- scratch/generated artifacts and abandoned variants;
- dead components/helpers/imports/exports;
- obsolete tests/fixtures/config/flags;
- superseded implementation paths;
- stale comments/docs created by replaced behavior.

For redesign/refactor/replacement work, deletion is expected when the new path genuinely supersedes the old one.

Use a change-budget audit only as a diagnostic:

```text
files added/removed
affected files
net code growth
new dependencies/abstractions/durable tests
obsolete path removed?
```

Unexpected permanent growth must trace to a real requirement; LOC/test count is never a success metric.

## 10. BREAK only when it adds independent evidence

For material/high-risk work or subjective design, a fresh bounded reviewer can challenge false completion.

BREAK asks only: **is the current target falsely considered complete?** It is not a repo-wide bug hunt.

Promote a concern to Required only with concrete evidence: reproducible failure, contradiction with authoritative truth, directly observable counterexample, or violated invariant/acceptance clause.

If confirmed: diagnose → bounded repair → re-JUDGE affected claims → CLEAN affected residue. Do not run endless review loops.

Read `references/break.md` for substantial/critical passes.

## 11. Findings are not automatically work

Classify new findings against the target:

- **REQUIRED** — target cannot honestly close without it.
- **RECOMMENDED** — meaningful, not a blocker.
- **OPTIONAL** — useful, low leverage.
- **DEFERRED** — intentionally postponed.
- **IRRELEVANT** — no material impact.

Do not silently expand scope. More possible improvement does not mean the current target is unfinished.

## 12. Domain skills remain domain owners

Load a domain skill only when materially relevant, for example material UI/UX → `design-pipeline`.

Use one HOST. Do not stack competing generic execution/planning hosts or overlapping craft providers merely for more quality.

When a domain skill is active, share the same target/contract; let it define specialty quality/evidence; return findings to this HOST for target-relative triage; do not let it silently widen scope.

## 13. Completion predicate

Complete only when:

```text
Required obligations = 0
AND required evidence is current
AND cleanup obligation is satisfied
AND material changed hunks are accounted for
AND repository delivery obligations are satisfied
```

Before claiming completion, reconcile the original request against actual changes, evidence, and delivery state. A required failed, unknown, stale, or blocked obligation means **PARTIAL / BLOCKED**, even if the code is written. Report the concrete gap; a blocker explains an incomplete handoff, it does not satisfy the obligation. Do not call an unpushed change delivered remotely. Continue recoverable authorized work instead of asking whether to finish it.

Then STOP. Do not launch another broad audit because further improvement is theoretically possible.

For material reports distinguish what was **Checked / Sampled / Inferred / Not checked**. Never let the completion claim exceed the evidence scope.

> Close the user's finite target with the smallest coherent change and strongest proportionate evidence, without manufacturing progress through extra code, tests, files, abstractions, or endless review.
