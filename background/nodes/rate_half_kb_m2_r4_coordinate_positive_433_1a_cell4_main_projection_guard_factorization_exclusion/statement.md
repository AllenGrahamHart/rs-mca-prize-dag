# KoalaBear positive 433-1a cell-4 main projection guard-factorization exclusion

- **status:** PROVED
- **scope:** the main compact plane chart in common cell `4`, signs
  `(-1,-1)`, over `F_2130706433`; exact source symmetry transports the result
  to all eight rows in orbit `[4,7]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_cell4_genus1_plane_kernel_reduction`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_cell4_exceptional_scale_chart_exclusion`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_cell4_signed_pair_projection_reconstruction`,
  and
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient`
- **consumer:** `rate_half_band_closure`

Let `P(b,t)` be the compact plane equation and let `F(w0,b,t)` be the
degree-`13` live factor in the necessary signed `DE+/DE-` projection.  Write

```text
ell=(t^2+1)^2,
N0=A0(w0),  D0=A2(w0),
r=rn/rd,    rd=ell,
G=rd^2 w0-rn^2.                                  (KBC4GF-1)
```

Repeated exact pseudo-reduction by `P`, after every multiplication, gives a
polynomial `C` of degrees `(13,3,200)` satisfying

```text
C = ell^21 N0 D0^5 G        modulo P.             (KBC4GF-2)
```

If `f13` and `c13` are the leading `w0` coefficients of `F` and `C`, a
further three plane reductions prove exactly

```text
c13 F-f13 C = 0             modulo P.             (KBC4GF-3)
```

The norm `Res_b(P,f13)` has degree `1124`.  Its exact factorization contains
only the four guarded linear roots `t=+/-1,+/-i`, one irreducible quadratic,
and four irreducible cubics.  Hence `f13` is nonzero at every admissible
deployed point of `P=0`.

An admissible signed pair on the live projection would have `F=0`.
Equations `(KBC4GF-2)--(KBC4GF-3)` would then force

```text
N0 D0 G=0.                                          (KBC4GF-4)
```

This is impossible: `N0` is a nonzero source product record, `D0` is a
denominator guard, and `G!=0` is the source-pair disjointness guard
`w0!=r^2`.  Thus the necessary signed pair is empty on the whole main chart.
The proved exceptional-scale theorem covers every omitted plane scale, and
the root-sign symmetry quotient transports the exclusion to all rows in
cells `4` and `7`.  Therefore orbit `[4,7]` is PROVED excluded.

This closes one positive `433-1a` symmetry orbit.  It does not close the
other five open representatives, the positive route, K3, LIST, MCA, or
either Prize problem.

## Falsifier

A failed quotient-ring identity, an admissible deployed zero of `f13`, an
actual source packet with `N0D0G=0`, an unhandled exceptional plane scale,
or a root-sign row outside the proved symmetry transport.
