# Proof - L1 Mersenne HNF m=8 order-one cubic three-two-one generic fully-proportional parameter reduction

Write `a_d=b-6` in (DQR3). Direct collection gives

```text
40a_d^3+480a_d^2+2520a_d+6480
  =40b(b^2-6b+27),

462a_d+3402=42(11b+15),

480a_d^2+5760a_d+30240=480b^2+12960.               (1)
```

Hence

```text
N_1=q(qP+2880bR_0),
N_0=qR_0Q+17280R_0^2+q^2T_c.                       (2)
```

If `b=0`, then `P=630q`, so `N_1=630q^3!=0`: every official
characteristic exceeds seven and the inherited saturation has `q!=0`.
Thus `N_1=0` gives `b!=0` and the reconstruction in (FPR2). Substitute it
in the second line of (2), divide by `q^2`, and multiply by `2880b^2`.
The result is exactly `F_N=0`. Reversing these operations proves both
directions of (FPR2).

Now use (DQR6). Since `c_0q!=0`, `U_1=0` is exactly the first equation in
(FPR4), or

```text
S_0=-c_1R/(2c_0)-qa_d/18.                           (3)
```

Complete the square in the constant role value:

```text
c_2R^2+c_1RS_0+c_0S_0^2
 =c_0(S_0+c_1R/(2c_0))^2
  -delta_Phi R^2/(4c_0).                            (4)
```

Substituting (3) into `U_0=0`, using (4), and multiplying by `12c_0`
gives

```text
c_0^2(q^2a_d^2+144qR_0)-81delta_Phi R^2=0,          (5)
```

which is the second equation in (FPR4). Conversely, (3) and (5) reverse
the calculation and recover `U_1=U_0=0`.

Finally, `P_4=-3qd^2+qa_dd+12R_0`, so its discriminant is the expression
in parentheses in (5). Combining the exact conic and role equivalences with
the dependency gives (FPR5). QED.
