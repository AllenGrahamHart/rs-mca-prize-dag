# KoalaBear c2 (1,1,2) near positive moving-moving other-xi square-ell exclusion

- **status:** PROVED
- **scope:** the deployed KoalaBear field `F_(2130706433^6)`; positive
  near-aligned source-line `(1,1,2)` packets; moving-moving internal template;
  representative `xi=b`; swapped square allocation `c->1/d,d->1/b`
- **dependencies:**
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction`
  and
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate`
- **consumer:** `rate_half_band_closure` (evidence)

Normalize `a=2`, orient `(xi,eta,ell)=(b,c,d)`, put `w=1/c`, and use
moving-moving source edges `{2,b}` and `{2,1/b}`. Require

```text
residual c ~ (W-1/d)^2,       residual d ~ (W-1/b)^2.       (KBMMOS-2)
```

After removing the exact finite-incidence square, both `c` conditions have
b-degree four and remain reciprocal in `b`. Reduction through `s=b+1/b`
leaves exactly three nonstandard parent components, of bidegrees `(2,3)`,
`(4,4)`, and `(2,1)`. The `d` product and sum conditions have b-degrees six
and five. The product splits into two cubic branches; eliminating each
against the sum leaves exactly two nonstandard parent components in total,
of bidegrees `(3,3)` and `(16,12)`. Thus there are six exhaustive
parent-component pairs.

Complete characteristic-zero and deployed-prime factorizations of the six
pair projections leave exactly 22 nonstandard irreducible factors whose
residue degrees divide six: ten linear, nine quadratic, one cubic, and two
sextic factors; two of the linear factors occur with multiplicity two.
Every other factor has degree `10,11,13`, or `20`. For each retained
factor, the four primitive equations saturated by the complete collision,
inversion-fixed, reciprocal, `z=1`, and finite-incidence product give the
unit ideal. A direct/resultant primary and a no-import fraction-free and
terminal-subresultant audit reproduce the full route. Hence `(KBMMOS-1)` is
empty over the deployed field.

Together with the sixteen earlier charts, 17 of the 18 affine positive
charts are closed. This node does not delete the mixed allocation in this
orbit, the projective `w=0` boundary, a negative locus, a packet, or the
rate-half target.

## Falsifier

An admissible deployed-field solution of `(KBMMOS-2)`, an omitted
degree-dividing-six modular factor, or a nonforbidden point in either
certificate path.
