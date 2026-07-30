# KoalaBear c2 (1,1,2) near positive fixed-xi mixed exclusion

- **status:** PROVED
- **scope:** the deployed KoalaBear field `F_(2130706433^6)`; positive
  near-aligned source-line `(1,1,2)` packets; fixed-moving internal template;
  relative orbit `xi=a`; mixed residual allocation only
- **dependencies:**
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction`
  and
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate`
- **consumer:** `rate_half_band_closure` (evidence)

Normalize `a=xi=2`, orient `(eta,ell)=(c,d)`, and put `w=1/c`. In the mixed
allocation, each residual quadratic has both target roots:

```text
residual over c = scalar * (W-1/2)(W-1/d),
residual over d = scalar * (W-1/2)(W-1/d).        (KBNMX-1)
```

After the finite-incidence and collision factors are removed, the two
conditions over either q-root are quadratic in the internal label `b`. Their
within-fiber resultants have one common residual curve `R(c,d)` of bidegree
`(8,6)`. The cross-product resultant has two admissible factors of bidegrees
`(2,1),(6,5)`, while the cross-sum resultant has three of bidegrees
`(1,1),(4,3),(10,8)`.

Projecting the intersections of `R` with the two product factors and the
three sum factors gives univariate polynomials of degrees 96 and 186. Their
squarefree gcd is

```text
(d-2)(d-1)(2d-1).                                (KBNMX-2)
```

An independent fraction-free reconstruction eliminates in the opposite
variable and obtains `(c-2)(c-1)(2c-1)`. Both gcd identities persist modulo
`p=2130706433`. Every root in these supports is a forbidden label collision
or inversion-fixed label. Therefore the mixed chart is empty over
`F_(p^6)`.

Together with the two square-allocation theorems, 3 of the 18 affine
positive charts are closed. This node does not delete the other 15 affine
charts, the projective `w=0` boundary, a negative locus, a full packet, or
the rate-half target.

## Falsifier

An admissible deployed-field solution of `(KBNMX-1)`, a noncollision factor
in either projected support gcd, or failure of the opposite-variable replay.
