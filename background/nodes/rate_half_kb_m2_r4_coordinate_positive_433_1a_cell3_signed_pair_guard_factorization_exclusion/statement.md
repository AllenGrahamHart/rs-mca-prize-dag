# KoalaBear positive 433-1a cell-3 signed-pair guard-factorization exclusion

- **status:** PROVED
- **scope:** the compact main chart in common cell `3`, signs `(-1,-1)`,
  over `F_2130706433`; exact source symmetry transports the result to all
  eight rows in orbit `[3,6]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_cell3_genus3_plane_kernel_reduction`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_cell3_exceptional_scale_chart_exclusion`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_quadratic_paired_product_resultant_interface`,
  and
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient`
- **consumer:** `rate_half_band_closure`

Let `P(b,t)` be the 25-term compact plane equation.  For two squared source
labels `w_j=z_j^2`, the necessary signed `DE+/DE-` equations have degrees
two and four in `w1`.  Reduce both equations by `P`, eliminate `w1`, and
reduce the resultant again.  The exact projected polynomial `R(w0,b,t)` has
degrees `(16,3,531)` and `35876` terms.

Put

```text
N0=A0(w0),   D0=A2(w0),   r=rn/rd,
G=N0 D0^5 (w0+1)(w0-t^2)(rd^2w0-rn^2)^2.       (KBC3GF-1)
```

Eight bounded plane pseudo-reductions give a 17,380-term representative `C`
of a nonzero plane-leading scale times `G`.  If `r16,c16` are the leading
`w0` coefficients of `R,C`, three further reductions prove exactly

```text
c16 R-r16 C = 0 modulo P.                         (KBC3GF-2)
```

The norm `Res_b(P,r16)` factors into ten linear, three irreducible quadratic,
and three irreducible cubic factors.  Six linear roots are exactly the
already-closed exceptional-scale values

```text
0, +1, -1, +i, -i, 1288361599.                    (KBC3GF-3)
```

At the other four roots, exact specialization of `gcd(P,r16)` gives a finite
atlas.  Two roots lift only to `b=-1`, violating the original guard `b+1`.
The other two roots have two deployed `b` lifts each; every deployed root of
`R(w0)` lies on `N0`, `D0`, `w0=-1`, `w0=t^2`, or `w0=r^2`.  Nonlinear
factors have no base-field root.

Away from this complete leading atlas, `(KBC3GF-2)` and `R=0` force `G=0`.
Every factor of `G` is an original nonzero product, denominator, or source-
label disjointness guard.  Hence no necessary signed pair exists on the main
chart.  The exceptional-scale theorem covers every omitted scale, and exact
symmetry transports the result to all rows in cells `3` and `6`.  Therefore
orbit `[3,6]` is PROVED excluded.

This leaves four positive `433-1a` representatives / 24 raw rows.  It does
not close those representatives, the positive route, K3, LIST, MCA, or
either Prize problem.

## Falsifier

A failed resultant or quotient-ring identity, a missed norm root, an
unguarded deployed point in the leading atlas, a factor of `(KBC3GF-1)` not
covered by an original guard, or invalid symmetry transport.
