# Audit

- The ambient lower bound is `p>=n^2`, not `p>=m^2`. The exact field-degree
  check in `(7)` is therefore performed separately for `m=n` and `m=3n`.
- The subgroup order need not be dyadic. The Stepanov construction uses only
  `K={x:x^m=1}` and the inequalities `(3)`.
- The parameter rule is integer-exact: `B` is the ceiling cube root of `2m`,
  `A=m//B`, and `D` is the largest integer satisfying the strict linear-system
  inequality. The verifier checks both that inequality and failure at `D+1`.
- `(CPS1)` is for one fixed affine pair. Summing it independently over nine
  quotient branches would discard the cube-preimage compression used by the
  consumer.
