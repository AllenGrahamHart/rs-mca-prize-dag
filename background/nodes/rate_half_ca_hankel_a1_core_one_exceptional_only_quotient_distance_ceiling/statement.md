# `A=1` core-one exceptional-only quotient-distance ceiling

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_distance_gap`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_two_sided_resultant_saturation`

Retain the official exceptional-only face and put

```text
h=delta_A(h_1),       e=2^38-1,       r=2e+1.         (QDC1)
```

Then

```text
h<=3(e+1)/2=412316860416.                             (QDC2)
```

Combined with the quotient-distance gap, the exact surviving alternatives
are therefore

```text
h=3,
or
183251937965<=h<=412316860416.                        (QDC3)
```

In particular, every distance from `412316860417` through the ambient
Vandermonde ceiling `r+2=549755813889` is impossible.

More precisely, if `G_z` is the clean degree-`r` locator at an ordinary
supported slope and

```text
a_z=|G_z intersect R_A|,
```

then `G_z\R_A` represents the quotient class of `h_1`, so

```text
h<=r-a_z.                                             (QDC4)
```

Each of the `2e` exceptional roots occurs in exactly `e-1` of the `4e`
ordinary locators. Averaging `(QDC4)` gives `(QDC2)`. This is a theorem-level
compression only; it does not exclude the macroscopic interval in `(QDC3)`.
