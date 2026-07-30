# KoalaBear c2 (1,1,2) near positive fixed-xi swapped-square exclusion

- **status:** PROVED
- **scope:** the deployed KoalaBear field `F_(2130706433^6)`; positive
  near-aligned source-line `(1,1,2)` packets; fixed-moving internal template;
  relative orbit `xi=a`; swapped square allocation only
- **dependencies:**
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction`
  and
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate`
- **consumer:** `rate_half_band_closure` (evidence)

Normalize `a=xi=2`, orient `(eta,ell)=(c,d)`, and put `w=1/c`. This theorem
interchanges the two target roots from the direct-square chart:

```text
residual over c = scalar * (W-1/d)^2,
residual over d = scalar * (W-1/2)^2.              (KBNSW-1)
```

For all four endpoint-line pairs, the two middle-coefficient resultants have
gcd support contained in

```text
d in {2,1,-1,1/2}.                                (KBNSW-2)
```

All values in `(KBNSW-2)` are forbidden collisions or inversion-fixed
labels. One left-line leading-zero locus has only that support. The other has
one additional component

```text
7c+17d-30=0,       17d^2-38d+17=0,                (KBNSW-3)
```

and `(KBNSW-3)` forces `5cd-4c-4d+5=0`, equivalently the excluded label
`z=1`. Exact reduction modulo `p=2130706433` preserves all squarefree support
statements. Therefore this swapped q-slice chart is empty over `F_(p^6)`.

Together with the direct-square theorem, 2 of the 18 affine positive charts
are closed. This node does not delete the other 16 affine charts, the
projective `w=0` boundary, a negative locus, a full packet, or the rate-half
target.

## Falsifier

An admissible deployed-field solution of `(KBNSW-1)`, failure of the
component identity in `(KBNSW-3)`, or a noncollision factor in either modular
gcd replay.
