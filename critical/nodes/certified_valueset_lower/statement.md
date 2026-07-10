# certified_valueset_lower

- **status:** see dag.json (single source of truth; dag status PROVED) [header retrofit 2026-07-10, catch #69 — was: TARGET]
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#3']

## Statement

For a knife-edge row (specific p): certify |{e1(B) mod p}| > B* by exhibiting a provably all-pairs-distinct class family of size > B*. Collision-monotonicity makes the safe side free; THIS is the entire hard half. Per-prime (almost-all-primes tools do not apply); sampling unreachable at N' >= 128.

## Attack surface

compose pairwise height-certified distinctness (norm < p => no collision) into large families: a packing/coding problem in the swap metric — minimum-swap-distance families whose difference heights stay below p, or a smarter invariant certifying blocks at once

## Falsifier

n/a (a construction target; its absence just leaves knife-edge rows undecided)

## Ledger (migrated notes)

the knife-edge census's difficulty CONCENTRATED into one object; everything else in Tier A is estimates + elementary structure
