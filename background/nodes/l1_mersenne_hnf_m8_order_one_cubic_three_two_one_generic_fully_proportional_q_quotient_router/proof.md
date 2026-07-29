# Proof - L1 Mersenne HNF m=8 order-one cubic three-two-one generic fully-proportional q-quotient router

In the quotient by `F_b`, equation (FQR1) gives

```text
a_2q^2=-a_1q-a_0.                                  (1)
```

This is (FQR4) for `j=2`. For `j>=3`, multiply (1) by
`a_2^(j-2)q^(j-2)`. Apply (FQR4) at indices `j-1` and `j-2`; the second
term receives one extra factor `a_2`. The coefficients are exactly the
recurrences in (FQR3), proving (FQR4) by induction.

Multiply (FQR2) by `a_2^5`. The constant and linear terms contribute
`a_2^5theta_0` and `a_2^5theta_1q`. For `2<=j<=6`, equation (FQR4) gives

```text
a_2^5theta_jq^j
 =a_2^(6-j)theta_j(u_jq+v_j) mod F_b.              (2)
```

Summing (2) proves (FQR5)--(FQR6).

Suppose `a_2!=0`. On `F_b=0`, equation `Theta_*=0` is equivalent by
(FQR6) to `R_1q+R_0=0`. If `R_1!=0`, solve for `q`; substituting
`q=-R_0/R_1` into (FQR1) and multiplying by `R_1^2` gives exactly `U=0`.
Every step is reversible under `a_2R_1!=0`. If `R_1=0`, the affine
remainder is zero exactly when `R_0=0`, proving (FQR8). The `a_2=0` chart
is (FBF6), with `Theta_*=0` retained, proving (FQR9).

For the degree ledger, `(deg_b a_2,deg_b a_1,deg_b a_0)=(2,4,6)`.
Induction in (FQR3) gives

```text
deg_b u_j<=4(j-1),       deg_b v_j<=4j-2.          (3)
```

The total-degree bound `deg Theta_*<=12` gives
`deg_b theta_j<=12-j`. Applying (3) termwise in (FQR5) yields
`deg_b R_1<=26` and `deg_b R_0<=28`. Each of the three terms in `U` then
has degree at most 58. QED.
