# Claim contract

## Claim

The `(0,6,1)` magnitude-profile branch at `N=256`, folded profile `(3,4,0)`,
and `V=66` is empty on every pair-feasible row.

## Dependencies

- `e1_n256_s16_e33_profile_parity_diameter_reduction` for the exact profile
  and cubic threshold;
- `e1_n256_proper_conductor_collision_exclusion` for the conductor split;
- `collision_norm_criterion` for the final norm contradiction.

## Nonclaims

- no exclusion of `(5,7)`, `(1,8)`, or `(4,5,1)`;
- no exclusion of a lower variance;
- no assertion that the sharp abstract subgroup example is an
  autocorrelation profile;
- no promotion of either universal target.

## Falsifier

A symmetric set avoiding `0,64` with a target fiber larger than `|A|-2`, a
profile `(0,6,1)` vector with `M_3>1644`, or a pair-feasible collision in this
profile refutes the claim.
