# Claim contract

## Claim

The `(5,7)` autocorrelation magnitude-profile branch at `N=256`, folded
profile `(3,4,0)`, and `V=66` is empty on every pair-feasible row.

## Dependencies

- `e1_n256_s16_e33_profile_parity_diameter_reduction` supplies the exhaustive
  profile list, unique light diameter, diameter-Sidon condition, and threshold;
- `e1_n256_proper_conductor_collision_exclusion` removes every gcd-greater-than-one
  support, including the unrestricted moment maximizer;
- `collision_norm_criterion` supplies the row-prime norm contradiction.

## Computational scope

Both implementations cover all 100 classified light orbits, all
`binom(124,3)` heavy supports per orbit, and all 64 global-sign-normalized sign
patterns. Every returned chamber is complete; errors and missing templates
would leave the packet explicitly incomplete.

## Nonclaims

- no exclusion of a lower variance;
- no claim that `M_3<=1416` holds at proper conductor;
- no promotion of either universal target.

## Falsifier

A diameter-Sidon light support outside the 100 orbits, disagreement between
the two exact censuses, a full-conductor profile vector with `M_3>1416`,
failure of the proper-conductor router, or a pair-feasible collision in this
profile refutes the claim.
