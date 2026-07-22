# `A=1` core-one distance-three quadratic locator-rank gate

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_pair_lagrange_normal_form`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_external_split_design_saturation`

Retain the official pair-Lagrange data. Thus `A` is squarefree of degree
`2e`, its roots are partitioned by pair locators `D_1,...,D_e`, and `B` is
the degree-three canonical locator. Put

```text
U_0=A,       U_i=B A/D_i       (1<=i<=e),
V=span{U_0,...,U_e}.                                  (QLR1)
```

The coefficient space of `Q(z;X)` as a polynomial in `z` is exactly `V`.
Its quadratic product space satisfies the strict pair-Lagrange bound

```text
dim(V V)<=3e+1.                                       (QLR2)
```

Let `C` be the `6e+3` active outside rows supplied by the exact external
design. For `x in C`, let

```text
G_x(z)=product_(gamma in S_x)(z-gamma)
```

be its monic degree-`e` supported-slope locator, and let `g(x)` be the
`e+1` coefficient vector of `G_x`. Form the quadratic locator matrix

```text
M_2=(g_i(x)g_j(x))_(x in C, 0<=i<=j<=e).              (QLR3)
```

Then

```text
rank M_2<=3e+1.                                       (QLR4)
```

Consequently the `6e+3` rows of `M_2` have nullity at least `3e+2`.
Moreover, for `e>=4`, the external locator points lie on at least

```text
binom(e+2,2)-(3e+1)=e(e-3)/2                         (QLR5)
```

linearly independent quadrics in projective coefficient space.

This is a necessary gate, not an exclusion. A proposed external design whose
quadratic locator rank exceeds `3e+1` cannot come from the pair-Lagrange
chart. Passing `(QLR4)` does not prove the resultant power, subgroup
membership, boundary residue conditions, or the original lift.
