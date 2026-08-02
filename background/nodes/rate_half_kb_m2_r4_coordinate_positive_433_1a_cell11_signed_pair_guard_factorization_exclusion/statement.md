# KoalaBear positive 433-1a cell-11 signed-pair guard-factorization exclusion

- **status:** PROVED
- **scope:** common cell `11`, signs `(-1,-1)`, over
  `F_2130706433`; exact source symmetry transports the result to all four
  root-sign rows in orbit `[11]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_vieta_minor_compiler`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_remaining_common_curve_profile`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_product_base_rank_global_certificate`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_quadratic_paired_product_resultant_interface`,
  and
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient`
- **consumer:** `rate_half_band_closure`

The saturated common ideal has a ten-element lex basis.  Exact reduction of
the unique common kernel gives a 45-term plane equation `P(b,t)` of
bidegree `(4,8)`.  The normalized kernel has `b`-degree at most three and
satisfies `B1(-W)=-B1(W)`.

The complete necessary signed-pair resultant reduces modulo `P` to a
42,316-term polynomial `R(w0,b,t)` of degrees `(16,3,667)`.  Nine bounded
pseudo-reductions construct a representative `C` of a nonzero
plane-leading scale times

```text
G=N0D0^5(w0-t^2)^2(rd^2w0-rn^2)(rd^2w0+rn^2).    (KBC11-1)
```

For the leading `w0` coefficients `r16,c16`, exact reduction proves

```text
c16R-r16C=0 modulo P.                              (KBC11-2)
```

The norm `Res_b(P,r16)` has degree 2664.  Its exact factorization has ten
linear factors, two irreducible cubics, and one irreducible septic.  Seven
linear roots are compact-kernel scale values.  Two further roots lift only
to `b=-1`; at the remaining root `t=989155728`, every deployed root of
`R(w0)` lies on `N0`, `D0`, `w0=t^2`, or `w0=+/-r^2`.

Exact factorization of all six compact-kernel scales gives seven base-field
roots.  Direct replay at every root in the original localized common ideal
gives the unit ideal, including the nontrivial values `1231496538` and
`1620586492`.

Thus no admissible signed pair exists on the main chart or its scale
complement.  Exact root-sign symmetry excludes all four rows of cell `11`:
orbit `[11]` is PROVED excluded.

This leaves one positive `433-1a` representative / eight raw rows:
`[9,10]`.  It does not close the positive route, K3, LIST, MCA, or either
Prize problem.

## Falsifier

A failed common-kernel reduction or quotient identity, a missed deployed
norm or scale root, an unguarded finite lift, or invalid symmetry transport.
