# Audit

## Claim boundary

The node proves three facts only:

1. first carried layout gives a disjoint exhaustive Top/Post partition;
2. G1 plus K4 bounds Top by the exact weighted atlas census `N_top`;
3. `B_post=n^6-N_top` composes with that cap on the same ledger.

It does not prove `#Post<=B_post`. That inequality remains the finite content
of `pma_wide_residual`.

## Scope checks

- Global owners are removed before layout assignment, so their profile-line
  charges are not subtracted from or duplicated in the primitive `n^6` line.
- The rate-half formula is the exact G1 atlas census, not the older coarse
  `(121/128)n^6` upper bound.
- At the three lower rates G1 proves structural floor-band emptiness, so the
  entire primitive line is available to Post.
- The theorem is finite and `sigma=1`; no asymptotic-reserve allowance is
  inferred.
- Top uses the first carried layout. An existential re-layout would invalidate
  the G1 census and is explicitly excluded.

## Mutation controls

The verifier rejects both tempting accounting errors: allocating the full
`n^6` line to Post at rate half, and replacing the exact top census by a
strictly smaller cap. It also checks the lower-rate empty-band cutoff and the
required DAG dependencies.
