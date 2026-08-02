# KoalaBear positive 433-1a cell-14 signed-pair guard-factorization exclusion

- **status:** PROVED
- **scope:** common cell `14`, signs `(-1,-1)`, over
  `F_2130706433`; exact source symmetry transports the result to all four
  root-sign rows in orbit `[14]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_vieta_minor_compiler`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_remaining_common_curve_profile`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_product_base_rank_global_certificate`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_quadratic_paired_product_resultant_interface`,
  and
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient`
- **consumer:** `rate_half_band_closure`

Exact lex reduction of the saturated common ideal gives an eight-element
basis.  It yields a 17-term compact plane equation `P(b,t)` of bidegree
`(4,8)`, with leading `b` coefficient `t^4`, and rational expressions for
`r`, `c`, and the unique common kernel.  The normalized kernel has
`b`-degree at most three and satisfies `B1(-W)=-B1(W)`.

For squared source labels `w_j=z_j^2`, put

```text
N_j=A0(w_j),  D_j=A2(w_j),  r=rn/rd.
```

The two necessary signed-pair equations are

```text
N1 D0+N0 D1=0,
k^2 w0(1-w0)^2 D1^2-k^2 w1(1-w1)^2 D0^2-4N0D0D1^2=0. (KBC14-1)
```

Their complete `w1` resultant, reduced by `P`, is a 41,556-term polynomial
`R(w0,b,t)` of degrees `(16,3,752)`.  Nine bounded pseudo-reductions give a
15,580-term representative `C` of a nonzero power of the plane-leading
coefficient times

```text
G=N0 D0^5 (w0+1)^2 (rd^2w0-rn^2)(rd^2w0+rn^2). (KBC14-2)
```

Writing `r16,c16` for the leading `w0` coefficients of `R,C`, three more
reductions prove exactly

```text
c16 R-r16 C=0 modulo P.                            (KBC14-3)
```

The norm `Res_b(P,r16)` has degree `2752`.  Its exact factorization has
eight linear factors and irreducible factors of degrees three, five, and
six.  Seven nontrivial linear fibers lift only to `b=0,+1,-1`, except for
one fiber with two deployed `b` lifts.  At those two lifts every deployed
root of `R(w0)` lies on `N0`, `D0`, `w0=-1`, `w0=r^2`, or `w0=-r^2`;
the residual quadratic factors are irreducible.  Thus the complete leading
atlas contains no admissible point.

Every denominator, projective, projected, and plane-leading scale omitted
by the compact chart factors over the deployed field.  The only linear
roots are `t=0,+/-1,+/-i`; the other factors are irreducible cubics.  All
five linear fibers are original source-label guards, and direct replay in
the original saturated common ideal gives the unit ideal at each one.

Away from these complete exception ledgers, `(KBC14-1)` forces `R=0`, then
`(KBC14-3)` forces `G=0`.  Every factor of `G` is an original product,
denominator, or source-label disjointness guard, a contradiction.  Exact
root-sign symmetry therefore excludes all four rows of cell `14`: orbit
`[14]` is PROVED excluded.

This leaves three positive `433-1a` representatives / 20 raw rows:
`[9,10]`, `[11]`, and `[12,13]`.  It does not close the positive route, K3,
LIST, MCA, or either Prize problem.

## Falsifier

A failed common-kernel reduction or quotient identity, a missed deployed
scale or leading-norm root, an unguarded finite lift, a factor of
`(KBC14-2)` not covered by an original guard, or invalid symmetry transport.
