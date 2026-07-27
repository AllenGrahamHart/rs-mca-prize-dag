# Claim contract

## Claim

The complete E34 generic heavy template has weighted third moment at most 1770
on every full-conductor profile-`(6,7)` vector. Affine-unit transport makes 57
representative censuses exhaustive, so no pair-feasible collision lies in the
template.

## Dependencies

- `e1_n256_s16_e34_generic_affine_weld_reduction` for orbit and weld coverage;
- `e1_n256_proper_conductor_collision_exclusion` for the full-conductor split;
- `e1_n256_s16_e34_three_profile_reduction` and `collision_norm_criterion`
  for the exact cubic-to-norm implication.

## Nonclaims

- no emptiness of the geometric chamber: 418,464 representative
  full-conductor profile vectors exist;
- no direct assertion about lower variances;
- no status change for the universal E1 or adjacent-unsafe targets.

## Falsifier

A missing affine orbit, missing normalized vector, shard mismatch, generic
vector with `M_3>1770`, or failure of the cubic sign certificate refutes the
claim.
