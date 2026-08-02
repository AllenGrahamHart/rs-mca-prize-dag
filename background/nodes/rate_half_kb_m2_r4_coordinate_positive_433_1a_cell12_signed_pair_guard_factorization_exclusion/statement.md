# KoalaBear positive 433-1a cell-12 signed-pair guard-factorization exclusion

- **status:** PROVED
- **scope:** common cell `12`, signs `(-1,-1)`, over
  `F_2130706433`; exact source and duplicate-role symmetry transports the
  result to all eight rows in orbit `[12,13]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_vieta_minor_compiler`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_remaining_common_curve_profile`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_product_base_rank_global_certificate`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_quadratic_paired_product_resultant_interface`,
  and
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient`
- **consumer:** `rate_half_band_closure`

The saturated common ideal has a nine-element lex basis.  Exact reduction of
the unique common kernel gives a 17-term plane equation `P(b,t)` of
bidegree `(4,8)`, with leading `b` coefficient `t^4`.  The normalized
kernel has `b`-degree at most three and satisfies `B1(-W)=-B1(W)`.

For squared source labels `w_j=z_j^2`, put `N_j=A0(w_j)`, `D_j=A2(w_j)`,
and `r=rn/rd`.  The complete necessary signed-pair resultant of

```text
N1D0+N0D1=0,
k^2w0(1-w0)^2D1^2-k^2w1(1-w1)^2D0^2-4N0D0D1^2=0              (KBC12-1)
```

reduces modulo `P` to a 36,236-term polynomial `R(w0,b,t)` of degrees
`(16,3,672)`.  Ten bounded pseudo-reductions construct a representative
`C` of a nonzero plane-leading scale times

```text
G=N0D0^5(w0+1)(rd^2w0-rn^2)(rd^2w0+rn^2)^2.      (KBC12-2)
```

If `r16,c16` are the leading `w0` coefficients, exact reduction proves

```text
c16R-r16C=0 modulo P.                              (KBC12-3)
```

The norm `Res_b(P,r16)` has degree 2432.  Its exact factorization has eight
linear factors, three irreducible cubics, and one irreducible decic.  Six
linear roots are compact-kernel scale values.  At the other two roots,
every deployed root of `R(w0)` lies on `N0`, `D0`, `w0=-1`, or
`w0=+/-r^2`; residual quadratics are irreducible.

Five scale fibers are the original `t=0,+/-1,+/-i` label guards and replay
to the unit ideal in the original localized common system.  The sole proper
scale root `t=1117681606` has exactly two deployed common points.  Direct
evaluation of the unnormalized common kernel at both points gives a
nonzero kernel and a complete degree-16 resultant whose every deployed
root again lies on `N0`, `D0`, `w0=-1`, or `w0=+/-r^2`.

Thus no admissible signed pair exists on the main chart or its scale
complement.  Exact symmetry excludes all eight rows in cells `12` and `13`:
orbit `[12,13]` is PROVED excluded.

This leaves two positive `433-1a` representatives / 12 raw rows:
`[9,10]` and `[11]`.  It does not close the positive route, K3, LIST, MCA,
or either Prize problem.

## Falsifier

A failed common-kernel reduction or quotient identity, a missed deployed
norm or scale root, an unguarded main or exceptional lift, or invalid
root-sign/duplicate-role transport.
