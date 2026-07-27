# Claim contract

## Claim

The `(4,5,1)` magnitude-profile branch at `N=256`, folded profile `(3,4,0)`,
and `V=66` is empty on every pair-feasible row.

## Dependencies

- `e1_n256_s16_e33_profile_parity_diameter_reduction` for the profile and
  exact cubic threshold;
- `e1_n256_proper_conductor_collision_exclusion` for the conductor split;
- `collision_norm_criterion` for the quotient and small-field norm
  contradictions.

## Computational scope

The load-bearing census covers every exact mod-16 layer allocation in both
the order-128 odd chamber and the divided order-64 odd chamber. Completeness
is checked by an independent dynamic-programming allocation count. The
outer-`4Z` chamber is proved analytically and is not delegated to the census.

## Nonclaims

- no exclusion of `(5,7)` or `(1,8)`;
- no assertion that a quotient allocation is realized by an autocorrelation;
- no exclusion of a lower variance;
- no promotion of either universal target.

## Falsifier

A legal quotient allocation omitted by the census, a checked allocation with
objective above the reported maximum, failure of the `4Z` norm argument, or
a pair-feasible collision in profile `(4,5,1)` refutes the claim.
