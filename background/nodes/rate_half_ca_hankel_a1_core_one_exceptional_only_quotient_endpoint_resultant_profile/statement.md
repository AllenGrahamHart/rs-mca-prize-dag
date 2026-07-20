# `A=1` exceptional quotient endpoint resultant profile

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_distance_sharp_ceiling`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_two_sided_resultant_saturation`

Retain the sharp endpoint

```text
e=2^38-1,       r=2e+1,
h=3(e+1)/2-1,       k_0=(e-1)/2.                      (QER1)
```

Let `z=0` be the exceptional slope, let

```text
P_ord(z)=product_(zeta ordinary supported)(z-zeta),
```

and use the monic-first resultant

```text
R_A(z)=Res_X(A(X),Q(z;X))
      =product_(a:A(a)=0)Q(z;a).                       (QER2)
```

There is a nonzero field scalar `kappa` such that exactly one of the following
two profiles holds.

1. **Flat profile.** Every ordinary complement has size `3(e+1)/2`, and

   ```text
   R_A(z)=kappa z^(2e) P_ord(z)^k_0.                   (QER3)
   ```

2. **Swapped profile.** Let `z_min` be the unique ordinary slope with minimal
   complement size `h`, and let `z_max` be the unique slope with complement
   size `3(e+1)/2+1`. Then

   ```text
   (z-z_max)R_A(z)
    =kappa z^(2e)(z-z_min)P_ord(z)^k_0.                (QER4)
   ```

Put `H_A=P_X/A` and `K_0=3(e+1)/2=r-k_0`. The complementary resultant is
also forced. In the flat profile,

```text
Res_X(H_A,Q)=kappa' P_ord^K_0,                         (QER5)
```

while in the swapped profile,

```text
(z-z_min)Res_X(H_A,Q)
 =kappa'(z-z_max)P_ord^K_0.                            (QER6)
```

Here `kappa'` is nonzero. In particular, the exceptional slope is absent
from the complementary resultant and the two linear-factor deviations are
opposite.

Conversely, within either sharp-endpoint incidence profile, `(QER3)` or
`(QER4)`, together with `(QER5)` or `(QER6)`, records every exceptional and
complementary ordinary-slope incidence with its exact multiplicity. The
theorem is a necessary endpoint certificate; it does not prove that either
resultant profile is impossible.
