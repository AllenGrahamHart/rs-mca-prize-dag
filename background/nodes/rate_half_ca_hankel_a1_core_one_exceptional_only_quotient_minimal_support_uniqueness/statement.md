# `A=1` exceptional quotient minimal-support uniqueness

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_distance_router`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_distance_gap`

Retain the exceptional-only face and put

```text
e=2^38-1,       r=2e+1,
h=delta_A(h_1),       W_A=span{c(a):a in R_A},
|R_A|=r-1=2e.                                           (QMU1)
```

If

```text
h<=e+1=274877906944,                                    (QMU2)
```

then the quotient class `[h_1]` has one unique minimal support `T` of size
`h`. Its nonzero coefficients are also unique modulo `W_A`.

For an ordinary supported slope `z`, let `G_z` be its clean degree-`r`
locator and put

```text
a_z=|G_z intersect R_A|,       H_z=G_z\R_A.             (QMU3)
```

Then `|H_z|>=h`. Equality holds if and only if the fiber is internal in the
quotient-distance ledger. In that case

```text
H_z=T,       a_z=r-h,
j_z=#{a in R_A:beta_a+z alpha_a=0}=h-1.                (QMU4)
```

Consequently all minimum-complement ordinary fibers use the same support
`T`, and their cancellation sets in `R_A` are pairwise disjoint. Their
number is at most

```text
floor(2e/(h-1)).                                        (QMU5)
```

Combined with the proved distance gap, the surviving high-distance range
splits exactly into

```text
183251937965<=h<=274877906944: unique minimal support,
274877906945<=h<=412316860416: uniqueness not asserted. (QMU6)
```

The theorem does not exclude either interval or classify the unique support
polynomial.
