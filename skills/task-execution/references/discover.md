# DISCOVER

DISCOVER asks: **What material part of the system is absent from the current acceptance model?**

It is milestone-only. Do not run it after every small edit.

## Triangulate three realities
### Intent
User goals, product source of truth, policy, design, architecture, accepted decisions.

### Structure
Routes, pages, APIs, schemas, jobs, events, permissions, state machines, integrations, code paths.

### Behavior
Browser/API/runtime behavior, tests, logs/traces, reachable states, failure/recovery paths.

## Reconciliation findings
- intent exists, structure missing → possibly missing implementation;
- structure exists, intent missing → unmodeled capability;
- structure exists, behavior unreachable/broken → implementation/runtime gap;
- behavior exists but neither intent nor structure model explains it → undocumented/emergent behavior.

Every candidate must cite structural/runtime/authoritative evidence.

DISCOVER does not silently enlarge the Current Target. Return findings to Project Compass for Required/Recommended/Optional/Deferred/Irrelevant triage.