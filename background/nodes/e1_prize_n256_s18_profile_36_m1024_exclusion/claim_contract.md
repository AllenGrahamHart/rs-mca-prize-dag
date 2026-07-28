# Claim contract

## Imported facts

From `e1_prize_n256_s18_profile_36_sharp_product_window`:

- cofactor `1024` forces singleton multiplicity `mu=10`;
- its only residual variances are `{4,6,8,10,12}`.

## New theorem

No profile-`(3,6,S=18)` vector of multiplicity ten has autocorrelation energy
in `{2,3,4,5,6}`. Therefore the cofactor-`1024` collision class is empty.

## Exclusions

1. The enumeration uses affine normalization only for surjectivity; it does
   not divide a count by an assumed free group action.
2. The 68 orbits include every low-chord multiplicity-ten support, not every
   multiplicity-ten support. Supports omitted by the chord gate already have
   energy above six.
3. This node removes one cofactor and does not close the full profile or the
   aggregate pair budget.
4. It makes no claim about the geometrically nonempty `mu=2` branch for
   cofactor `1028`.
