# Audit

1. The extrapolation uses all classified rows, but only the inequality
   `deg g_r<=n<|X|`; no generic-rank assumption is inserted.
2. The sign in the barycentric weight is fixed by the factor
   `(x_*-x)L_X'(x)` and checked independently over `F_101`.
3. The quotient bound is a consequence of exact degrees after divisibility;
   it is not an additional rank assumption.
4. Binary-form divisibility is intrinsic. The remainder matrix uses a chart
   with infinity away from `Z(H)`, so no root or degree is silently lost.
5. The zero heavy row is retained: `T_j=0` is allowed by the source theorem.
6. `verify.py` constructs coefficient polynomials and the remainder matrix.
   `verify_audit.py` uses hard-coded row values, weights, and remainder
   columns and checks a mutation that destroys divisibility.
7. The node proves compatibility with the augmented heavy-row gate only.
   Other Hankel/source equations remain live.
