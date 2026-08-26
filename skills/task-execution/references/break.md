# BREAK

BREAK is an adversarial falsification pass, preferably in a fresh context. It is not a request to invent more work.

## Inputs
- Task Contract / acceptance obligations
- resulting artifact/current implementation
- authoritative project context
- relevant JUDGE evidence/interfaces

Avoid builder rationale unless it is itself evidence.

## Valid confirmed finding
Require at least one:
- reproducible failure;
- direct contradiction with authoritative truth;
- executable/observable counterexample;
- deterministic violation of an invariant or acceptance clause.

Plausible concern without evidence is a risk/question, not a confirmed defect.

## Two useful attacks
1. **Claim attack** — can a modeled requirement be falsified?
2. **Boundary attack** — can the implementation escape a negative boundary (authorization, data integrity, recovery, concurrency, etc.)?

Missing-scope discovery belongs to DISCOVER, not BREAK.

## On failure
Counterexample → diagnosis → bounded repair → JUDGE affected claims → fresh BREAK if consequence warrants.