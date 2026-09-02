# Harness v2 evaluation

Routing/composition fixtures answer **what should activate**, not whether the harness improves real work.

Run deterministic repository checks:

```bash
python scripts/harness_eval.py check
```

This validates `VERSION`, skill metadata versions, JSON fixture shape, unique case IDs, the single-HOST invariant, and the one-primary-craft-provider invariant where encoded.

## Real outcome evaluation

Do not claim Harness v2 is better from prompt inspection or routing fixtures alone. Run representative tasks repeatedly with:

- **baseline** — the comparison setup you actually want to beat;
- **candidate** — the changed harness/version.

Record observed outcomes using the shape in `outcome-runs.example.json`, then summarize:

```bash
python scripts/harness_eval.py outcomes path/to/real-runs.json
```

The script does not call a model or invent task outcomes. The agent/model environment under evaluation must produce the actual runs and evidence.

Track dimensions separately:

- behavioral/task success;
- premature/false completion;
- user corrections;
- unnecessary permanent files/helpers;
- unnecessary durable tests/fixtures;
- obsolete/temporary residue;
- functional/accessibility/responsive regressions;
- UI pairwise preference and direction/reference fidelity when applicable;
- tool calls, latency/cost, and variance.

Do not collapse these into one universal quality score.

## Provider drift

`providers.json` records reviewed upstream refs for version-sensitive optional providers. Check GitHub-backed providers with:

```bash
python scripts/harness_eval.py provider-drift
```

Exit code `2` means at least one reviewed ref differs from the upstream default-branch HEAD. Drift is not an instruction to auto-update: re-review only when the provider is actually needed, then update its reviewed ref/version deliberately. Network/API failure exits `3`.

## Test-quality sampling

For sampled new durable tests, verify that each:

- protects a stable contract/invariant;
- would fail when the protected fault returns;
- does not merely duplicate a stronger verifier;
- does not block a legitimate behavior-preserving refactor.

When adding a durable harness rule, use ablation thinking: if removing it does not repeatedly worsen representative outcomes, simplify, move it to conditional guidance, or delete it.

Do not use raw test count, coverage growth, one attractive demo, or routing success as proof that the harness is better.
