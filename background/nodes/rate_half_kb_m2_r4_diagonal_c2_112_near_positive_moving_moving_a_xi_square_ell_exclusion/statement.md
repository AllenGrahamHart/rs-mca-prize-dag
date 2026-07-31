# KoalaBear c2 (1,1,2) near positive moving-moving a-xi square-ell exclusion

- **status:** PROVED
- **scope:** the deployed KoalaBear field `F_(2130706433^6)`; positive
  near-aligned source-line `(1,1,2)` packets; moving-moving internal template;
  representative `xi=a`; square allocation `c->1/d`, `d->1/2`
- **dependencies:**
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction`
  and
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate`
- **consumer:** `rate_half_band_closure` (evidence)

Normalize `a=xi=2`, orient `(eta,ell)=(c,d)`, put `w=1/c`, and use
moving-moving source edges `{2,b}` and `{2,1/b}`. Require the residual over
`c` to have double root `1/d` and the residual over `d` to have double root
`1/2`. After removing the finite-incidence square, the four product/sum
conditions are reciprocal in `b`. Under `s=b+1/b`, their degrees in
`(s,c,d)` are

```text
c product (2,8,8),  c sum (2,12,9),
d product (2,5,6),  d sum (2,9,8).                  (KBMMAE-1)
```

Eliminating `s` leaves three nonstandard components over `c`, of bidegrees
`(2,1),(2,3),(4,4)`, and two over `d`, of bidegrees `(2,1),(4,2)`. The six
component pairs are exhaustive. One has only standard support. The other five
introduce respectively a linear, cubic, degree-nine, degree-five, and another
degree-nine factor. Modulo `p=2130706433`, the degree-five and both degree-nine
factors
remain irreducible and cannot meet `F_(p^6)`; the linear and cubic give four
distinct linear fibers.

For each of those four fibers, adjoining all equations `(KBMMAE-1)` and
saturating by the complete collision, inversion-fixed, reciprocal, `z=1`,
and finite-incidence product gives the unit ideal. A direct/resultant primary
and a no-import fraction-free/subresultant audit reproduce the complete
census and all four saturations. Hence this chart is empty over the deployed
field.

Together with the ten earlier charts, 11 of the 18 affine positive charts
are closed. This node does not delete the other seven moving-moving charts,
the projective boundary, a negative locus, a packet, or the rate-half target.

## Falsifier

An admissible deployed-field solution of `(KBMMAE-1)`, a failure of its
reciprocal lift, an omitted residue-degree-dividing-six factor, or a
nonforbidden point in either certificate path.
