# Audit

- Pairing 6 reverses which signed `DE` value enters the `u` and `v` paired
  quadratics; the verifier reconstructs those two cuts independently.
- The omitted sum remains `(d+e)^2`, so `H=de*(u+v)^2-suv` is unchanged.
- The pseudo-remainder is division-free and includes the final leading
  coefficient before norming.
- Every norm and inverse-guard numerator/denominator root is directly lifted.
- All 96 `f` rows are nonzero and fail the colored pair; no target boundary
  is used in the exclusion.
- `xi=1` transport is exact at fixed matching 6 and does not identify lanes.
