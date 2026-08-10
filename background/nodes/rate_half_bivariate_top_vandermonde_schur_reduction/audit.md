# Audit

1. The parameter basis change is legal because the field contains more
   projective values than there are coordinate fibres in `W`.
2. Only the highest clone at a deficient point appears in the top slice.
   Lower clones are retained in the residual matrix.
3. The Vandermonde block uses distinct domain points and nonzero leading
   coefficients.
4. The reduction proves a rank identity, not that the residual matrix is
   generic or full rank.
5. Pivot-set dependence does not affect whether `M_W` has full column rank.
6. The primary verifier checks synthetic scalar and deficient-column cases.
   The audit independently checks the published ten `m=1` matrices, where
   the residual rank is exactly zero.
