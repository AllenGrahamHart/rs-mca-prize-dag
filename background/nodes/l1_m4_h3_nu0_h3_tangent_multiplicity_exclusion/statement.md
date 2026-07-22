# L1 m=4, h=3, nu=0 cubic-tangent multiplicity exclusion

- **status:** PROVED
- **dependencies:** `l1_m4_h3_nu0_nonzero_b_tangent_exclusion`,
  `l1_m4_h3_euler_quotient_factorization`
- **consumer:** `l1_mixed_petal_amplification`

Assume `nu=0`, `b!=0`, and `h=deg H=3`. Retain

```text
g(Y)=Y^3+aY+b,       Delta=-4a^3-27b^2!=0,
y_0=-3b/(2a),        T=2a(R-y_0),
kappa=4alpha y_0/g(y_0).                              (TME1)
```

For a root `x` of `T` over the algebraic closure, put
`e=ord_x(T)`. Every repeated tangent root satisfies the exact local identity

```text
e>=2  =>  ord_x(H-kappa)=e.                           (TME2)
```

The preceding tangent-radical theorem gives

```text
2<=r=deg rad(T)<=3.                                   (TME3)
```

Since `H-kappa` is cubic, `(TME2)` makes every repeated-root multiplicity at
most three; simple roots have the same bound. Therefore

```text
p=deg T=sum_(T(x)=0) ord_x(T)<=3r<=9.                 (TME4)
```

Every official characteristic is at least `8191`, so this is impossible.
Thus the complete `nu=0`, `b!=0`, `deg H=3` endpoint is empty on all four
official `m=4` rows.

This does not treat `b=0`, positive valuation, nonembedded `h=2`, wider
`m`, wider exchanges, or the full L1 node.
