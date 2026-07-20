# `A=1` exceptional quotient minimal-support packing

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_minimal_support_uniqueness`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_distance_ceiling`

Retain the official exceptional-only quotient class with

```text
e=2^38-1,       r=2e+1,       |D_res\R_A|=v=6e+7.
```

Let `L_h` be the number of distinct minimal supports of size
`h=delta_A(h_1)`. For two distinct minimal supports `T,T'`,

```text
|T intersect T'|<=lambda_h:=2h-2e-4.                  (QMP1)
```

Thus `h<=e+1` permits only one support, recovering the uniqueness theorem.
For `h>=e+2`, put

```text
Delta_h=h^2-v lambda_h.                               (QMP2)
```

Whenever `Delta_h>0`, the exact Johnson second-moment bound is

```text
L_h<=floor(v(h-lambda_h)/Delta_h).                    (QMP3)
```

On the official row, `Delta_h>0` throughout

```text
274877906945=e+2 <= h <=302646214511.                 (QMP4)
```

In particular,

```text
L_(e+2)<=5,
L_h<=6       for e+2<=h<=279180239468.                (QMP5)
```

The second interval contains `4,302,332,524` quotient distances. The bound
does not classify any leader, exclude a distance, or control
`h>=302646214512`.
