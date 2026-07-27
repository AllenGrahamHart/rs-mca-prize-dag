# Claim contract

## Claim

The complete normalized E34 nonquarter-diameter weld chamber has weighted
third moment at most 1560 on every full-conductor profile-`(6,7)` vector.
Consequently no pair-feasible collision lies in that heavy template.

## Dependencies

- `e1_n256_s16_e34_nonquarter_diameter_weld_reduction` for complete
  normalization and chamber coverage;
- `e1_n256_proper_conductor_collision_exclusion` for the full-conductor split;
- `e1_n256_s16_e34_three_profile_reduction` and `collision_norm_criterion`
  for the exact cubic-to-norm implication.

## Nonclaims

- no emptiness of the geometric chamber: 899,456 full-conductor
  profile-`(6,7)` vectors exist;
- no exclusion of the progression or generic templates;
- no status change for the universal E1 or adjacent-unsafe targets.

## Falsifier

A missing normalized vector, a shard mismatch, a full-conductor chamber vector
with `M_3>1560`, or failure of the inherited cubic sign certificate refutes
the claim.
