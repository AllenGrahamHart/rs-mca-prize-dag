# Audit - PMA sigma-one variable-defect exact-hit floor

## Checked axes

1. `a=d+2` is forced by exact agreement `K-d+a=k+1`.
2. The zero-hyperplane count is `L+d+1`: `d` missed-core points, one
   background point, and `L` petal points.
3. Pairwise rational-value collisions are nonzero linear conditions for every
   `d>=1` because constants and `X` lie in the numerator space.
4. Injective labels make the prescribed values distinct; the unused-label
   denominator is `q-1-a`, not `q-a`.
5. Exact support recovers `D`; no auxiliary multiplicity is counted.
6. The near-coset exclusion is uniform in `D`, using the worst possible
   addition of all `a` petal hits to one index-two coset.
7. The Linnik prime is chosen in the class `-1 mod n`, so the order-`n`
   subgroup genuinely generates `F_(p^2)` rather than lying in the base
   field.
8. The corollary is explicitly outside the `sigma=Omega(n/log n)` reserve and
   is not promoted as an `imgfib` counterexample.

## Residual risk

The result imports Linnik's classical theorem, pinned to Xylouris,
arXiv:0906.2749. It does not classify the rich rational-value collisions that
are mandatory at the corrected reserve.
