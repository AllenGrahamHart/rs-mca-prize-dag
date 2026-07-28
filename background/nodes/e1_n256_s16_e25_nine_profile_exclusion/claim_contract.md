# Claim contract

## Claim

No pair-feasible `N=256`, folded-profile `(3,4,0)`, `V=50` collision has any
of the nine profiles in the exact E25 reduction.

## Dependencies

- `e1_n256_s16_e25_profile_parity_light_reduction` for exhaustion by 111
  affine one-diameter light templates;
- `e1_n256_proper_conductor_collision_exclusion` for all 14,296 imprimitive
  cubic exceptions;
- `collision_norm_criterion` for the `M_3<=13` branch and the `2^250` norm
  threshold.

## Output supplied

Together with the exact E25 reduction, this closes the `V=50` endpoint.

## Scope exclusions

- no exclusion at `V<=48`;
- no claim about folded profile `(4,2,0)` or later bands;
- no claim that the cubic majorant remains useful below `V=50`.

## Falsifier

A missing affine light orbit, disagreement between the complete censuses, an
unrecorded `M_3>13` vector, an incorrect conductor, disagreement between
FLINT and PARI, or any primitive exceptional norm at least `2^250` refutes
the claim.
