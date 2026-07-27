# Claim contract

## Inputs

- `e1_n256_s16_e37_quotient_schur_exclusion`, giving the residual `V<=72`;
- `e1_n256_s16_sparse_l1_variance_exclusion`, giving the exact chord/slack
  model and rational cubic family;
- `collision_norm_criterion`, giving nonzero norm and the row-prime endpoint.

## Output

No pair-feasible profile-`(3,4,0)` collision has `V=72`; the remaining
positive even variance satisfies `V<=70`.

## Guards

1. The `R(B,B,B)<=174` replacement is used only after the complete
   weight-two layer is divided into a symmetric subset of `Z/64 Z` avoiding
   0 and 32.
2. The replacement is maximized allocation by allocation; it is not
   subtracted only from one displayed optimizer.
3. The order-64 quotient census is used only after division by two of the
   complete outer support.
4. The support-in-`4Z` norm argument uses the E=36 ceiling 56.
5. This theorem does not classify the positive even residual `V<=70`.

## Falsifier

A pair-feasible profile-`(3,4,0)` collision at `V=72`, an admissible quotient
allocation exceeding its stated chamber maximum, or a symmetric 16-point
subset of `Z/64 Z` with `R(B,B,B)>174`.
