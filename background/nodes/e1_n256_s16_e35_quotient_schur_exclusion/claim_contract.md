# Claim contract

## Inputs

- `e1_n256_s16_e36_quotient_schur_exclusion`, giving the residual `V<=70`
  and the exact `Z/64 Z` inner-layer theorem;
- `e1_n256_s16_sparse_l1_variance_exclusion`, giving the exact chord/slack
  model and rational cubic family;
- `collision_norm_criterion`, giving nonzero norm and the row-prime endpoint.

## Output

No pair-feasible profile-`(3,4,0)` collision has `V=70`; the remaining
positive even variance satisfies `V<=68`.

## Guards

1. The `R(B,B,B)<=174` replacement is used only in the inherited valid inner
   chamber and is maximized allocation by allocation.
2. The order-64 quotient census is used only after division by two of the
   complete outer support.
3. The four exceptional outer allocations are the complete set with
   `R(A,A,A)>458`; all compatible middle and top allocations are exhausted.
4. The two-point top-layer cubic is replaced by zero only because the ambient
   group is a 2-group.
5. The support-in-`4Z` norm argument uses the E=35 ceiling 54.
6. This theorem does not classify the positive even residual `V<=68`.

## Falsifier

A pair-feasible profile-`(3,4,0)` collision at `V=70`, an admissible quotient
allocation exceeding its stated chamber maximum, a fifth odd outer allocation
with `R(A,A,A)>458`, or a compatible exceptional three-layer allocation above
2054.
