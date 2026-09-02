# Harness v2 evaluation

The composition cases in this directory test routing expectations only. They do not prove that the harness improves real task outcomes.

For quality claims, compare repeated baseline and candidate runs on representative tasks from different repositories.

Evaluate dimensions separately:

- task/behavioral success;
- premature completion and missed required work;
- number of user corrections;
- unnecessary permanent files/code/helpers;
- unnecessary durable tests/fixtures;
- obsolete or temporary residue left behind;
- functional/accessibility/responsive regressions;
- UI pairwise human preference;
- design-direction/reference fidelity when applicable;
- tool calls, latency/cost, and variance across runs.

For sampled new durable tests, check that each protects a stable contract, would fail when the protected fault returns, does not merely duplicate a stronger verifier, and does not block a legitimate refactor that preserves behavior.

When adding a durable harness rule, use ablation thinking: if removing the rule does not repeatedly worsen representative outcomes, simplify it, move it to a conditional reference, or remove it.

Do not use one universal quality score, raw test count, coverage growth, or one attractive demo as proof that the harness is better.
