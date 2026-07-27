# Claim contract

## Claim

The `(1,8)` autocorrelation magnitude-profile branch at `N=256`, folded
profile `(3,4,0)`, and `V=66` is empty on every pair-feasible row.

## Dependencies

- `e1_n256_s16_e33_profile_parity_diameter_reduction` supplies the unique
  light diameter, one-odd-class parity condition, and exact cubic threshold;
- `collision_norm_criterion` supplies the row-prime norm contradiction.

## Computational scope

The production and audit implementations both cover all eleven classified light
templates, all `binom(124,3)` heavy supports per template, and all 64 sign
patterns after global-sign normalization. The bound is over every conductor,
so no conductor chamber is omitted or delegated.

## Nonclaims

- no exclusion of the remaining `(5,7)` profile;
- no exclusion of a lower variance;
- no promotion of either universal target.

## Falsifier

A normalized one-odd light support outside the eleven templates, a vector omitted
by either census, a profile-`(1,8)` vector with `M_3>1356`, or a pair-feasible
collision in this profile refutes the claim.
