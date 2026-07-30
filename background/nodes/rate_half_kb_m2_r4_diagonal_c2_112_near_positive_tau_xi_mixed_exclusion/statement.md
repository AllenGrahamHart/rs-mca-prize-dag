# KoalaBear c2 (1,1,2) near positive reciprocal-xi mixed exclusion

- **status:** PROVED
- **scope:** the deployed KoalaBear field `F_(2130706433^6)`; positive
  near-aligned source-line `(1,1,2)` packets; fixed-moving internal template;
  relative orbit `xi=tau(a)`; mixed residual allocation only
- **dependencies:**
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction`
  and
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate`
- **consumer:** `rate_half_band_closure` (evidence)

Normalize the common endpoint to `a=2`, take `xi=tau(a)=1/2`, orient
`(eta,ell)=(c,d)`, and put `w=1/c`. In this mixed allocation,

```text
residual over c = scalar * (W-2)(W-1/d),
residual over d = scalar * (W-2)(W-1/d).          (KBNTM-1)
```

After explicit finite-chart and collision factors are removed, the two
within-fiber resultants share one bidegree-`(8,6)` residual curve. The
cross-product resultant has two retained factors of bidegrees `(2,1),(6,5)`;
the cross-sum resultant has three of bidegrees `(1,1),(4,3),(10,8)`.
Projecting their intersections with the residual curve gives degree-96 and
degree-186 polynomials whose squarefree gcd is

```text
(d-2)(d-1)(2d-1).                                (KBNTM-2)
```

An independent fraction-free reconstruction eliminates in the opposite
variable and obtains `(c-2)(c-1)(2c-1)`. Both identities persist modulo
`p=2130706433`; every root is a forbidden collision or inversion-fixed
label. Therefore this chart is empty over `F_(p^6)`.

Together with the three fixed-`xi` allocation theorems, 4 of the 18 affine
positive charts are closed. This node does not delete the other 14 affine
charts, the projective boundary, a negative locus, a packet, or the rate-half
target.

## Falsifier

An admissible deployed-field solution of `(KBNTM-1)` or noncollision support
in either projected gcd replay.
