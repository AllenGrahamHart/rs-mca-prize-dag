# Proof

The corrected complement is

```text
Q A_1+P_cl E B_1=P_X.                               (1)
```

Its two products on the left have `X`-degree at most `D_0`, while
`deg P_X=n_X=D_0-1`. Reverse `(1)` at degree `D_0`. Using

```text
F=Y^rQ(t,1/Y),       G=Y^D_0B_1(t,1/Y),
A_vee=Y^(D_0-r)A_1(t,1/Y),
R_X=Y^(D_0-1)P_X(1/Y),                              (2)
```

gives

```text
F A_vee+P_cl E G=Y R_X.                             (3)
```

The infinity theorem says

```text
A_vee(t,0)=[X^(D_0-r)]A_1=P_cl j_inf.               (4)
```

Hence `(FRC2)` defines a polynomial `U`, and

```text
A_vee=P_cl j_inf+YU.                                (5)
```

The reciprocal-resultant descent defines `L` by

```text
j_infF+EG=YL.                                       (6)
```

Substitute `(5)` into `(3)`, group `(6)`, and cancel the nonzero polynomial
`Y`:

```text
F(P_clj_inf+YU)+P_clEG
  =P_cl(j_infF+EG)+YFU
  =Y(P_clL+FU)
  =YR_X.
```

This proves `(FRC3)` and the degree bound in `(FRC2)`. Its constant term is

```text
(E q_bar)[X^(D_0-r-1)]A_1+P_clDelta_inf=R_X(0)=1,
```

which recovers `(RBN2)`.

Reduce `(FRC3)` modulo any root `gamma` of `P_cl`. This gives `(FRC5)`.
For the resultant, reduce `(FRC3)` modulo `F` and use scalar homogeneity:

```text
Res_Y(F,R_X)=Res_Y(F,P_clL)
            =P_cl^r Res_Y(F,L)
            =c_XP_cl^rE^(r-1),
```

where the final equality is `(RRD4)`. This proves `(FRC4)`. The derivation
starts from a corrected square; reversing it does not prove the omitted
reconstruction, unit, Hankel, or splitting conditions. QED.
