# Claim contract

## Claim

No pair-feasible `N=256`, folded-profile `(3,4,0)`, `V=62` collision has
magnitude profile `(3,7)`, `(2,5,1)`, or `(1,3,2)`.

## Dependencies

- `e1_n256_s16_e31_profile_parity_light_reduction` for exhaustive profiles,
  the eight-template router, and the exact `M_3=1302` cutoff;
- `collision_norm_criterion` for the norm-divisibility implication;
- `e1_n256_proper_conductor_collision_exclusion` for the proper-conductor
  complement of profile `(3,7)`.

## Nonclaims

- no statement about `V<=60` or folded profile `(4,2,0)`;
- no global collision-pair allowance;
- no direct promotion of either universal target.

## Falsifier

A valid vector outside the eight templates, a census row missed by either
engine, disagreement on any printed aggregate, a full-conductor `(3,7)` vector
with `M_3>1302`, or failure of the proper-conductor theorem refutes the claim.
