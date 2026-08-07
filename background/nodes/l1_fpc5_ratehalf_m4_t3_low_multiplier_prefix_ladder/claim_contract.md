# Claim contract

## Input

One LS6 atom with multiplier degree `a<=e<=ell-a`.

## Output

An exact disjoint union of `Q_0^(e-a)` ordinary locator-prefix cells of depth
`ell+e-1`, with exact average-scale cancellation to effective depth
`ell+a-1`.

## Preserved

- monicity and exact locator degree;
- one fixed source/triple/defect/cross-ratio atom;
- a bijection between flat points and `(Q,R)` coordinates.

## Nonclaims

- prefix maximum equals its average;
- field-many cells may be summed without the deeper-prefix gain;
- the split or LS6 gcd filters are automatic;
- high multiplier degree is covered.
