# mca_unsafe

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#4']

## Statement

B_C(a_safe - 1) > B*: cap above 1-rho-2^-9 (proved) + witnesses at the adjacent grid point (unsafe_at_crossing).

## Ledger (migrated notes)

PROMOTED red -> amber (ring-1 assembly sweep 2026-07-04): see assembly_sweep_ring1.md + the pinned manifest entry.

FALSE-GREEN CASCADE CORRECTION 2026-07-26: `zone_b` is retained as evidence
for constructing the row payload, not as a duplicated unconditional premise.
The live open dependency is the corrected `unsafe_at_crossing` implication.
