# Proof - L1 Mersenne HNF m=8 order-one cubic three-two-one coefficient-matrix router

In (SQC5), write

```text
G_2^2+AU G_2-Y(A+x)V-L_4=G_2H-W.                    (1)
```

Then `E_4=0` is the first line of (CMR2). Likewise

```text
E_5=(q-d)D^2H+((q-d)G_2-6dD)K_6,                   (2)
```

which is the second line. The determinant of their coefficient matrix in
`(H,K_6)` is

```text
(DG_2)J-(-x)(q-d)D^2=D Delta.                       (3)
```

When `Delta!=0`, Cramer's rule gives exactly (CMR3), proving the generic
equivalence.

Suppose `Delta=0`. Multiply the first line of (CMR2), after moving `DW` to
the left, by `J`, and the second by `x`. Adding gives

```text
D Delta H-DWJ=0.                                    (4)
```

Hence `WJ=0`. If `J=0`, then `Delta=x(q-d)D=0`, so `x=0`; the second line
of (CMR2) gives `H=0`, and the first gives `W=0`. Conversely those four
relations satisfy (CMR2). If `J!=0`, equation (4) gives `W=0`. The matrix
has determinant zero and its second row is nonzero, so retaining the second
line of (CMR2) is equivalent to both lines. This proves (CMR4).

Now set `x=0`. Then `A=6`, `U=Y`, and direct substitution in (SQC3) gives
(CMR5). Since `D!=0`, `E_4=0` reduces to

```text
-6Y^3+9Y^2-3L_2Y+L_2^2/4-L_4=0.                   (5)
```

Multiplying (5) by `-16` and inserting (SQC2) gives `C_0=0`. The sixth
equation is `DM-K_6=0`. Substituting `K_6=DM` into `E_5=0` and cancelling
`D` gives `F_5=0`. This proves (CMR6).

Finally take the singular `J=0` subbranch. Here `H=0` gives
`Y=-L_2/6`. Since `D!=0`, also `L_2!=0`, and

```text
G_2=L_2,
V=L_2(L_2+36)/36=(q+30)(q+102)/144.                (6)
```

Dividing `J=L_2(q-d+dV)=0` by `L_2` and multiplying by 144 gives `F_J`.
The relation `W=6YV+L_4=L_4-L_2V=0`, multiplied by 288, gives `F_W` after
expansion. This proves (CMR7). QED.
