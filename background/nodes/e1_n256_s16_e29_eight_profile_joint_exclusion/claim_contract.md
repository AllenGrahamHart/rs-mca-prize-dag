# Claim contract

## Claim

No pair-feasible `N=256`, folded-profile `(3,4,0)`, `V=58` collision has any
of the eight profiles in the exact E29 reduction.

## Dependencies

- `e1_n256_s16_e29_profile_parity_light_reduction` for exhaustion by 111
  affine light templates;
- `e1_n256_proper_conductor_collision_exclusion` for all 3,992 imprimitive
  cubic exceptions;
- `collision_norm_criterion` for the `M_3<=872` branch and the `2^250` norm
  threshold.

## Output supplied

Together with the exact E29 reduction, this closes the `V=58` endpoint.

## Scope exclusions

- no exclusion at `V<=56`;
- no claim about folded profile `(4,2,0)` or later swap bands;
- no route-wide pair-incidence or image-size theorem.

## Falsifier

A missing affine light orbit, disagreement between the two complete censuses,
an unrecorded `M_3>872` vector, an incorrect conductor, disagreement between
FLINT and PARI, or any primitive exceptional norm at least `2^250` refutes the
claim.
