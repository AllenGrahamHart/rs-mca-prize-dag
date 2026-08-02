# KoalaBear positive 433-1a cell-9 signed-pair guard-factorization exclusion

- **status:** PROVED
- **scope:** common cell `9`, signs `(-1,-1)`, over
  `F_2130706433`; exact source and duplicate-role symmetry transports the
  result to all eight root-sign rows in orbit `[9,10]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_vieta_minor_compiler`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_remaining_common_curve_profile`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_product_base_rank_global_certificate`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_quadratic_paired_product_resultant_interface`,
  and
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient`
- **consumer:** `rate_half_band_closure`

The saturated common ideal has an eleven-element lex basis.  Exact reduction
of the unique common kernel gives a 45-term plane equation `P(b,t)` of
bidegree `(4,8)`.  The normalized kernel has `b`-degree at most three and
satisfies `B1(-W)=-B1(W)`.

The complete necessary signed-pair resultant reduces modulo `P` to a
36,876-term polynomial `R(w0,b,t)` of degrees `(16,3,587)`.  Seven bounded
pseudo-reductions construct a representative `C` of a nonzero
plane-leading scale times

```text
G=N0D0^5(w0+1)(w0-t^2)^2(rd^2w0-rn^2).           (KBC9-1)
```

For the leading `w0` coefficients `r16,c16`, exact reduction proves

```text
c16R-r16C=0 modulo P.                              (KBC9-2)
```

The norm `Res_b(P,r16)` has degree 2344.  Its exact factorization has five
linear factors, two irreducible quadratics, and three irreducible cubics.
Its only base-field roots are

```text
t=0,1,i,-i,-1.
```

These are exactly the base-field roots of all six compact-kernel scales.
Each is an original source guard, and direct replay in the original
localized common ideal gives the unit ideal at every value.

Thus no admissible signed pair exists on the main chart or its scale
complement.  Exact root-sign and duplicate-role symmetry excludes all eight
rows of cells `9` and `10`: orbit `[9,10]` is PROVED excluded.  No positive
`433-1a` common-orbit representative remains.

This node does not by itself close K3, LIST, MCA, or either Prize problem.

## Falsifier

A failed common-kernel reduction or quotient identity, a missed deployed
norm or scale root, a nonunit exceptional common chart, or invalid symmetry
transport.
