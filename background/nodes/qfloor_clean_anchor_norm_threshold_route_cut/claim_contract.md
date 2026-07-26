# Claim contract

## Inputs

- the six clean candidate agreements and budgets from the pinned consumption
  replay;
- the exact scope of `qfloor_exact`;
- the official field cap `q<2^256`.

## Output

An exact proof that `qfloor_exact` is inapplicable at all six clean candidate
predecessors.

## Guards

1. `N'=n/(m-k)` is derived from the unsafe predecessor, not rounded.
2. `ell'=rho N'+1`; the support complement `N'-ell'` has the same binomial
   count but is not substituted into the norm expression without symmetry.
3. The theorem requires the strict inequality `p>(2ell')^(N'/2)`.
4. A raw class count is not a distinct-value or distinct-slope count.

## Nonclaims

- The quotient value set is not small.
- The candidate predecessor is not safe.
- E1 injectivity, exceptional-prime control, or averaged occupancy is not
  resolved.
