# Evidence, Gates, and Capability Health

## Evidence hierarchy

Choose evidence by the claim, not a universal ranking:

| Claim | Relevant evidence |
| --- | --- |
| Workflow or persistence works | Exercise the flow and inspect its resulting authoritative state |
| Implementation builds or satisfies types | Existing build/type checks |
| Layout matches the chosen direction | Inspect comparable actual and reference renders at relevant states/viewports |
| Users understand the flow | User observation; label expert assessment as heuristic when that is all that exists |
| Aesthetic preference improved | Contextual pairwise visual judgment; identify who judged it |

Source inspection and reasoning can guide these checks but cannot replace a missing observation. Critical claims benefit from orthogonal modalities when practical.

Do not let the completion label exceed the evidence scope. Task-level evidence does not become feature, milestone, or release evidence by association.

## Coverage honesty

Always distinguish:

```text
Checked:
Sampled:
Inferred:
Not checked:
```

No finding in a sampled subset is not evidence of absence elsewhere.

## Evidence freshness

Evidence is bound to relevant state. If implementation/config/schema/provider behavior affecting a claim changes, prior evidence becomes `STALE` until re-judged.

Tracker statuses, progress files, generated plans, and gate ledgers are not exempt. Persistence makes a claim durable, not necessarily true.

## Application legibility

Verification quality is limited by what the agent can actually observe.

If a material claim requires runtime/browser/data/log evidence but the project exposes no reliable way to inspect it:

- mark the claim `UNKNOWN` or coverage degraded;
- do not substitute additional reasoning for missing observation;
- prefer the smallest reproducible improvement that makes the relevant state observable when the benefit justifies it.

Useful project legibility can include stable local startup, deterministic fixtures/test accounts, browser automation, relevant logs, inspectable data/state, and reproducible commands. Do not build an observability platform merely to close a small task.

## Durable Gates

For long/resumable/orchestrated work, persist Required obligations outside fragile conversation context when useful. Keep the ledger **task-local, small, and outcome-based**.

A gate ledger is an execution/evidence cache for the current target. It is not a project roadmap, backlog, spec system, or product source of truth.

Gate integrity after planning closure:

- adding newly discovered Required gates is allowed only when they truly block the current target;
- strengthening a gate is allowed when new evidence reveals a missing invariant;
- removing/weakening/reclassifying a Required gate requires recorded justification;
- changing its judge invalidates old evidence;
- checked/manual/tracker evidence is not automatically trusted; reproduce runnable checks for consequential claims;
- Required + `ABANDONED` blocks the target unless residual risk is explicitly accepted.

If durable state conflicts with current repository/runtime/spec evidence, reconcile the contradiction instead of trusting the persisted prose.

Do not create a gate framework for trivial work. Prefer existing project commands/test harnesses rather than inventing new infrastructure just to satisfy the process.

## Gate locality and orchestration

For parallel/resumable work, each locally scheduled work unit may expose:

```text
Owns: mutable surfaces it may change
Needs: prerequisites that must already be verified
Tier: required judgment/effort class
```

Use leaf gates for local outcomes, branch gates for integration, and root gates for the **current target**. Use release-level gates only when the current target itself is a release.

Dispatch ready disjoint leaves only when Task Execution owns child scheduling. If an external orchestrator owns dispatch/retry/work-item transitions, do not create a competing scheduler; return unit evidence/status to it.

Whole-project checks belong at branch/root/release boundaries only when the claim truly requires them.

Parallel execution does not weaken evidence requirements. Returned evidence is still a cache until the judging layer can reproduce the important check.

## Capability contracts

Describe the required capability independently of provider/tool.

Example:

```text
Capability: rendered interactive checkout verification
Preferred: project Playwright/browser tooling
Fallback: another valid browser path
```

Health means the required operation produced task-relevant evidence. Installed/reachable/exit-0/non-empty are weaker signals, not proof.

Fallback rules:

- established provider first;
- bounded fallback on real failure;
- do not weaken the claim to fit fallback;
- surface degraded coverage if fallback is weaker.

## Final report audit

Re-measure counts/numbers that matter to the report. Never state “all N files/flows/checks” from memory. If not measured, label the number unverified or omit it.

Report completion at the scope actually judged:

```text
TASK | SLICE | FEATURE | MILESTONE | RELEASE
```

`RELEASE READY` requires release-level evidence; `SHIP` is a release action, not a generic evidence status.
