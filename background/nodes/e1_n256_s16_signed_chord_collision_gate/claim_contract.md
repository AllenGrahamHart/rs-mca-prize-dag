# Claim contract

## Input

- `e1_n256_s16_sparse_l1_variance_exclusion`, including profile
  `(3,4,0)` and the exact residual `0<V<=104`.

## Output

Every vector in that residual has signed repeated-distance cross sum
`C<=-15`, and therefore contains an oppositely signed equal-chord pair.

## Guards

1. Distances are circular distances modulo 128, not ordinary absolute
   differences.
2. Chord weights include the negacyclic orientation sign.
3. Diameter pairs contribute zero to autocorrelation and are charged through
   `D_64`.
4. The conclusion is a necessary additive relation, not norm divisibility or
   collision.
5. Profile `(4,2,0)` and all later distance bands remain outside this
   statement.

## Falsifier

A profile-`(3,4,0)` vector with `0<V<=104` whose signed
repeated-distance cross sum exceeds `-15`.
