# Evidence, Gates, and Capability Health

## Evidence hierarchy
Prefer evidence closer to reality:
1. runtime behavior / executable result;
2. reproducible integration/state test;
3. deterministic static/structural analysis;
4. rendered state tied to viewport/data/state;
5. source inspection;
6. heuristic reasoning;
7. aesthetic/preference opinion.

Use the evidence modality appropriate to the claim. Critical claims benefit from orthogonal modalities when practical.

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
Evidence is bound to relevant state. If implementation/config/schema/provider behavior affecting a claim changes, prior evidence becomes STALE until re-judged.

## Durable Gates
For long/resumable/orchestrated work, persist Required obligations outside conversation context. Keep the ledger small and outcome-based.

Gate integrity after planning closure:
- adding newly discovered Required gates is allowed;
- strengthening a gate is allowed;
- removing/weakening/reclassifying a Required gate requires recorded justification;
- changing its judge invalidates old evidence;
- checked/manual evidence is not automatically trusted; reproduce runnable checks for consequential claims;
- Required + ABANDONED blocks the target unless residual risk is explicitly accepted.

Do not create a gate framework for trivial work. Prefer existing project commands/test harnesses rather than inventing new infrastructure just to satisfy the process.

## Gate locality and orchestration
For parallel/resumable work, each work unit should expose:
```text
Owns: mutable surfaces it may change
Needs: prerequisites that must already be verified
Tier: required judgment/effort class
```

Use leaf gates for local outcomes, branch gates for integration, and root gates for whole-target evidence. Dispatch all ready disjoint leaves, verify each as it returns, then immediately release dependents whose `Needs` are now satisfied. Whole-project checks belong at branch/root boundaries unless a leaf claim truly requires them.

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