# Proof - J-zero guard compiler

The scaled formulas follow directly from `X=dW`. The common quadratic is

```text
Q(W)=W^2+(g_1+y)W+v,
```

and the dependency gives `x=dg_1`, `Y_j=dy`, and `V_j=d^2v`. This proves
the first line of (JGC4). Multiplying
`G=Q(W)(W-y)` by `d^3`, and using `a=A/d` and `B=S_c/d^3` in
`F=G+aQ+B`, proves the remaining lines.

Evaluate `Qhat` at `Y_j`:

```text
Qhat(Y_j)=3Y_j^2+2xY_j+G_j.
```

The role reconstruction (FJR1) therefore gives
`R_j=A Qhat(Y_j)`. The formula for `d` in (JGC1) gives
`S_c=S_j+qd/3=eta R_j`. Substituting these identities and
`lambda-1=eta^(-1)` gives

```text
(A/d)(S_c/d^3)(eta^(-1))(Qhat(Y_j)/d^2)
 =A R_j Qhat(Y_j)/d^6
 =R_j^2/d^6.
```

This proves (JGC5). A matched ordered color pair has nonzero, pairwise
distinct `1,beta,gamma`. Hence `eta`, `eta+1`, `lambda`, and
`lambda-1` are all nonzero. Together with `d*R_j!=0`, (JGC5) pays
`a*B*(lambda-1)*Q(y)!=0`; it also gives `R*S!=0` because the scaled
role values are `(R_j,S_c)=(R_j,eta R_j)`.

For (JGC7), use the product discriminant formula twice. Since
`Ghat=Qhat(X)(X-Y_j)`,

```text
disc(Ghat)=disc(Qhat) Qhat(Y_j)^2.
```

At the two roots of `Qhat`, `Fhat=S_c`. At `X=Y_j`, the role identity
`A Qhat(Y_j)=(lambda-1)S_c` gives `Fhat=lambda S_c`. Thus

```text
Res_X(Ghat,Fhat)=S_c*S_c*(lambda S_c)=lambda S_c^3.
```

Finally

```text
disc(Fhat Ghat)=disc(Fhat)disc(Ghat)Res(Fhat,Ghat)^2,
```

which is (JGC7). Every factor in (JGC7) except `D_Q,D_F` is already
nonzero, proving (JGC8).

It remains to check the exact fiber degrees. Equation (JGC9) gives
`E-1=(beta-1)Fhat/S_c`, so its gcd with the squarefree `Lhat` is
exactly `Fhat`. Also

```text
E-beta=(beta-1)(Fhat-S_c)/S_c
      =(beta-1)Qhat(X)(X-Y_j+A)/S_c.
```

The extra linear factor cannot add a root outside `Qhat`: at such a root
`Fhat=S_c!=0`, and it is not `Y_j` because `A!=0`. Thus the gcd is
exactly `Qhat`. Finally `E-gamma` vanishes at `Y_j`; it does not vanish on
`Fhat` or `Qhat`, where `E` equals `1` or `beta`. Its gcd with `Lhat` is
therefore exactly `X-Y_j`. This proves (JGC10).

The scaling identity gives `d^6L(-1/d)=Lhat(-1)`, so (JGC11) is exactly
the removed-root coprimality guard. It also gives
`Lhat(0)=d^6L(0)=K_6` by (SQC2). The remaining entries in `G_alg` are
precisely the coefficient-router denominators, the generic `Delta*W`
chart, the order-one `c=d+1` guard, the HNF factors, and the role factors
printed by the dependencies. Fixed numerical denominators are units in all
official characteristics. Hence (JGC12) is a lossless finite guard ledger.
QED.
