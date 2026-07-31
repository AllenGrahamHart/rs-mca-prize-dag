# KoalaBear c2 (1,1,2) near positive other-xi mixed exclusion

- **status:** PROVED
- **scope:** the deployed KoalaBear field `F_(2130706433^6)`; positive
  near-aligned source-line `(1,1,2)` packets; fixed-moving internal
  template; representative `xi=b`; mixed allocation `c,d -> {1/b,1/d}`
- **dependencies:**
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction`
  and
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate`
- **consumer:** `rate_half_band_closure` (evidence)

Normalize `a=2`, choose `xi=b`, orient `(eta,ell)=(c,d)`, and put
`w=1/c`. At each q-root `c,d`, require the two residual roots to be the
distinct values `1/b,1/d`. After removing the finite-incidence square, the
four product/sum conditions have degrees

```text
c product (3,6,5), c sum (3,10,7),
d product (3,6,5), d sum (3,10,7)                 (KBNMM-1)
```

in `(b,c,d)`. Their within-root resultants have exactly one low component
of bidegree `(3,2)` and one high component of bidegree `(16,14)`, besides
printed forbidden factors.

The four low/high component pairs are exhaustive. Low/low leaves only
standard support, `19d-17`, and `2d^3-19d^2+19d-14`. Low/high and high/low
leave respective degree-40 factors whose deployed modular degree censuses
are `[1,2,2,4,4,27]` and `[1,1,6,32]`. For high/high, the cross-product
resultant leaves two nonstandard components. Projecting the high within-`c`
component against them gives deployed factors of degrees

```text
1,1,1,2,2,2,4,5,7,7
and
1,1,1,1,1,2,2,3,3,4,6,7,7,8,11,12,17,25,52.   (KBNMM-2)
```

Only residue degrees dividing six can enter `F_(p^6)`. Every such
nonstandard fiber in `(KBNMM-1)`--`(KBNMM-2)` is empty or consists only of
collision, inversion-fixed, reciprocal, `z=1`, or finite-incidence points.
A direct/resultant primary and a no-import fraction-free/subresultant audit
with an independently written residue-field checker reproduce this
classification. Hence this mixed chart is empty over the deployed field.

Together with the eight earlier charts, 9 of the 18 affine positive charts
are closed. This node does not delete the other nine affine positive charts,
the projective boundary, a negative locus, a packet, or the rate-half target.

## Falsifier

An admissible deployed-field solution of `(KBNMM-1)`, an omitted modular
factor of residue degree dividing six, or a nonforbidden point in either
certificate path.
