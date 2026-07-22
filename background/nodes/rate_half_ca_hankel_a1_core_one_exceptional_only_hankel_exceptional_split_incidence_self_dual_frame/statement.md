# `A=1` exceptional split-incidence self-dual frame

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_exceptional_self_dual_evaluation_code`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_two_sided_resultant_saturation`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_distance_sharp_ceiling`

Use `z=E/H`, so the exceptional slope is `z=0`. For every exceptional root
`a in R_A`, define

```text
g_a(z)=Q(z;a)/z=sum_(i=1)^e q_i(a)z^(i-1).          (HSF1)
```

Then `g_a` has degree exactly `e-1`, nonzero constant and leading
coefficients, and splits with `e-1` distinct roots in the set `Z_cl` of
`4e` ordinary clean slopes. Its root set is exactly

```text
Z_a={gamma in Z_cl: Q(gamma;a)=0}.                  (HSF2)
```

The coefficient matrix

```text
G=(q_i(a))_(1<=i<=e, a in R_A)                     (HSF3)
```

has rank `e` and generates the weighted self-dual code from `(HSD3)`:

```text
G D_beta G^T=0.                                     (HSF4)
```

At the sharp high-distance endpoint, the column root sets form one of the
following two exact incidence frames:

1. **Flat:** every ordinary slope belongs to `(e-1)/2` of the `2e` sets
   `Z_a`.
2. **Swapped:** the replication multiset is

   ```text
   {(e+1)/2,(e-3)/2,((e-1)/2)^(4e-2)}.              (HSF5)
   ```

Moreover every `e`-column minor of `G` obeys the complementary weighted
square law `(HSD5)`. Thus either endpoint profile requires a weighted
self-dual frame of `2e` split degree-`e-1` polynomials on `4e` printed
slopes with the displayed replication. Excluding these two frame classes is
a sufficient Hankel-side endpoint theorem; their nonexistence is not proved
here. In fact the exact `e=3,F_101` fixture in `verify.py` realizes the flat
frame with six disjoint root pairs and nonzero self-dual weights. Therefore
split incidence, flat replication, and weighted self-duality alone do not
give a scale-free exclusion; an official proof must additionally use the
Forney values, smooth-domain placement, or large-`e` structure.
