# Claim contract

## Claim

No pair-feasible `N=256`, folded-profile `(3,4,0)`, `V=54` collision has any
of the six profiles in the exact E27 reduction.

## Dependencies

- `e1_n256_s16_e27_profile_parity_light_reduction` for exhaustion by eight
  affine light templates;
- `e1_n256_proper_conductor_collision_exclusion` for all 1,596 imprimitive
  cubic exceptions;
- `collision_norm_criterion` for the `M_3<=443` branch and the `2^250` norm
  threshold.

## Output supplied

Together with the exact E27 reduction, this closes the `V=54` endpoint.

## Scope exclusions

- no exclusion at `V<=52`;
- no claim about folded profile `(4,2,0)` or later swap bands;
- no route-wide pair-incidence or image-size theorem.

## Falsifier

A missing affine light orbit, disagreement between the two complete censuses,
an unrecorded `M_3>443` vector, an incorrect conductor, disagreement between
FLINT and PARI, or any primitive exceptional norm at least `2^250` refutes the
claim.
