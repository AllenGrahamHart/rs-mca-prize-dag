# Claim contract

## Claim

Every prize-envelope collision in profile `(4,2,0)` is impossible. Removing
its zero contribution from the binding rate-`1/8` weighted-kernel ledger makes
`(3,6,18)` the maximum-weight remaining profile and raises the conservative
oriented-vector cap from 69,541 to 93,962.

## Dependencies

- `e1_prize_n256_s18_variance_cofactor_windows` supplies the complete prize
  cofactor list and excludes `1538`.
- The six cofactor-exclusion nodes remove `1028,514,256,16,4,2`.
- `e1_low_square_mass_weighted_kernel_dictionary` supplies the exact
  multiplicity formula and pair-budget conversion.

## Scope fences

1. RowC retains all 419 local cofactor classes.
2. Profiles other than `(4,2,18)` are not excluded by this synthesis.
3. The cap 93,962 is sufficient but stronger than the weighted target.
4. No aggregate collision-vector or edge count is proved.
