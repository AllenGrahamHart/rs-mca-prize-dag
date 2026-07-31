# KoalaBear c2 (1,1,2) near positive moving-moving tau-xi orbit exclusion

- **status:** PROVED
- **scope:** the deployed KoalaBear field `F_(2130706433^6)`; positive
  near-aligned source-line `(1,1,2)` packets; moving-moving internal template;
  representative `xi=tau(a)`; all three residual-root allocations
- **dependencies:**
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction`
  and
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate`
- **consumer:** `rate_half_band_closure` (evidence)

Normalize `a=2`, orient `(eta,ell)=(c,d)`, put `w=1/c`, and use source
edges `{2,b}` and `{2,1/b}`.  For the `xi=tau(a)` orbit the distinguished
residual root is `2`; the ell root is `1/d`.  This node excludes all three
moving-moving allocations

```text
square-xi:  c->{2,2},     d->{1/d,1/d},
square-ell: c->{1/d,1/d}, d->{2,2},
mixed:      c,d->{2,1/d}.                              (KBMMT-1)
```

After exact finite-incidence removal, reciprocal reduction through
`s=b+1/b`, parent factorization, and deletion of factors bound to the full
forbidden product, the three charts have respectively `3x3`, `3x2`, and
`1x1` nonstandard component pairs.  Their complete modular routers retain
exactly 15, 4, and 10 factors whose residue degrees divide six.  Saturating
the four trace equations by the collision, inversion-fixed, reciprocal,
`z=1`, and finite-incidence product gives the unit ideal for every one of
the 29 factors.

A direct/resultant primary and a no-import audit using fraction-free source
reconstruction and terminal subresultants independently reproduce every
source core, trace lift, parent census, pair projection, residue-degree
sieve, and saturation.  Hence the complete `xi=tau(a)` moving-moving orbit
is empty over the deployed field.

Together with the twelve earlier charts, 15 of the 18 affine positive
charts are closed.  This node does not delete the other reciprocal xi orbit,
the projective `w=0` boundary, a negative locus, a packet, or the rate-half
target.

## Falsifier

An admissible deployed-field solution of any allocation in `(KBMMT-1)`, an
omitted residue-degree-dividing-six factor, or a nonforbidden point in either
certificate path.
