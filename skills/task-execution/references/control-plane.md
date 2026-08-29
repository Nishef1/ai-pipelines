# Control Plane Boundaries

Use when project state, issue tracking, specs, milestones, external orchestration, multi-agent scheduling, repository delivery policy, or release state is involved.

## Why this boundary exists

Long-running coding agents often fail by collapsing several different questions into one:

```text
What should the product become?
What work has been accepted?
What is ready to execute?
What should run now?
How should this task be implemented?
How is the repository change delivered?
What evidence proves it?
Is a release ready?
```

No single task harness should silently own all of them.

## Concern ownership

### Product authority
Owns product intent, user value, release scope, strategic priority, and acceptance policy.

Typical sources: explicit user decisions, canonical product docs, approved strategy/requirements.

### Work-control authority
Owns accepted work items, dependency relationships, assignment, and lifecycle/status when the project has an authoritative tracker.

A tracker state is a work-management claim, not proof that runtime behavior is correct.

### Scheduler / orchestrator
Owns dispatch, concurrency, retries, workspace lifecycle, and work-item transitions when an external orchestrator is active.

Use **one scheduler** for the same work graph. Task Execution may parallelize child units only when it actually owns scheduling inside the current target.

### Repository delivery policy
Owns the applicable branch, commit/push expectations, PR requirements, and other repository-delivery rules.

An explicit user request to modify repository code/files authorizes the ordinary in-scope source mutation needed to carry out that request when write access exists. A remote Git provider does not make the source edit a new approval boundary by itself.

If user/project policy says completed repository changes are committed and pushed, those actions are part of delivery and should not trigger a second confirmation request.

This does **not** automatically authorize production deployment/release publication, force-push/history rewriting, destructive remote data changes, purchases, external communications, or unrelated repository/account mutations.

### Task Execution
Owns understanding, planning closure, bounded implementation, evidence, target-relative triage, and stopping for the currently selected/assigned target.

It must not invent a second backlog, dependency graph, project roadmap, or repository delivery policy to compensate for missing context.

### Domain skills
Own specialty-specific criteria, tools, and domain evidence: design, security, database, deployment, reliability, and similar concerns.

### Evidence layer
Runtime behavior, tests, browser/render state, logs, data, schemas, actual repository content, and other reproducible observations determine what is actually supported.

### Release judgment
Consumes release requirements plus current integration/evidence. It is not implied by closing a task or feature.

## One authoritative source per concern

Prefer:

```text
one product truth per product concern
one authoritative work tracker
one scheduler/orchestrator
one repository delivery policy
one current-target execution host
```

Do not maintain a prose shadow copy of the same project state unless the project deliberately adopts and reconciles it.

Avoid patterns such as:

```text
issue tracker + hand-maintained STATE.md + separate agent backlog
external scheduler + task-execution project scheduler
spec system + duplicate feature contract in a gate file
requested code change + patch-only handoff despite available write access
```

Local execution gates may reference tracker/spec IDs, but they should store only the evidence needed to close the current target.

## Ready does not mean important

Dependency systems can answer questions like:

- is this work blocked?
- which prerequisites are complete?
- which items can run now?

They do not by themselves answer:

- which user problem matters most?
- which capability belongs in this release?
- which tradeoff is worth making?

Treat `ready`, `unblocked`, or a numeric tracker priority as authoritative only to the extent the project's product/work policy makes it so.

## Reconcile state with reality

Persistent state drifts.

Treat tracker statuses, generated plans, progress logs, gate ledgers, and markdown state as claims that may need reconciliation against:

- current repository state;
- actual runtime behavior;
- tests/integration evidence;
- canonical specs/contracts;
- relevant Git history when historical truth matters.

Do not change a trusted tracker/spec merely because code differs; first determine which source is stale or incorrect.

## Spec systems

When a project adopts a spec/change lifecycle, use it for the behavior contract it owns. Task Execution should consume the current spec/acceptance and verify implementation against it, not rewrite the same contract into another global document.

Feature convergence and release convergence are separate judgments. A feature can satisfy its spec while the release remains incomplete.

## Adapters, not replacement frameworks

If integrating a project-control provider, prefer a thin capability adapter:

```text
read current work
read dependency/readiness state
read acceptance/spec context
optionally update status when authorized
```

Keep provider-specific commands and volatile behavior outside the host core where possible.

External writes to trackers, issue systems, or orchestrators remain subject to the user's/project's authorization policy. Do not generalize that restriction to ordinary source-file edits that were already explicitly requested.

## When no control plane exists

Do not respond by inventing a full project-management framework.

Keep only enough local state to close the current target:

```text
Target Level
Current Target
Finish Line
Required remaining
Current evidence
Open assumptions/conflicts
```

If repeated work demonstrates a genuine need for durable project control, recommend adopting or designing that capability as a separate decision rather than silently growing Task Execution into it.