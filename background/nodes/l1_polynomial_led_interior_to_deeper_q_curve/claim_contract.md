# Claim contract - L1 polynomial-led interior cells are deeper-Q curves

## Inputs

- base-field domain and polynomial-led received word of degree `m+e`;
- `1<=e<=k` and `m>k`;
- complete-agreement gcd guard.

## Outputs

- explicit injective curve `theta_z:B^e->B^(w+e)`;
- exact disjoint decomposition into guarded depth-`w+e` Q fibers;
- exact ambient-density cancellation under a deeper-Q bound;
- explicit `|B|^e` additive/rounding cost.

## Consumer rule

Route every below-cap polynomial-led interior cell to depth-uniform Q before
posing an independent BC bound.  Retain the gcd guard inside each slice.  A
finite proof must control curve occupancy or explicitly pay the additive
`|B|^e` term; it may not erase it by average-density algebra.

## Nonclaims

No result is asserted for nonconstant minimal vectors or `e>k`.  No Q
flatness, curve equidistribution, or finite budget fit is proved.

## Falsifier

A valid codeword outside the curve union, duplicate slices, a curve point
whose reconstructed product has degree at least `k`, a retained support with
an extra agreement, or a bound omitting the additive slice cost.
