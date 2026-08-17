# Audit

1. The least unsafe cardinality is `B_*+1`, not `B_*`; the residual floor
   therefore exceeds the printed PR slack by exactly one.
2. Group merging occurs before applying `R_2` or `R_3`. The `508` count is
   consequently a count of distinct promoted spaces, not certificates with
   multiplicity.
3. Extending the rich flat to a hyperplane of `U^perp` preserves every rich
   column and forces promoted dimension exactly `r+1`.
4. Common zeros are actual labelled coordinates inside `G_0`; no distinct-
   projective-point assumption is used.
5. The primary verifier uses `math.comb`; the audit uses direct product
   quotients and `divmod`. Both reproduce all floors and ceilings.
6. The adapter is invoked separately inside each bucket. No varying-core
   charge or reverse scalar-locator transport is asserted.
