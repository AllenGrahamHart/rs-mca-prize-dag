# Claim contract

## Claim

No pair-feasible `N=256`, folded-profile `(3,4,0)`, `V=52` collision has any
of the six two-odd profiles in the exact E26 reduction.

## Dependencies

- `e1_n256_s16_e26_profile_parity_light_reduction` for exhaustion by 87
  affine light templates;
- `e1_n256_proper_conductor_collision_exclusion` for all 9,564 imprimitive
  cubic exceptions;
- `collision_norm_criterion` for the `M_3<=228` branch and norm threshold.

## Output supplied

The live `V=52` residual consists only of four six-odd profiles:
`(6,5)`, `(5,3,1)`, `(4,1,2)`, and `(6,1,0,1)`.

## Scope exclusions

- no exclusion of those four six-odd profiles or any `V<=50` chamber;
- no claim about folded profile `(4,2,0)` or later swap bands;
- no route-wide pair-incidence theorem.

## Falsifier

A missing two-odd light orbit, disagreement between the complete censuses, an
unrecorded `M_3>228` vector, an incorrect conductor, disagreement between
FLINT and PARI, or any primitive norm at least `2^250` refutes the claim.
