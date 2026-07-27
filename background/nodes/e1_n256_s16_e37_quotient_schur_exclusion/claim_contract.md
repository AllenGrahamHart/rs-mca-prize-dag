# Claim contract

## Inputs

- `e1_n256_s16_e38_quotient_schur_exclusion`, giving the residual `V<=74`;
- `e1_n256_s16_sparse_l1_variance_exclusion`, giving the exact chord/slack
  model and rational cubic family;
- `collision_norm_criterion`, giving nonzero norm and the row-prime endpoint.

## Output

No pair-feasible profile-`(3,4,0)` collision has `V=74`; the remaining
positive even variance satisfies `V<=72`.

## Guards

1. The special `R(B,B,B)<=174` replacement is used only when the complete
   weight-two layer lies in `4 Z/128 Z`.
2. The replacement is maximized allocation by allocation; it is not merely
   subtracted from one displayed optimizer.
3. The order-64 census is used only after division by two of the complete
   outer support.
4. The support-in-`4Z` norm argument uses the E=37 ceiling 58, not the older
   E=38 ceiling 60.
5. This theorem does not classify the positive even residual `V<=72`.

## Falsifier

A pair-feasible profile-`(3,4,0)` collision at `V=74`, or an admissible
quotient allocation exceeding the chamber maximum used for its case.
