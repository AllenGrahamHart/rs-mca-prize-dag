# Proof

The incoming MCA-from-CA theorem applies at integer radius `r` under

```text
2r<=n-k.
```

Substitute `r=n-a` and rearrange:

```text
2(n-a)<=n-k
iff n+k<=2a
iff a>=ceil((n+k)/2).                                    (1)
```

For `n=2^41` and `k=2^40`, `n+k=3*2^40` is even, so the right side of `(1)`
is exactly

```text
a>=3*2^39=3n/4.                                         (2)
```

Every integer in the live interval has `a<=3n/4-1`, hence violates `(2)`.
At its closest point,

```text
2(n-(3n/4-1))-(n-k)
  =n/2+2-n/2
  =2,                                                    (3)
```

which proves `(SC4)`. At the endpoint `a=3n/4`, the left side of `(3)` is
zero, so the hypothesis holds with equality. This is precisely the endpoint
already consumed by `rate_half_half_distance_safe_bracket`. Therefore the
unique-decoding transfer supplies the endpoint and no point of the live
interior. QED.
