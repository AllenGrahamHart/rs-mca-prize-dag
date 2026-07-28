# Claim contract

## Claim

No pair-feasible `N=256`, folded-profile `(3,4,0)`, `V=56` collision has any
of the eight profiles in the exact E28 reduction.

## Dependencies

- `e1_n256_s16_e28_profile_parity_light_reduction` for exhaustion by 154
  affine light templates;
- `e1_n256_proper_conductor_collision_exclusion` for all 8,266 imprimitive
  cubic exceptions;
- `collision_norm_criterion` for the `M_3<=658` branch and the `2^250` norm
  threshold.

## Output supplied

Together with the exact E28 reduction, this closes the `V=56` endpoint.

## Scope exclusions

- no exclusion at `V<=54`;
- no claim about folded profile `(4,2,0)` or later swap bands;
- no route-wide pair-incidence or image-size theorem.

## Falsifier

A missing affine light orbit, disagreement between the two complete censuses,
an unrecorded `M_3>658` vector, an incorrect conductor, disagreement between
FLINT and PARI, or any primitive exceptional norm at least `2^250` refutes the
claim.
