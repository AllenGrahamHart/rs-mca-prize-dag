# Audit

- Full-generator coefficient independence remains valid over the algebraic
  closure, where the irreducible component factorization is taken.
- Separation rank across two variable groups is ordinary matrix rank.  The
  product of rank-`h` and rank-`g` separated expressions has at most `hg`
  terms, so the required submultiplicative upper bound is elementary.
- The complement `G_i` has parameter degree `m-e_i`; its rank bound
  `m-e_i+1` counts homogeneous binary monomials and does not assume its
  coefficients are independent.
- The ceiling direction is preserved when `b` is replaced by its upper
  bound.  Since official `m` is divisible by four and
  `b<=m/4-1`, the worst-case ratio is strictly greater than four.
- Rank at least five is an exclusion, not a classification.  No generic
  rank-five point count is consumed downstream.
- The verifier checks the ceiling arithmetic, official constants, and DAG
  wiring.  The proof itself is symbolic and needs no numerical experiment.
