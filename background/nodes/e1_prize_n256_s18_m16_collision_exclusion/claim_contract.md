# Claim contract

## Claim

The cofactor `m=16` class is empty for the prize-envelope `N=256` profile
`(4,2,0)`.

## Dependencies

- `e1_prize_n256_s18_m16_high_variance_exclusion` supplies the exact residual
  variance window and inherits the profile, norm equation, and prize interval.

## Scope fences

1. This theorem excludes only cofactor `m=16`.
2. It does not exclude the remaining cofactors `m=2` or `m=4`.
3. The normalized vector count is not an unoriented collision-edge count.
4. No weighted pair-budget bound is inferred from `540332`.
5. The 64-bucket fingerprint is a reproducibility certificate for two exact
   streams, not a substitute for the pinned enumerators and resultant code.
