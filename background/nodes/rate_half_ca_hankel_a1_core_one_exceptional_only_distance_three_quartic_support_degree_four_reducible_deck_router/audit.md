# Audit

1. Reducibility is geometric. Frobenius-conjugate graph components are
   charged before selecting a base-field deck transformation.
2. The residual divisor has total bidegree at most `(2,2)` and at most two
   positive-bidegree components. The `2912` ledger deliberately charges two
   worst-case `1440` components plus the graph constant `32`.
3. The Newton-support lemma enumerates all supports, not coefficient values.
   It is used only to exhibit an admissible unimodular transform; absolute
   irreducibility remains a theorem hypothesis at that step.
4. One-dimensional Newton support is not silently bounded. Absolute
   irreducibility makes it a primitive toral binomial, handled separately.
5. Degree multiplicativity on the toral normalization forces a graph; this
   excludes higher-exponent correspondences without assuming they are
   automorphisms.
6. A special deck graph is required to carry a subgroup point before its
   scalar is placed in `mu_N`.
7. The theorem constrains `psi`, not the original matching. Downstream work
   must still handle pairs lying in different fibers of the inner quotient.
