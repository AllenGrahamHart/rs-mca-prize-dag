# Claim contract

## Claim

The complete normalized E34 quarter heavy-position template has weighted
third moment at most 1188 on every full-conductor profile-`(6,7)` vector.
Consequently no pair-feasible collision lies in that template.

## Dependencies

- `e1_n256_s16_e34_heavy_chord_template_reduction` for normalization;
- `e1_n256_proper_conductor_collision_exclusion` for the full-conductor split;
- `e1_n256_s16_e34_three_profile_reduction` and `collision_norm_criterion`
  for the exact cubic-to-norm implication.

## Nonclaims

- no emptiness of the geometric quarter class: 1,031,680 full-conductor
  profile-`(6,7)` vectors exist;
- no exclusion of the other three heavy templates;
- no status change for the universal E1 or unsafe targets.

## Falsifier

A missing normalized vector, a shard mismatch between the two implementations,
a full-conductor quarter vector with `M_3>1188`, or failure of the inherited
cubic sign certificate refutes the claim.
