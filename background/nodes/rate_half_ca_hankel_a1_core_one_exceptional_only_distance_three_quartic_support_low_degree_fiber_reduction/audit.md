# Audit

1. The comparison uses `r_l=P_l/D_l^2`; this is the normalization for which
   the smooth weight cancels across two omitted-pair gates.
2. A constant comparison is not discarded. It forces two quartics to be
   the corresponding squared pair locators and then forces global
   antiweight, including the two formerly omitted pairs.
3. Equality of selected rational generators need not separate finitely many
   normalization points. The proof explicitly charges at most `18d^2`
   ordered lifts, producing the `9d^2` pair loss in `(QFR5)`.
4. The degree-eight comparison ceiling is exact before cancellation.
   Generator compression uses divisibility of function-field extension
   degrees, not a dimension heuristic.
5. Degrees five through eight are removed by tame Riemann--Hurwitz. A pair
   whose own quartic is not divisible by its locator consumes a distinct
   ramification point; two remaining divisible quartics yield a nonconstant
   degree-at-most-four member of `F_p(psi)`.
6. The theorem classifies all-rank deficiency. It does not convert analogue
   rank data into a universal support exclusion.
