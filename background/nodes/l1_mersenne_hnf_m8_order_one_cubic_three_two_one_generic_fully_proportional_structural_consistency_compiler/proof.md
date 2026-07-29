# Proof - L1 Mersenne HNF m=8 order-one cubic three-two-one generic fully-proportional structural-consistency compiler

The coefficient router gives the first four reconstructions in (FSC1).
Equation (FCR3) gives `H_c+G_c=ell`; solving
`H_c=G_c+A(x+Y_c)` gives the displayed `Y_c`. Conversely these two equations
imply

```text
2G_c=L_2-x^2-A(2x+Y_c),                            (1)
```

so the original definitions of `G_2,H,Y` are recovered. Defining `V_c` as
in (FSC1), the original `D=YV` equation is exactly `Z_D=0` under the printed
denominators.

For `Q_0`, use `A(x+Y_c)=H_c-G_c=ell-2G_c`. Its original definition becomes

```text
Q_0=6G_c+x(ell-2G_c)-20-8q/3-D_c
   =A G_c+x ell-20-8q/3-D_c,                       (2)
```

which is exactly `Z_Q=0`.

Finally, on `Z_D=0`,

```text
W_0=Y_c(A+x)V_c+15+23q/4+q^2/8
   =(A+x)D_c+15+23q/4+q^2/8.                       (3)
```

Substitute (3) and `H_c=ell-G_c` in
`R_0=G_2H-xQ_0-W_0`; the result is `Z_R=0`. More explicitly, the original
`R_0` residual minus the expression defining `Z_R` is
`(A+x)(Y_cV_c-D_c)`, so the joint use of `Z_D,Z_R` is reversible. This proves
(FSC3).

For the degree bounds, the rational functions `(D_c,Q_c,G_c,Y_c,V_c)` admit
numerator/denominator degree bounds

```text
(3/1), (5/3), (6/4), (6/5), (12/10),              (4)
```

where fixed numerical factors are ignored. A common denominator for `Z_D`
has degree 15, giving numerator degree at most 18. Common denominators
`bE_GD_*` and `b^2E_G^2D_*` for `Z_Q,Z_R` have degrees 7 and 11; termwise
collection gives numerator degrees at most 10 and 15. Cancellation can only
lower these bounds, proving (FSC4).

On `rho_1!=0`, substitution of `q=-rho_0/rho_1` in a polynomial of
`q`-degree `m_i` is cleared exactly by `rho_1^m_i`. Thus (FSC5) is polynomial
and reversible. Combining it with (FQR7) and (FSC3) proves (FSC6). QED.
