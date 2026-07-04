# aperiodic_zero_at_crossing

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#3']

## Statement

CORRECTED by the margin tables (wave 1, 117/117): integrality does NOT hold at A*+1 — margins log2(n^3 FM) are POSITIVE at A* and A*+1 at ALL ten table rows (+9.6..+243); the exactly-zero radius begins at A_zero = A*+2 everywhere (proved monotone from there, margins -363 .. -1.5e12 bits). So the adjacency machinery must DECIDE A*+1 with a live aperiodic term — R2's constant matters there, and at prize-max rate 1/2 the A*+2 margin is only -12.87 bits (absorbs B <= 3.31: the exponent budget is nearly exhausted at that single point; mirrored on the list side at -12.84). These thin points are QA.4 census objects.

## Ledger (migrated notes)

conditional on r2_rigidity; crystallizes the integrality mechanism discovered in the proved-results survey (pinned row, exactslack, qfloor, FM1 are all exactness-on-a-stratum) | R2 IDENTIFICATION REWIRING (2026-07-04, referee packet in r2_identification.md): the consumer needs R2 only at the admissible rows, where the PROVED compiler/budget chain converts the obligation to the compiled form r2_clean_rates (R_post <= 16n^3) verbatim — the general n^B FM conjecture (r2_rigidity) demoted to ev. The critical path now flows through r2_clean_rates <- the proved xr engines + xr_clean_residual_any_gate <- the smallcore/spread chain <- THE TERMINAL CLUSTER — the dichotomy/A3/C1 campaign is now visibly the safe side's aperiodic engine.
