# Claim contract

## Claim

No pair-feasible `N=256`, folded-profile `(3,4,0)`, `V=60` collision has
magnitude profile `(4,2,2)`.

## Dependencies

- `e1_n256_s16_e30_profile_parity_light_reduction` supplies the exact profile,
  six-odd light router, and cubic cutoff;
- `e1_n256_proper_conductor_collision_exclusion` removes the four dilated
  exceptional vectors;
- `collision_norm_criterion` converts the exact primitive norm bound into
  collision exclusion.

## Consumer effect

The E30 residual contracts from three six-odd profiles to `(6,6)` and
`(5,4,1)`.

## Nonclaims

- no exclusion of `(6,6)` or `(5,4,1)`;
- no closure of `V=60` or a lower variance;
- no claim that the unrestricted structured relaxation is below 1087.

## Falsifier

A missing odd difference mask, a compatible assignment above 1087 outside
the three printed exceptions, an omitted actual vector in an exceptional
orbit, or a primitive exceptional norm at least `2^250` refutes the claim.
