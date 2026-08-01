# Attack routes (round-3 escalation targets, from the r3b report sec. 6)

1. Octave-31 census completion (199 rows; 4 rows need a compute-law
   amendment or contributor run — >16GiB / longer ceiling at q > 4.05e9).
2. The full-ledger lever (drop w_max entirely) if any extended zone slot
   resists.
3. A quantitative iid-approximation theorem under v_2(q-1) large — the bulk
   proof lead; 918552577 is the worked example of accident-vs-ledger
   cancellation.
4. Gated L=2: a proof-side level-uniformity argument is the only route
   (exact reach is impossible).

## [2026-08-01] The 256-basis factorisation is banked as evidence

`dli_c1_256_block_basis_factorization` proves that every official level's
odd-moment matrix consists of 256 invertible blocks `A_a=D_aF`.  Each block
Fourier marginal is exactly iid, but all cross-block dependence lies on the
single deterministic orbit `C_a=M^aC_0`.  Future attacks must analyze that
orbit; marginal iid estimates, prime censuses, q-sized dynamic programs,
and top-level `v_2` surplus arguments do not address the remaining claim.
