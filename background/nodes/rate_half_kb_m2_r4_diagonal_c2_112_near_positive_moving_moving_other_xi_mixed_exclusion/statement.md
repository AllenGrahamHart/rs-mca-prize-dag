# KoalaBear c2 (1,1,2) near positive moving-moving other-xi mixed exclusion

- **status:** PROVED
- **scope:** deployed field `F_(2130706433^6)`; positive near-aligned source-line
  `(1,1,2)` packets; moving-moving internal template; other relative `xi`
  orbit; mixed residual allocation `c,d -> {1/b,1/d}`.
- **requires:**
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction`
  and
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate`.
- **consumer:** `rate_half_band_closure` (evidence edge).

Normalize `a=2`, `xi=b`, `(eta,ell)=(c,d)`, `w=1/c`, and use moving source
edges `{2,b}` and `{2,1/b}`. Require the residual quadratics at both roots
`c,d` to have root multiset `{1/b,1/d}`. After the stated standard
collision, inversion-fixed, incidence, and endpoint loci are removed, no
deployed-field point satisfies all four residual conditions.

This closes the last of the 18 affine positive near-aligned charts. It does
not classify a negative reconstruction locus, the homogenized `w=0`
boundary, another packet, or the rate-half target itself.
