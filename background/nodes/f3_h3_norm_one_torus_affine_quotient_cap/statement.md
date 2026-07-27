# H3 norm-one torus affine quotient cap

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_mobius_excess_half` (scoped evidence)
- **dependency:** `f3_h3_pgl2_pair_identity`

Let `E/F_p` be quadratic, write `bar(x)=x^p`, and put

```text
T={x in E^*:x*bar(x)=1}.
```

If `H<=T`, `a,b in E^*`, and

```text
I_(a,b)=#{z in H:a z+b in H},
```

then

```text
I_(a,b)<=2.                                           (NT1)
```

For the H3 affine quotient pencil, take `a=t`, `b=1-t`. If
`t notin {0,1}`, the identity point `z=1` is always counted, so the exact
PGL2 ledger gives

```text
I_aff(t)<=2,       R(t)=I_aff(t)-1<=1.              (NT2)
```

As a concrete Mersenne-characteristic multiplicative instance, specialize to

```text
p_M=2^31-1,       F=F_(p_M^4),       n=2^21.
```

Since `n | p_M+1`, the unique order-`n` subgroup `H<=F^*` lies in
`F_(p_M^2)` and in its norm-one torus. Every quotient-supported target is a
ratio of elements of `(1-H)\{0}`, hence also lies in `F_(p_M^2)`. Therefore
`(NT2)` applies to every nonidentity target and

```text
X_18=sum_(t!=1)(P(t)-18)_+ R(t)
    <=sum_t P(t)=(n-1)^2,
17X_18<17n^2<300n^2.                                (NT3)
```

Thus the C36' weighted-excess assertion is proved on this quartic
multiplicative-subgroup instance. This is not the deployed Mersenne-31
Chebyshev line round: that evaluation domain is the `chi`-projection of a twin
coset, not `H`. It is also not a prime-field corridor theorem, a genuine
extension-field Mattarei theorem, or a complete adjacent-safe certificate.
