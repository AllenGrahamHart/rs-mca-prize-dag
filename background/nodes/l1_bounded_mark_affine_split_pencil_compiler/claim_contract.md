# Claim contract - L1 bounded-mark affine split-pencil compiler

## Inputs

- the exact L1 core-defect pair `(F,W)` with `F` monic and
  `gcd(F,W)=1`;
- pairwise disjoint petals, distinct labels, and exact partial supports;
- polarized support entropy and the L1 cutoff for the aggregate corollary.

## Output

Fixed-polarity partial-petal pairs split into at most `q^p` affine syndromes,
each parallel to the corresponding full-petal kernel and each homogenized by
exactly one additional projective direction. The same pair gives the exact
bounded-basepoint split-pencil identities `(AC7)`. Per source chart and fixed
defect degree, support patterns and syndromes cost only the polynomial
pre-factor `(AC10)` for fixed polarity; `(AC11)` states the separate chart and
defect-degree aggregation cost.

## Consumer rule

Consumers may replace the bounded-polarity arbitrary-locator branch by a
uniform split/saturated-point count in the one-direction cells `(AC5)`. They
may not cite the existing zero-syndrome full-petal payment as a bound for an
arbitrary affine cell without a separate affine-stability theorem.
They must also retain non-intrinsic source-chart first-match multiplicity.

## Falsifier

Two partial solutions with the same missing syndrome whose difference fails a
full-petal equation; a monic fiber requiring more than one homogenizing
direction; failure of `(AC7)`; or a support pattern omitted by the
orientation-plus-exceptions encoding.
