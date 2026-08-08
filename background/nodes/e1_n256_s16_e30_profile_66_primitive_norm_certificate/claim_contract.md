# Claim contract

## Input

The exact 1,232-vector output of
`e1_n256_s16_e30_profile_66_actual_census_certificate`.

## Output

Independent exact norms for every primitive vector and the uniform bound
`N<2^250`.

## Falsifier

A missing vector, a FLINT/PARI mismatch, a different maximum, or a norm at
least `2^250`.  Collision exclusion is assembled by the parent node.

