# Audit - petal reserve rich-fiber reduction

## Checked axes

1. The threshold is `k+ell-1`, so removing `d` core agreements requires
   `ell+d` non-core agreements, not `ell+d-1`.
2. The background bound `r<=d` uses `W!=0`; maximality `b<ell` is exactly
   what excludes `W=0` from the list.
3. Pigeonhole is over source petals, not over rational values in the ambient
   field.
4. Distinct source labels identify each touched petal with one value fiber of
   `W/L_D`.
5. The asymptotic conclusion uses the explicit lower cutoff
   `sigma=Omega(n/log n)`, not the entropy inequality alone without a
   polynomial-field hypothesis.

## Remaining attack

Bound or structurally own rational functions whose source-coupled value fiber
has size at least `ell^2/(n-k+1)` on one petal, while summing over all defects
and first-match layouts.
