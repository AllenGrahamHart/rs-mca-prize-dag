# L1 m=4, h=3 positive tangent multiplicity exclusion

- **status:** PROVED
- **dependencies:** `l1_m4_h3_tangent_radical_exclusion`,
  `l1_m4_h3_euler_quotient_factorization`
- **consumer:** `l1_mixed_petal_amplification`

Assume `nu>0`. The tangent-radical theorem reduces the complete positive
branch to

```text
(nu,eta)=(1,2) or (2,1),       eta=deg H.              (PTM1)
```

Retain

```text
y_0=-3b/(2a),       T=2a(R-y_0),
kappa=4alpha y_0/g(y_0),
P=X^nu H-kappa.                                         (PTM2)
```

For every root `x` of `T` over the algebraic closure, put
`e=ord_x(T)`. Every repeated tangent root satisfies

```text
e>=2  =>  ord_x(P)=e.                                  (PTM3)
```

In both cases in `(PTM1)`, `P` is cubic. The tangent-radical theorem also
gives `2<=r=deg rad(T)<=3`. Hence every tangent multiplicity is at most
three and

```text
p=deg T=sum_(T(x)=0) ord_x(T)<=3r<=9.                 (PTM4)
```

This contradicts every official characteristic. Therefore both positive
strata are empty on all official `m=4,h=3` rows.

This does not treat `nu=0`, nonembedded `h=2`, wider `m`, wider exchanges,
or the full L1 node.
