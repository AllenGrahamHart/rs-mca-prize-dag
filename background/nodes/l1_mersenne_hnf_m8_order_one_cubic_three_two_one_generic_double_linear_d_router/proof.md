# Proof - L1 Mersenne HNF m=8 order-one cubic three-two-one generic double-linear-d router

Use `Q_6=Q_0-qd/3` in `E_6=DQ_6-K_6`, and expand the conic as

```text
C=120d^4+480d^3+840d^2+720d+360
  +q(154d^2+378d+378)+35q^2.                       (1)
```

The leading terms of `720E_6` and `qC` cancel. After dividing their sum by
the unit two, direct coefficient collection gives

```text
R_3=(720E_6+qC)/2
   =-132qd^3+(12q^2-558q)d^2
    -(120Dq+1062q+86q^2)d
    +360DQ_0-360-1098q-191q^2+10q^3.               (2)
```

Reduce this cubic once by `P_4` from (GLD3):

```text
R_2=R_3-44dP_4
   =q kappa d^2+B_1d+B_0.                          (3)
```

Its quadratic coefficient is opposite to that of `kappa P_4/3`. Hence

```text
3R_2+kappa P_4=M_1d+M_0.                           (4)
```

Substituting (2)--(3) into (4) and multiplying by two gives (GDL2).
Every official characteristic exceeds five, so all divisions and fixed
integer multipliers above are units.

On `P_4=C=0`, identity (GDL2) says

```text
E_6=0  if and only if  M_1d+M_0=0.                 (5)
```

The dependency proves that, on `E_6=0`, equations `E_4=E_5=0` are
equivalent to `P_4=C_1d+C_0=0`. Adding the retained conic and role equation
therefore proves the exact system (GDL3).

If `C_1!=0`, the first linear equation reconstructs `d=-C_0/C_1`. The
second linear equation is then equivalent to `Omega=0`, proving chart one.
If `C_1=0`, the first line instead gives `C_0=0`. When `M_1!=0`, the second
line reconstructs `d=-M_0/M_1`, proving chart two. Finally, when both
linear coefficients vanish, their equations are exactly `C_0=M_0=0`,
which gives (GDL5).

Conversely, each chart reconstructs both linear equations in (GDL3), and
(5) plus the dependency recovers `E_6,E_4,E_5`. Clearing denominators is
reversible under the stated coefficient and inherited saturations. This
proves all three charts. QED.
