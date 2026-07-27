# Claim contract

## Claim

The complete E34 progression template has weighted third moment at most 1722
on every full-conductor profile-`(6,7)` vector. Odd-unit transport makes five
representative censuses exhaustive, so no pair-feasible collision lies in the
template.

## Dependencies

- `e1_n256_s16_e34_progression_weld_reduction` for normalization, weld
  coverage, and invariant unit transport;
- `e1_n256_proper_conductor_collision_exclusion` for the full-conductor split;
- `e1_n256_s16_e34_three_profile_reduction` and `collision_norm_criterion`
  for the exact cubic-to-norm implication.

## Nonclaims

- no emptiness of the geometric chamber: 3,131,008 weighted full-conductor
  profile vectors exist;
- no exclusion of the generic heavy template;
- no status change for the universal E1 or adjacent-unsafe targets.

## Falsifier

A missing unit orbit, missing normalized vector, shard mismatch, progression
vector with `M_3>1722`, or failure of the cubic sign certificate refutes the
claim.
