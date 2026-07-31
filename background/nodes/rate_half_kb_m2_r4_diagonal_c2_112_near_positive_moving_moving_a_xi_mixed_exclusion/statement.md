# KoalaBear c2 (1,1,2) near positive moving-moving a-xi mixed exclusion

- **status:** PROVED
- **scope:** the deployed KoalaBear field `F_(2130706433^6)`; positive
  near-aligned source-line `(1,1,2)` packets; moving-moving internal template;
  representative `xi=a`; mixed allocation `c,d->{1/2,1/d}`
- **dependencies:**
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction`
  and
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate`
- **consumer:** `rate_half_band_closure` (evidence)

Normalize `a=xi=2`, orient `(eta,ell)=(c,d)`, put `w=1/c`, and use
moving-moving source edges `{2,b}` and `{2,1/b}`. Require both residuals to
have the two distinct roots `1/2,1/d`. After removing the finite-incidence
square, the four product/sum conditions are reciprocal in `b`. Under
`s=b+1/b`, their degrees in `(s,c,d)` are

```text
c product (2,8,7),  c sum (2,12,9),
d product (2,6,7),  d sum (2,10,9).                 (KBMMAM-1)
```

Eliminating `s` leaves exactly one nonstandard parent component on each side,
of bidegrees `(8,10)` and `(8,6)`. Their sole pair projection has degree 128.
Besides standard support, its characteristic-zero factor degrees are
`2,12,12,32`. Modulo `p=2130706433`, the complete nonstandard degree census
is

```text
1,1,1,1, 2,2,2,2,2, 3, 5, 7, 29.                 (KBMMAM-2)
```

The degree-5, degree-7, and degree-29 factors cannot meet `F_(p^6)`. For each
of the remaining four linear, five quadratic, and one cubic factors,
adjoining all equations `(KBMMAM-1)` and saturating by the complete collision,
inversion-fixed, reciprocal, `z=1`, and finite-incidence product gives the
unit ideal. A direct/resultant primary and a no-import audit with a
fraction-free source shard and terminal-subresultant router reproduce the
full census and all ten saturations. Hence this chart is empty over the
deployed field.

Together with the eleven earlier charts, 12 of the 18 affine positive charts
are closed, including every `xi=a` chart. This node does not delete the six
charts in the other two relative xi orbits, the projective boundary, a
negative locus, a packet, or the rate-half target.

## Falsifier

An admissible deployed-field solution of `(KBMMAM-1)`, an omitted
residue-degree-dividing-six factor, or a nonforbidden point in either
certificate path.
