# `A=1` core-one distance-three resultant-power equivalence

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_dual_row_product_power_router`,
  `rate_half_residual_prime_field_collapse`

Retain the official pair-Lagrange data and let `C(X)` be the squarefree monic
locator of the `6e+3` active outside rows. Put

```text
r=2e+1,       q_e(X)=[z^e]Q(z;X),
Delta(X)=Res_z(Q(z;X),partial_z Q(z;X)),              (RPE1)
H(z)=Res_X(C(X),Q(z;X)),
L=Res_X(C,q_e).                                       (RPE2)
```

Then the exact external split design exists if and only if both conditions
below hold.

1. Every active-row polynomial has exact degree `e` and is squarefree:

   ```text
   gcd(C,q_e Delta)=1.                                (RPE3)
   ```

2. There is a monic squarefree polynomial `P_Z` of degree `3e`, split over
   the base field, such that

   ```text
   H=L P_Z^r.                                         (RPE4)
   ```

When these conditions hold, the design is unique and reconstructed by

```text
Z_ext=roots(P_Z),
G_gamma={x:C(x)=0 and Q(gamma;x)=0}.                  (RPE5)
```

Every row in `(RPE5)` has degree `e` and every block has size `r`; hence the
incidence matrix and all external locators are outputs, not search variables.

On the official residual fields, `F=F_p` with `p>2^167`, while

```text
deg H=e(6e+3)=3er<2^79.                               (RPE6)
```

Therefore `p` divides neither `r` nor any relevant derivative degree. The
candidate in `(RPE4)` is uniquely recovered without factor multiplicities:

```text
P_Z=monic(H/gcd(H,H')).                               (RPE7)
```

Thus the live distance-three decision contains no independent external
slope, block, locator, incidence, or `P_Z` variable. It is exactly a compact
row-discriminant test followed by a split perfect-power test for one
resultant.
