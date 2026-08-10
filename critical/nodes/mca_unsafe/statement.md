# mca_unsafe

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#4']

## Statement

B_C(a_safe - 1) > B*: cap above 1-rho-2^-9 (proved) + witnesses at the adjacent grid point (unsafe_at_crossing).

SYMBOL BINDING (round-28 quantifier audit, 2026-08-10 — recorded because it
was load-bearing and unlabelled): `a_safe` here is THE SAME SYMBOL as in the
safe-side node, and this claim is what pins it. The safe-side node's prose
leaves `a_safe` unbound; this statement, together with the root assembly's
requirement to EXHIBIT the crossing, makes `a_safe` the located crossing
index. No pass may re-point `a_safe` at one of the two nodes alone — in
particular a safe point supplied at a bracket end (half distance `3n/4`, or
full agreement `n`) is not a legal value of `a_safe`, because it makes this
claim false or open.

## Ledger (migrated notes)

PROMOTED red -> amber (ring-1 assembly sweep 2026-07-04): see assembly_sweep_ring1.md + the pinned manifest entry.

FALSE-GREEN CASCADE CORRECTION 2026-07-26: `zone_b` is retained as evidence
for constructing the row payload, not as a duplicated unconditional premise.
The live open dependency is the corrected `unsafe_at_crossing` implication.
