# Claim contract

## Claim

No pair-feasible `N=256`, folded-profile `(3,4,0)`, `V=52` collision has any
of the four six-odd profiles in the exact E26 reduction.

## Dependencies

- `e1_n256_s16_e26_profile_parity_light_reduction` for exhaustion by 1,234
  affine six-odd light templates;
- `e1_n256_proper_conductor_collision_exclusion` for all 29,206 imprimitive
  cubic exceptions;
- `collision_norm_criterion` for the `M_3<=228` branch and the `2^250` norm
  threshold.

## Output supplied

Together with the exact E26 reduction and the proved two-odd exclusion, this
closes the `V=52` endpoint.

## Scope exclusions

- no exclusion at `V<=50`;
- no claim about folded profile `(4,2,0)` or later swap bands;
- no route-wide pair-incidence or image-size theorem.

## Falsifier

A missing affine light orbit, disagreement between the two complete censuses,
an unrecorded full-conductor `M_3>228` vector, an incorrect conductor,
disagreement between FLINT and PARI, or any primitive exceptional norm at
least `2^250` refutes the claim.
