# `A=1` distance-three aligned Pade residual has degree at most four

- **status:** PROVED
- **closure:** proof plus exact official incidence certificate
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_pade_large_class_static_denominator`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_external_split_design_saturation`

Let `H` be the official large static Pade relation class, of size `h`, with
static denominator `B` of degree `d<=t`. There is a set of aligned outside
orbit coordinates of size at least

```text
e-33       in the antipodal branch,
e-44       in the constant-product branch.          (QPAR1)
```

For every aligned coordinate `u`, the complement has the common factor
`P_H` and exact form

```text
K_u=P_H R_u,
R_u=R_2U^2+R_1U+R_0 evaluated at U=u,               (QPAR2)
```

where

```text
1<=k=deg_Z R_u=e+d-h<=4.                            (QPAR3)
```

Every `R_u` is a split squarefree divisor of `P_Z/P_H`. For every external
root `gamma` outside `H`, the equation `R_U(gamma)=0` is a nonzero quadratic
in `U`, so that root occurs in at most two aligned residuals.

Thus the final all-deficient support obstruction is a degree-`1,2,3`, or
`4` quadratic pencil containing at least `e-33` or `e-44` distinct split
divisors of the fixed squarefree polynomial `P_Z/P_H`, with no root used
more than twice. The high-degree simultaneous-gcd leaf is eliminated.
