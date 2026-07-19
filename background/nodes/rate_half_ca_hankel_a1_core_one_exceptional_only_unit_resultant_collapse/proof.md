# Proof

Let `a=[X^r]Q`. Since `r=2e+1` is odd and
`n_X=D_0-1=8e+6` is even, resultant symmetry has positive sign:

```text
Res_X(Q,P_X)=Res_X(P_X,Q)
            =c_XP_cl^rE^(r-1).                       (1)
```

The corrected second complement gives, modulo `Q`,

```text
P B_1=P_X.                                           (2)
```

Taking the product of `(2)` over the `r` roots of `Q` in an algebraic
closure of the parameter function field gives

```text
product_(Q(alpha)=0)B_1(alpha)
  =Res_X(Q,P_X)/(a^n_X P^r).                         (3)
```

The infinity theorem proves `deg_X B_1=D_0=n_X+1`. Hence the monic-root
formula for the resultant, followed by `(1)`, yields

```text
Res_X(Q,B_1)
 =a^D_0 product B_1(alpha)
 =a^(D_0-n_X)c_XP_cl^rE^(r-1)/P^r
 =c_X a/E
 =c_X q_bar.                                         (4)
```

This proves `(EUR2)`. The exact exponent `D_0-n_X=1` is load-bearing.

For `W`, the first complement gives `P_XW=P` modulo `Q`, so

```text
product_(Q(alpha)=0)W(alpha)
  =P^r a^n_X/Res_X(Q,P_X).                           (5)
```

If `m=deg_XW`, multiply `(5)` by `a^m` and apply `(1)`:

```text
Res_X(Q,W)
 =c_X^(-1)a^(m+n_X)P^r/(P_cl^rE^(r-1))
 =c_X^(-1)(E q_bar)^(m+n_X)E,
```

which is `(EUR3)`. When `v_inf!=0`, `(EIR3)` makes
`[X^(r-1)]W=-E q_bar v_inf` nonzero, so `m=r-1` and `(EUR4)` follows.

Finally `WB_1=1` modulo `Q`. Multiplying `(EUR2)` and `(EUR3)` gives

```text
Res_X(Q,W)Res_X(Q,B_1)=a^(m+D_0),                    (6)
```

exactly the leading-coefficient correction in the resultant of the unit
identity. This independently checks all exponents. QED.
