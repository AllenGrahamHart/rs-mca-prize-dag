# Claim contract

## Proved

- Under `(SD1)`, an extension-field list of size `L` projects through one
  base-field linear functional to `L` distinct base-field codewords without
  losing agreement.
- The threshold predicates in `(SD2)` are equivalent.
- The simpler condition `(SD3)` is sufficient.
- The upstream Mersenne-31 quartic `2^-100` specialization has the exact
  margin in `(SD4)`.

## Consumer

`rate_half_list_adjacent_crossing`, on extension rows whose domain lies in a
proper base field and whose candidate threshold satisfies `(SD1)`.

## Falsifier

An instance satisfying `(SD1)` with an extension list of size `L` but no
base-field list of that size falsifies the theorem.

## Nonclaims

- No base-field or extension-field list upper bound is proved.
- The domain containment `D subset F` is load-bearing.
- The strict inequality `(SD1)` is not weakened to equality.
- The deployed specialization has target `2^-100`; it is not relabeled as a
  `2^-128` prize row.
- Rows failing `(SD1)`, including sufficiently large extension degrees, remain
  open.
