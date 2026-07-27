# Audit

- The nine old `(c,A)` branches are disjoint labels inside one set
  `K intersection (K-1)`. Applying nine pointwise bounds discards this union
  and is the source of most of the former constant `29376`.
- The cube-preimage group has order `3n` only when `p=1 (mod 3)`. The ambient
  field hypothesis remains `p>=n^2`; the Mattarei transport checks that exact
  regime independently of the easier order-`n` case.
- `N_sing` counts ordered curve points, not unordered root triples. The
  parameterization is one-to-one after tangent parameters are removed.
- Only the node with `c=1` lies in `H^2`; adding one node for every singular
  trace would be an incorrect extra factor.
- The use of `17` is deliberately class-blind. The cheaper coefficient `10`
  and all richness/disjointness pruning remain available for a sharper bound.
- The Mattarei theorem is used at both orders. Its arbitrary Fermat
  coefficients are essential for quotient slopes outside `H`.
- The `<498` line leaves more than `1443n^2` of the current allowance, but
  that remainder is not a smooth-trace estimate and does not prove DSP8.
