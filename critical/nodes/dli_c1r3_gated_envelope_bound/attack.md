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

## [2026-08-01] The L=1 block-owner ledger localizes the black hole

`dli_c1_l1_block_owner_ledger` proves, using the wired official exclusions
of block relations of weight at most four, that C1-ZERO at `L=1` is exactly

```text
sum_(j<64) [A_j-15*2^(4j)/q] <= 3+1/q.
```

Here `A_j` is the weighted mass of earlier differences landing on the next
four-coordinate target set.  This is an accounting identity, not an excess
bound.  Literal SWIF-4 should not be the sole theorem target: weight-9/10
resonances can perturb individual block contractions while the aggregate
budget may remain valid.  Falsify those resonance channels first, then seek
a bounded-complexity resonance-packet theorem only if diffuse excess
survives.
