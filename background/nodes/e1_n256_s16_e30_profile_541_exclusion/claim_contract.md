# Claim contract

## Claim

No pair-feasible `N=256`, folded-profile `(3,4,0)`, `V=60` collision has
magnitude profile `(5,4,1)`.

## Dependencies

- `e1_n256_s16_e30_profile_parity_light_reduction` supplies the profile,
  six-odd router, and cubic cutoff;
- `e1_n256_proper_conductor_collision_exclusion` removes the 354
  proper-conductor exceptions;
- `collision_norm_criterion` turns the exact 86-vector norm ledger into
  collision exclusion.

## Consumer effect

Profile `(6,6)` becomes the sole live E30 profile.

## Nonclaims

- no exclusion of `(6,6)`;
- no closure of `V=60` or a lower variance;
- no generic theorem for six-odd profiles outside this exact layer ledger.

## Falsifier

A missing odd mask or affine light orbit, an omitted assignment above 1087,
an omitted actual exceptional vector, or a full-conductor exceptional norm at
least `2^250` refutes the claim.
