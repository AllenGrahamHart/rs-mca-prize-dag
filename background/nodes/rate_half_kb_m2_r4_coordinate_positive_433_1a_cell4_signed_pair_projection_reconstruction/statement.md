# KoalaBear positive 433-1a cell-4 signed-pair projection and reconstruction

- **status:** PROVED
- **scope:** main common matching cell `4`, signs `(-1,-1)`, over
  `F_2130706433`; source symmetry transports the reduction to cell `7`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_cell4_genus1_plane_kernel_reduction`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_cell4_exceptional_scale_chart_exclusion`,
  and
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient`
- **consumer:** `rate_half_band_closure`

Put `w_j=z_j^2`.  After reducing the necessary signed `DE+/DE-` pair by the
cell-4 plane equation and eliminating `w1`, the primitive projection factors
exactly as

```text
2058485041 (w0+1)^2 (w0-t^2) F(w0,b,t),         (KBC4SP-1)
```

where `F` is irreducible, has degrees `(13,3,284)` in `(w0,b,t)`, and has
`15792` terms.  The main source guards exclude `w0=-1` and `w0=t^2`.
Consequently every guarded signed-pair solution lies on `F=0`.

Pseudo-dividing the quartic signed equation by the quadratic one in `w1`
takes three steps and leaves a linear remainder.  The exact resultant identity
has leading-coefficient exponent three.  Reducing the two remainder
coefficients by the plane takes nine equal-scale steps.  Their common scale is

```text
(t-1)^5 (t+1)^7 (t+i)^45 (t-i)^49,
i=16711679, i^2=-1,                              (KBC4SP-2)
```

and their remaining polynomial gcd is `w0+1`.  All factors in `(KBC4SP-2)`
and `w0+1` are nonzero on the main chart.  Canceling them gives the exact
necessary relation

```text
L(w0,b,t) w1 + t M(w0,b,t) = 0.                 (KBC4SP-3)
```

Both `L` and `M` are irreducible and distinct.  Their respective degrees are
`(9,3,181)` and `(9,3,180)`, with `7176` and `7136` terms.  Thus `(KBC4SP-3)`
reconstructs `w1=-tM/L` wherever `L!=0`.  On `L=0`, a genuine signed-pair
solution must also satisfy `M=0`; that exceptional coefficient chart remains
open, with no dimensional claim in this node.

This node proves a necessary component reduction and reconstruction only.  It
does not impose the colored `BE` equations, exclude the `L=M=0` chart, exclude
cell 4 or 7, or close the positive route, K3, LIST, MCA, or either Prize
problem.

## Falsifier

A failed resultant reconstruction, an additional irreducible projection
factor, a canceled factor not covered by an original main-chart guard, a
nonlinear pseudo-remainder, a common factor of `L` and `tM`, or treating the
necessary projection as sufficient.
