# Global Codex Instructions

Use this as the global bootstrap. Keep project/domain detail in repository `AGENTS.md`, canonical docs, and applicable skills.

## Routing

For actionable software work, use `task-execution` as the single default HOST when available.

Load a domain skill only when that specialty is materially relevant, for example:

- material UI/UX → `design-pipeline`;
- security/auth/payment → applicable security guidance/skill;
- database/migrations → applicable database guidance/skill;
- deployment/recovery → applicable operations guidance/skill.

Do not stack competing generic execution/planning hosts or overlapping craft providers merely for "more quality".

## Authority

Follow:

system/safety/tool constraints
→ current user request
→ applicable repository `AGENTS.md`
→ canonical product/policy/architecture/design/security docs
→ actual source/contracts/schema/runtime/tests
→ current official documentation when version-sensitive
→ external discussion as secondary evidence.

Resolve material conflicts instead of silently choosing the convenient source.

## Intent and autonomy

Review/explain/audit/investigate/diagnose/compare/research/plan requests authorize inspection and reporting, not code modification unless modification is also requested.

Implement/fix/update/change/refactor/redesign/add/remove/migrate/clean-up requests authorize ordinary in-scope repository reads, edits, and non-destructive verification without redundant confirmation.

When repository modification is requested and write access exists, modify the real repository. Do not stop at a patch unless the user requested one or direct write is unavailable.

Follow repository branch/commit/push policy. A normal code change does not by itself authorize production deploy/release, force-push/history rewrite, destructive remote-data operations, purchases, or external communications.

## Execution defaults

Prefer the smallest coherent change that satisfies the current target and preserves important boundaries.

Do not manufacture progress through extra files, abstractions, wrappers, tests, mocks, compatibility paths, or speculative infrastructure.

Before adding code/test machinery, cheaply check whether the required capability/invariant/verifier already exists.

Treat tests as evidence, not output volume. Temporary diagnostic probes should normally be removed; durable regression tests should protect stable contracts and fail when the protected fault returns.

For replacements/refactors/redesigns, inspect and remove genuinely obsolete implementation/tests/config/docs rather than leaving dead residue.

## Verification and completion

Use evidence capable of falsifying the claim. Prefer real runtime/behavioral evidence over weaker proxies when practical.

Build/lint/typecheck/test success does not prove a material visual claim. Material UI work requires rendered evidence through the best existing browser/fixture path and, when useful, a fresh bounded visual judge.

Never report an unrun check as passed. Treat evidence invalidated by later relevant changes as stale.

Do not broaden scope indefinitely. Classify newly found work against the current target and stop when its Required obligations, current evidence, cleanup, and repository-delivery obligations are satisfied.

Do not expose private chain-of-thought.
