# Rate-half fixed-tail prefix floor

- **status:** see `dag.json` (single source of truth)
- **consumer:** `rate_half_band_closure` (ordinary-list side only)

Let `D` be a multiplicative coset of order `n` in `F`, let
`C=RS[F,D,k]`, and let `c` divide both `n` and `k`. Put `N=n/c`. Fix one
`c`-point fiber `C_0` of `x -> x^c` and an `s`-subset `T_0` of `C_0`, where
`0<s<c`. For integers `d>=0` and

```text
m=k/c+d <= N-1,
```

there is a received word with at least

```text
ceil(C(N-1,m)/q^d),        q=|F|,                         (FT1)
```

distinct codewords agreeing on exactly

```text
k+d*c+s                                                       (FT2)
```

coordinates.

For the rate-half cap row

```text
n=2^41, k=2^40, sigma*=8,592,912,738,
c=2^22, d=2048, s=2,978,146,
N=524,288, m=264,192,
```

the whole band is ordinary-list unsafe whenever

```text
q^2049 < 2^128 C(524287,264192).                           (FT3)
```

The corresponding field-size boundary is

```text
log2(q) < 255.9209759026302... .                            (FT4)
```

This extends the proved list-unsafe subslice beyond `255.900`, but it does not
cover fields up to the `2^256` cap. At that cap the best deterministic qcore
count remains `C(127,64)`, which is `4.8285...` bits below the list trigger.
The theorem makes no MCA claim and no upper-bound claim about heavier prefix
fibers.
