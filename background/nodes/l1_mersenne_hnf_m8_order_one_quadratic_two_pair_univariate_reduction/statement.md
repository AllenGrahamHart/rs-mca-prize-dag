# L1 Mersenne HNF m=8 order-one quadratic two-pair univariate reduction

- **status:** PROVED
- **dependencies:** `l1_mersenne_hnf_m8_order_one_conic_reduction`,
  `l1_mersenne_hnf_m8_order_one_quadratic_collision_router`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the two-antipodal-pair quadratic chamber on the four official
  `(m,h)=(8,7)` rows

Put

```text
d=c-1,       r=rho*c,       D=18+d-d^2.              (QUR1)
```

Every survivor in this chamber has `D!=0` and

```text
r=-192/D.                                            (QUR2)
```

It also satisfies the fixed degree-eight equation

```text
F(d)=5d^8+10d^7-180d^6+672d^5+2862d^4
     -15516d^3+8199d^2-44172d+4860=0.               (QUR3)
```

Conversely is not claimed. To close this chamber on one official prime it
is enough to verify, in a field containing `mu_8`, that

```text
gcd(F(X),X^(p+1)-zeta)=1       for every zeta in mu_8, (QUR4)
```

with the inherited saturation `X*(X+1)*D!=0`. Thus the remaining outer
torsion test is exactly 32 degree-eight gcd packets across the four rows;
no generic conic or high-degree resultant is required.

This reduction does not assert the gcd verdict, treat the collision-free or
one-repeat quadratic chambers, handle color degree at least three, construct
an inner lift, or promote L1.
