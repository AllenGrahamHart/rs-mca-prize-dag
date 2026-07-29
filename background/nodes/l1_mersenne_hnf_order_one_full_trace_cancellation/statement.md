# L1 Mersenne HNF order-one full-trace cancellation

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_order_one_newton_reciprocal_reduction`
- **consumer:** `l1_mixed_petal_amplification`

Retain the order-one notation, put `d=c-1`, and let

```text
zeta=d^(p+1) in mu_m,       d_star=c_star-1=zeta/d.   (FTC1)
```

The known roots removed from `P_(rho,c)` and `P_(rho_star,c_star)` are

```text
x_0=-1/d,                  x_0^star=-1/d_star.        (FTC2)
```

For every `j>=1`, they satisfy the exact trace identity

```text
(x_0^star)^(mj)=x_0^(-mj)=d^(mj).                    (FTC3)
```

Let `x_1,...,x_H`, where `H=h-1`, be the roots of the reduced polynomial
`L_(rho,c)`, and define the full-root traces

```text
T_j^star=(x_0^star)^(mj)+sum_(i=1)^H (x_i^star)^(mj),
T_j^-   =x_0^(-mj)       +sum_(i=1)^H x_i^(-mj).     (FTC4)
```

For every `1<=r<=H`, the first `r` reduced reciprocal coefficient equations
are equivalent to

```text
T_j^star=T_j^-            for 1<=j<=r.               (FTC5)
```

Consequently the first-three necessary system can be generated directly
from the original monic degree-`h` polynomials `P_(rho_star,c_star)` and
the monic reciprocal of `P_(rho,c)`. There is no need to divide out the
known root or construct `Qtilde`. The required powers remain

```text
8,16,24   for (m,h)=(8,7),
16,32,48  for (m,h)=(16,15).                         (FTC6)
```

This is an exact representation reduction. It does not prove the trace
system empty, impose pointwise Frobenius or cyclotomic divisibility, construct
an inner lift, or close L1.
