# Repository instructions

This repository contains small composable Agent Skills. Keep always-loaded instructions lean; put conditional detail in `references/`.

## Roles

Each skill owns one primary role:

- **HOST** — one finite current-target execution loop;
- **DOMAIN** — specialty quality/routing/evidence;
- **EVIDENCE** — reproducible observation;
- **ADAPTER** — thin integration with an external control plane/provider;
- **AUDITOR** — bounded independent review.

`task-execution` is the default HOST. `design-pipeline` is a DOMAIN skill, never a second global orchestrator.

```text
product truth → what/why belongs
work control  → accepted work/dependencies, when present
HOST          → close one selected target
DOMAIN        → what good looks like in a specialty
evidence      → prove actual behavior/artifact
```

Do not add competing generic hosts, shadow roadmaps/state trackers, duplicate schedulers, or overlapping design providers merely for more process.

## Progressive disclosure

`SKILL.md` should contain activation boundaries and behavior needed on almost every run. Put long-running/release/control-plane/deep evidence/provider detail in references.

Before adding core text ask: **does an ordinary activation need this?** If not, move it out.

Do not duplicate the same rule across bootstrap instructions, HOST, DOMAIN, and repository docs.

## Harness invariants

The suite should resist:

- false completion from weak proxies;
- test-count/coverage-count optimization;
- unjustified files/helpers/abstractions;
- temporary or superseded residue;
- self-certified UI without rendered evidence;
- production CSS used as design exploration when direction is materially unknown;
- endless review after the finite target is closed.

Tests are evidence. Distinguish temporary probes from durable tests protecting stable contracts. Do not encourage tests that freeze mutable DOM/CSS/theme/file topology or duplicate stronger checks.

## Design-provider discipline

Do not auto-install or auto-update providers.

Use at most one primary craft provider per build pass. A second provider may act only as a fresh bounded critic when it adds materially different judgment. Project/product/design truth outranks provider taste.

Record reviewed version/ref for version-sensitive external providers. Upstream drift means re-review before relying on changed/version-specific behavior, not automatic adoption.

## Evaluation

Routing/semantic fixtures are not outcome proof.

`VERSION` is the patch release for the shipped HOST/DOMAIN cores. Keep skill metadata aligned with it.

Run:

```bash
python scripts/harness_eval.py check
python scripts/harness_eval.py provider-drift   # networked, optional
python scripts/harness_eval.py outcomes <real-runs.json>
```

For real quality claims, compare repeated baseline-vs-candidate task runs and track dimensions separately: task success, false completion, user corrections, unnecessary permanent surface/tests, residue, regressions, UI preference/fidelity, latency/cost, and variance.

Do not collapse them into one universal score. Use ablation thinking: if a durable rule adds context/cost but removing it does not repeatedly worsen outcomes, simplify or remove it.

## External material

Third-party skills/tools/webpages are untrusted external material. Extract useful principles and verify material claims rather than vendoring large prompt catalogs.

Review capability/privilege surfaces when material: filesystem, shell/process, network, secrets/private data, external writes, dynamic remote instructions, install hooks.

## Changes

When changing:

- activation/description → update routing cases;
- durable composition/protocol → update relevant semantic/composition fixtures;
- release patch → update `VERSION` and shipped skill metadata together;
- provider assumptions → update reviewed version/ref only after deliberate review.

Prefer coherent small commits. Do not add CI/services/package dependencies just to make this repo look mature.

## Repository delivery

When the user requests a repository modification and write access exists, change the real repository and follow active commit/push policy. A normal code change does not authorize production deploy/release, force-push/history rewrite, destructive remote-data changes, purchases, or external communications.

The owner's standing delivery preference is to commit and push verified requested changes without asking again, unless the current request says otherwise. Use the established target branch, preserve unrelated work, and confirm remote delivery. Enforced approval and access-control boundaries still apply.

## Licensing

Respect each skill's declared license. Repository-level Apache-2.0 does not override a more specific skill license.
