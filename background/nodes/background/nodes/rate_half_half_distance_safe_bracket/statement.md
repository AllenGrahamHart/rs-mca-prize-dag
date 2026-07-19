# Rate-half high-field safe bracket at half distance

- **status:** PROVED
- **closure:** proof with published CA import
- **consumer:** `rate_half_band_closure`

Let `C=RS[F,D,k]` be the official rate-half row

```text
n=2^41,       k=2^40,       q=|F|>=2^169.
```

At

```text
r=(n-k)/2=2^39,
a=n-r=3n/4,
delta=r/n=1/4,
```

the published unique-decoding proximity-gap bound imported by
`mca_from_ca_reduction`, together with the exact MCA half-distance theorem,
gives

```text
B_mca(3n/4)<=n<=floor(q/2^128).                           (HD1)
```

Thus the rate-half adjacent crossing satisfies the improved high-field
bracket

```text
k+8,594,128,896 <= a_RH(q) <= 3n/4       (q>=2^169).     (HD2)
```

The claim is explicit about its published CA input. It is not a
self-contained extension of that input and does not reach the near-capacity
crossing.
