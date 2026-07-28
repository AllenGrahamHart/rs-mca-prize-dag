# L1 Mersenne HNF m=8 order-one quadratic HNF intersection

- **status:** PROVED
- **dependencies:** `l1_mersenne_hnf_m8_order_one_quadratic_pointwise_composition`,
  `l1_mersenne_hnf_m8_order_one_conic_reduction`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** every quadratic-color packet on the four official
  `(m,h)=(8,7)` rows

Put `d=c-1`, `r=rho*c`, and define

```text
a_0=15(d^3+48),
b_0=10(13d^4+55d^3+76d^2-216),
c_0=12(10d^5+62d^4+163d^3+237d^2+213d+180),        (QHI1)

a_1=35d^2,
b_1=14d(11d^2+27d+27),
c_1=120(d^4+4d^3+7d^2+6d+3).                       (QHI2)
```

Every quadratic-color survivor satisfies the two quadratics

```text
a_0 r^2+b_0 r+c_0=0,
a_1 r^2+b_1 r+c_1=0.                                (QHI3)
```

Consequently `d` is a root of the fixed polynomial

```text
R_2(d)=(a_0c_1-c_0a_1)^2
       -(a_0b_1-b_0a_1)(b_0c_1-c_0b_1).             (QHI4)
```

It has exact degree fourteen and leading coefficient `-691200`. Closure of
the complete quadratic-color chamber on one official row reduces to the
eight norm-color gcds

```text
gcd(R_2(X),X^(p+1)-zeta),       zeta in mu_8,        (QHI5)
```

with the inherited saturation `X*(X+1)!=0`. These 32 gcd verdicts are not
asserted here. The degree-eight two-antipodal reduction remains a sharper
sub-chamber endpoint. Higher color degrees, the cyclotomic converse, inner
lifts, and L1 also remain open.
