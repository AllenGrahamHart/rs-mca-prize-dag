# Audit

1. The padding sum is over off-line slopes only. The global value `e-6`
   loses exactly the `d_A=1` line contribution, giving `e-7`.
2. The `e-7` heavy slopes are distinct because `g_off` is squarefree.
3. Divisibility by `(X-x_*)^(e-7)` becomes equality only after comparing
   with the complete padding degree `sum r_delta=e-7`.
4. The residual degree uses `deg H_delta=a_delta-q_delta`, not the weaker
   bound `deg H_delta<=a_delta`.
5. The scalar `c` is retained in the norm and tangent formulas; monic fiber
   factors do not normalize the biform scalars.
6. Coprimality with `L_U0` is inherited from the exact norm theorem and the
   fact that `x_*` is outside `U_0`.
7. This is a reduction to `T`, not evidence that arbitrary degree-`e`
   polynomials are realizable.
