# Claim contract

## Inputs

- An official prize row and high band-proper depth.
- A deficient stacked window matrix.
- At least one maximal depth-`d` pair, so its joint error support has
  exactly `r'=n-k-d` points.
- The proved pointwise syzygy law from
  `xr_deficient_window_rational_direction_payment`.

## Outputs

- Projective rank one of the complete left kernel over `F(X)`.
- The coprime primitive pair and multiplier-space normal form `(PP1)`.
- Exact forced-root, dimension, affine-family, and core-intersection bounds.
- Empty forced-root residual below `ceil((2h+2)/3)`.

## Exclusions

- No count of maximal locators or parameters `tau`.
- No identification with P0, quotient, common-GCD, or upstream BC/SP.
- No application of a one-parameter locator-pencil theorem.
- No statement when the maximal family is empty, because the desired count
  is then already zero.
