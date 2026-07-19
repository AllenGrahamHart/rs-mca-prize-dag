# Proof

The `c=z=1` active-core profile has one nonsaturated row `x_0`. Its
exceptional-incidence bit is zero, and its zero trace gives no clean supported
root. Hence

```text
Q(gamma;x_0)!=0       for every root gamma of P.      (1)
```

Every other residual-domain row is saturated and has exactly `e` distinct
supported roots of `Q(t;x)`. Therefore, in the product defining the first
resultant in `(ERS3)`, every root of the monic `P_X` occurs exactly `e`
times, while `x_0` does not occur. The supported fibers are split and
squarefree, so no other root occurs. This proves

```text
Res_t(P,Q)=c_tP_X^e                                  (2)
```

for one `c_t!=0`.

At every supported slope, the corrected complement gives

```text
Q(gamma;X)A_1(gamma;X)=P_X.                          (3)
```

Multiplying `(3)` over all `T` roots of the monic `P`, and applying `(2)`,
gives

```text
Res_t(P,Q)Res_t(P,A_1)=P_X^T,
Res_t(P,A_1)=c_t^(-1)P_X^(T-e).                      (4)
```

This proves `(ERS3)` including the inverse scalar.

For the other projection, every clean supported fiber of `Q` has exactly
`r` residual-domain roots. Equation `(1)` says none is `x_0`, so all `r`
are roots of `P_X`. The exceptional fiber has exactly `r-1` residual-domain
roots and again none is `x_0`; all `r-1` are saturated. Consequently

```text
Res_X(P_X,Q)=c_XP_cl^rE^(r-1)                        (5)
```

for one nonzero scalar `c_X`.

At every root of `P_X`, the first complement gives

```text
Q(t;x)V(t;x)=P.                                      (6)
```

Multiplying `(6)` over all `n_X` roots and applying `(5)` yields

```text
Res_X(P_X,Q)Res_X(P_X,V)=P^n_X,
Res_X(P_X,V)=c_X^(-1)P_cl^(n_X-r)E^(n_X-r+1).        (7)
```

This proves `(ERS4)`.

Finally `T=4e+1`, `D_0=8e+7`, `n_X=D_0-1`, and `r=2e+1` give `(ERS5)`.
The total-degree check in either direction is the same exact identity

```text
Tr-1=e n_X.                                          (8)
```

The minus one is precisely the exceptional root deficit. Thus no degree is
available for another resultant factor. QED.
