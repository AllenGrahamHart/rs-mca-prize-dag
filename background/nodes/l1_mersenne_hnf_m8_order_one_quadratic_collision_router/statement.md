# L1 Mersenne HNF m=8 order-one quadratic-collision router

- **status:** PROVED
- **dependencies:** `l1_mersenne_hnf_order_one_frobenius_gate`,
  `l1_mersenne_hnf_m8_order_one_conic_reduction`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the four official `(m,h)=(8,7)` next-to-maximal rows

Put `d=c-1`, `r=rho*c`, remove the known root `x_0=-1/d`, and suppose the
colored Frobenius interpolant on the six roots of `L` is quadratic:

```text
P(W)=(W-x_0)L(W),
E(W)=A W^2+B W+C,       A!=0,       S=-B/A.          (QCR1)
```

If two distinct colors are repeated among those six roots, then

```text
S=0.                                                 (QCR2)
```

Thus the repeated fibers are antipodal pairs. There cannot be three such
pairs, so the collision pattern is exactly two antipodal pairs plus two
singleton colors.

Moreover, this two-pair chamber necessarily satisfies

```text
r*(18+d-d^2)+192=0.                                 (QCR3)
```

Consequently every live quadratic packet belongs to exactly one of:

```text
six distinct colors;
one repeated color and four singleton colors;
two antipodal repeated colors and two singleton colors, with (QCR3). (QCR4)
```

This is an exact router, not an exclusion of degree two. The three chambers
in (QCR4), higher color degrees, cyclotomic converse, and inner lifts remain
open.
