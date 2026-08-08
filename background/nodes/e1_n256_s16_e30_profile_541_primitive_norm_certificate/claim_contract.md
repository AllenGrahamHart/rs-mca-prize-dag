# Claim contract

## Input

The exact 86-vector primitive output of
`e1_n256_s16_e30_profile_541_actual_census_certificate`.

## Output

An independently reproduced exact norm for every input vector and the strict
uniform bound `N<2^250`.

## Falsifier

A missing primitive vector, any FLINT/PARI disagreement, a different maximum,
or a norm at least `2^250`.

The conversion of this norm bound into collision exclusion belongs to the
assembly parent and `collision_norm_criterion`.

