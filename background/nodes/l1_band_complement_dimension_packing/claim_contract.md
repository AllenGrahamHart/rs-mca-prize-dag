# Claim contract - L1 band complement-dimension packing

## Inputs

- an exact level-`m` shell in `2m<=n+k-1`;
- the balanced shifted-lattice coefficient dimension;
- Reed--Solomon pairwise agreement at most `k-1`.

## Outputs

- projective complement-pencil dimension `s=n-2m+k`;
- complement intersections of size at most `s-1`;
- exact integer packing cap `floor(binom(n,s)/binom(n-m,s))`;
- `exp(O(s))` payment at linear complement density;
- polynomial fixed-`s` and subexponential sublinear-`s` ranges.

## Consumer rule

Apply `(CP2)` before invoking BC or enumerating split-pencil profiles.  Remove
every shell whose exact cap fits the allocated numerator, and remove the
sublinear-`s` strip asymptotically only under the printed reserve condition.

## Nonclaims

No row-sharp result is asserted for linear `s`.  The cap is not normalized by
the base-field average and supplies no owner coalescing.

## Falsifier

A nonzero capped coefficient pair with zero first coordinate, two exact
complements sharing `s` roots, an exact-shell count exceeding `(CP2)`, or an
asymptotic absorption claim without `s=o(R log |B|)`.
