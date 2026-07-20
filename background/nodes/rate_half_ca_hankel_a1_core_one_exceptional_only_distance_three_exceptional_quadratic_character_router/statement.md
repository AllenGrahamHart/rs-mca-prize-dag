# `A=1` distance-three exceptional quadratic-character router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_matching_free_boundary_power_router`,
  `rate_half_residual_prime_field_collapse`

Retain the official distance-three support packet over its proved prime field
`F_p`. Let `s` be the stripped core row, `x_0` the omitted row, and `A` the
monic degree-`2e` exceptional locator. If any perfect matching can pass the
boundary root-unity gates, then

```text
-A(0)A(s)A(x_0) in (F_p^*)^2.                       (EQR1)
```

Equivalently, the support-only Legendre test is

```text
(-A(0)A(s)A(x_0))^((p-1)/2)=1.                      (EQR2)
```

Every factor is nonzero. This gate depends only on the exceptional support
and the two removed domain rows. It is checked before the triple, pair
matching, dual `r`-th-power classes, internal slopes, or fiber scalars.

The quadratic-character condition is necessary, not sufficient for central
symmetry or for the external split design.
