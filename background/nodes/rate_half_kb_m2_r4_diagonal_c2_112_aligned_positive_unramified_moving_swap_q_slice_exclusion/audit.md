# Audit

The proof uses three independently checkable layers:

1. `kb_c2_112_positive_qslice_symmetric.py` reconstructs the source form and
   audits its relative scale against an independent exact matrix solve.
2. `kb_c2_112_aligned_positive_unramified_flint.py` checks reciprocal
   coefficients before trace descent and regenerates the four residual-minor
   and kernel-conic caches.
3. `kb_c2_112_aligned_positive_unramified_moving_router.py` hash-pins those
   caches, reconstructs every projection and norm, instantiates every
   irreducible exceptional factor as a finite field, and replays surviving
   points in the original four trace equations.

The component replay reports `factors=6`, `rank_candidates=2`, `empty=2`,
`boundary=4`. The off-common replay reports `t_factors=7`,
`p_candidates=8`, `boundary=8`. A nonboundary candidate is a hard failure.

No numerical sampling, characteristic-zero genericity assumption, or
base-field-only root enumeration is used.
