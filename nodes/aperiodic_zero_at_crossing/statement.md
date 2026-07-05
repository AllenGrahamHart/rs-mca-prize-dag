# aperiodic_zero_at_crossing

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#3']

## Statement

At the clean-rate decision candidates (`rho` in `{1/4, 1/8, 1/16}`),
integrality does not kill the aperiodic contribution at `A*` or `A*+1`.
The exactly-zero range begins at `A_zero = A*+2`, after applying `fm1` and the
compiled clean-rate R2 bound.  Thus the adjacency machinery must decide
`A*+1` with a live aperiodic term; it may use exact zero only from `A*+2`.

## Rate Scope Repair 2026-07-06

The logical claim of this node is clean-rate only: `rho` in `{1/4, 1/8,
1/16}`.  The wired R2 premise is `r2_clean_rates`, so the rate-`1/2` thin point
is not proved by this node.  Rate `1/2` remains routed through
`rate_half_band_closure`.

## Ledger (migrated notes)

conditional on r2_rigidity; crystallizes the integrality mechanism discovered in the proved-results survey (pinned row, exactslack, qfloor, FM1 are all exactness-on-a-stratum) | R2 IDENTIFICATION REWIRING (2026-07-04, referee packet in r2_identification.md): the consumer needs R2 only at the admissible rows, where the PROVED compiler/budget chain converts the obligation to the compiled form r2_clean_rates (R_post <= 16n^3) verbatim — the general n^B FM conjecture (r2_rigidity) demoted to ev. The critical path now flows through r2_clean_rates <- the proved xr engines + xr_clean_residual_any_gate <- the smallcore/spread chain <- THE TERMINAL CLUSTER — the dichotomy/A3/C1 campaign is now visibly the safe side's aperiodic engine.
