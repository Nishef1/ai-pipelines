# Harness v2 evaluation

Routing/composition fixtures answer **what should activate**, not whether the harness improves real work.

Run deterministic repository checks:

```bash
python scripts/harness_eval.py check
```

This validates `VERSION`, skill metadata versions, JSON fixture shape, unique case IDs, the single-HOST invariant, and the one-primary-craft-provider invariant where encoded.

It does not execute fixture prompts or verify their expected behavior. The CLI labels this limitation explicitly. Run the outcome reporter's behavioral regression checks with `python -m unittest discover -s tests -v`; these protect input handling and reporting, not model quality.

## Real outcome evaluation

Do not claim Harness v2 is better from prompt inspection or routing fixtures alone. Run representative tasks repeatedly with:

- **baseline** — the comparison setup you actually want to beat;
- **candidate** — the changed harness/version.

Record observed outcomes using the shape in `outcome-runs.example.json`, then summarize:

```bash
python scripts/harness_eval.py outcomes path/to/real-runs.json
```

The script does not call a model or invent task outcomes. The agent/model environment under evaluation must produce the actual runs and evidence.

The shipped example is marked `example_only` and is rejected by `outcomes`. Create a separate input from observed runs; deleting the flag does not turn example numbers into evidence. Summaries are descriptive, do not authenticate the submitted evidence, and expose missing repeated comparisons. Mixed UI preferences across repeated runs are reported as mixed, not rejected or converted into a unanimous win.

### Testing the reported Sol failure modes

Use the same actual model identifier, settings, tools, starting repository, brief, and resource budget for baseline and candidate; record these with the evidence. Do not infer capabilities from a UI model label or compare different models and attribute the result to the harness. Keep raw transcripts, diffs, check outputs, and relevant captures outside the shipped skill. Let a reviewer inspect them against the original request rather than the builder's completion summary.

Use the completion/composition cases as bounded scenarios: multi-part work, a failed delivery, an uncovered behavioral bug, a copy-only fix, and an expressive RTL marketplace redesign. Evaluate which requested outcomes actually occurred, whether new tests protect a missing contract, and whether the actual render follows the brief. Repeated blind visual comparisons with human judgment are preferable for taste claims. The fixtures and current reporter tests are not these model runs.

### Research basis and limits

[OpenAI's harness engineering account](https://openai.com/index/harness-engineering/) supports keeping instructions navigable and making runtime evidence accessible. [Anthropic's application-harness experiments](https://www.anthropic.com/engineering/harness-design-long-running-apps) describe overly positive self-evaluation, the benefit of separate evaluation, and increasing cost and complexity across iterations. These motivate bounded evidence review here, not mandatory multi-agent loops, a universal aesthetic, or claims about GPT-5.6 Sol specifically. No repeated Sol baseline/candidate results are bundled with this patch.

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
