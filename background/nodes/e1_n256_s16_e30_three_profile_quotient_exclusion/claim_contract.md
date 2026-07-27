# Claim contract

## Claim

No pair-feasible `N=256`, folded-profile `(3,4,0)`, `V=60` collision has
profile `(0,3,2)`, `(6,2,0,1)`, or `(3,0,3)`.

## Dependencies

- `e1_n256_s16_e30_profile_parity_light_reduction` for the exact residual
  profiles and `M_3=1087` cutoff;
- `collision_norm_criterion` for nonzero norm divisibility and the small-field
  transfer.

## Nonclaims

- no exclusion of `(6,6)`, `(2,7)`, `(5,4,1)`, `(1,5,1)`, or `(4,2,2)`;
- no exclusion of `V<=58` or any other folded profile;
- no promotion of either universal target.

## Falsifier

A valid layer allocation omitted by the census, an incorrect objective upper
bound, an actual named-profile vector with `M_3>1087` in either quotient
chamber, or failure of the `4Z` small-field bound refutes the claim.
