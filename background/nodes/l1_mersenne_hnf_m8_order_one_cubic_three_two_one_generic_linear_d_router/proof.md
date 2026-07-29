# Proof - L1 Mersenne HNF m=8 order-one cubic three-two-one generic linear-d router

Let `Q_6=(Y-A)V-S`. The definitions in (SQC3) give

```text
Q_6=6G_2+AxU-L_3-D.                                 (1)
```

Substituting `L_3=20+q(d+8)/3` proves the first identity in (GLD2); the
other two follow directly from `L_4` and `J`.

Put

```text
F_4=G_2H-xQ_6-W,
F_5=(q-d)DH+JQ_6.                                   (2)
```

The polynomial identities

```text
E_4=DF_4+xE_6,
E_5=DF_5-JE_6                                      (3)
```

follow from `E_6=DQ_6-K_6` and (CMR2). Since `D!=0`, equations
`E_4=E_5=E_6=0` are therefore equivalent to `F_4=F_5=E_6=0`.

Use (GLD2) in (2). Collecting powers of `d` gives exactly

```text
12F_4=P_4,
3F_5=P_5.                                           (4)
```

The quadratic coefficients in (GLD3) are `-3q` and `qT`. Hence the
quadratic term cancels from `3P_5+TP_4`; collecting its remaining terms
gives (GLD4)--(GLD6). Because the official characteristics exceed three,

```text
P_4=P_5=0  iff  P_4=C_1d+C_0=0.                    (5)
```

This proves (GLD5).

If `C_1!=0`, (GLD5) is equivalent to (GLD7) and `P_4=0`. Substituting the
reconstruction in `P_4,E_6`, the conic, and the role equation and clearing
the displayed powers of `C_1` is reversible on this chart. Conversely, a
saturated solution of (GLD9) reconstructs `d`, recovers all four equations,
and then recovers `E_4=E_5=0` from (3)--(5). Saturating the cleared
numerators of `d,q-d,Delta,W` preserves the inherited and generic guards.

If `C_1=0`, equation (GLD5) instead forces `C_0=0`. Conversely,
`C_1=C_0=P_4=0` implies `P_5=0` by (GLD6), so (3)--(5) recover the original
three coefficient equations. Retaining the conic, role equation, and all
nonzero factors proves (GLD10) and completes both directions. QED.
