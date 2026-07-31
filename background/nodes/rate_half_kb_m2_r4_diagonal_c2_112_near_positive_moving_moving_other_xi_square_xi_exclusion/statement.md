# KoalaBear c2 (1,1,2) near positive moving-moving other-xi square-xi exclusion

- **status:** PROVED
- **scope:** the deployed KoalaBear field `F_(2130706433^6)`; positive
  near-aligned source-line `(1,1,2)` packets; moving-moving internal template;
  representative `xi=b`; square allocation `c->1/b,d->1/d`
- **dependencies:**
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction`
  and
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate`
- **consumer:** `rate_half_band_closure` (evidence)

Normalize `a=2`, orient `(xi,eta,ell)=(b,c,d)`, put `w=1/c`, and use
moving-moving source edges `{2,b}` and `{2,1/b}`. Require

```text
residual c ~ (W-1/b)^2,       residual d ~ (W-1/d)^2.       (KBMMOS-1)
```

After removing the exact finite-incidence square, the two `c` conditions
have b-degrees six and five. The product condition splits into two cubic
branches. Eliminating each cubic against the sum condition leaves exactly
two nonstandard parent components in total, of bidegrees `(4,3)` and
`(18,14)`. The `d` conditions remain reciprocal in `b`; reduction through
`s=b+1/b` leaves three nonstandard parent components. Thus there are six
exhaustive parent-component pairs.

Complete characteristic-zero and deployed-prime factorizations of the six
pair projections leave exactly eight nonstandard irreducible factors whose
residue degrees divide six: seven linear and one quadratic. Every other
factor has degree `4,5,8,9,14,15`, or `20`. For each retained factor, the
four primitive equations saturated by the complete collision,
inversion-fixed, reciprocal, `z=1`, and finite-incidence product give the
unit ideal. A direct/resultant primary and a no-import fraction-free and
terminal-subresultant audit reproduce the full route. Hence `(KBMMOS-1)` is
empty over the deployed field.

Together with the fifteen earlier charts, 16 of the 18 affine positive
charts are closed. This node does not delete the swapped or mixed allocation
in this orbit, the projective `w=0` boundary, a negative locus, a packet, or
the rate-half target.

## Falsifier

An admissible deployed-field solution of `(KBMMOS-1)`, an omitted
degree-dividing-six modular factor, or a nonforbidden point in either
certificate path.
