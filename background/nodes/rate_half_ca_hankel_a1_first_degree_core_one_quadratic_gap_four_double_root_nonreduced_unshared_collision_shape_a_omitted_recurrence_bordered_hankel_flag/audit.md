# Audit

1. Column replacement uses `e_k^T adj(M)v`; no transpose or cofactor sign is
   dropped.
2. The bordered determinant has a minus sign because `det M=0`.
3. Primitivity of `q` is needed for the gcd statement.
4. The generalized alternant is squared because the same exponent matrix
   occurs on both sides of the source diagonal.
5. `S_B` is not squarefree in the nonreduced branch, but its root is absent
   from `H_off`; only `H_off`, `g_off`, and `H_reg` are used squarefreely.
6. The rank characterization is asserted only on `H_reg`, where `D_1` is a
   unit. It is deliberately not extended across `g_off`.
