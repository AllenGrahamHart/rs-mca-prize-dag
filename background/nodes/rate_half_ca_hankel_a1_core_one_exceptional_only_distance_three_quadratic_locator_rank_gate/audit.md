# Audit

- The proof uses the degree-three hypothesis on `B` exactly once, in the
  bounded Bezout decomposition `B=uD_j+vD_i` with `u,v` linear.
- Pairwise coprimality of the `D_i` follows from the exceptional-root
  partition. Without it, the bounded Bezout map need not be invertible.
- The rank is projectively well defined: row normalization and the
  pair-Lagrange change of coefficient basis induce invertible row and column
  scalings/changes on the quadratic matrix.
- The verifier replays exact ranks for `e=3,4,5`, checks that every quadratic
  product lies in the printed `3e+1`-element span, and evaluates the
  quadratic coefficient matrix on `6e+3` rows.
- A degree-four replacement for `B` exceeds the claimed rank at `e=4`; this
  mutation guards the load-bearing cubic hypothesis.
