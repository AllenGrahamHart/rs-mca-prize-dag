# Claim contract

## Claim

No pair-feasible `N=256`, folded-profile `(3,4,0)`, `V=60` collision has
profile `(2,7)` or `(1,5,1)`.

## Dependencies

- `e1_n256_s16_e30_profile_parity_light_reduction` for the complete 87-orbit
  router and exact cubic cutoff;
- `collision_norm_criterion` for norm divisibility;
- `e1_n256_proper_conductor_collision_exclusion` for both proper-conductor
  complements.

## Nonclaims

- no exclusion of `(6,6)`, `(5,4,1)`, or `(4,2,2)`;
- no exclusion of `V<=58` or another folded profile;
- no global collision-pair allowance.

## Falsifier

A valid two-odd light support outside the 87 templates, a missed profile
vector, disagreement between either engine pair, a full-conductor `(1,5,1)`
vector above the cubic cutoff, or an exact `(2,7)` norm at least `2^250`
refutes the claim.
