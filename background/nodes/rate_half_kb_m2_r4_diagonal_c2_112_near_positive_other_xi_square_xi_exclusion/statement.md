# KoalaBear c2 (1,1,2) near positive other-xi square-xi exclusion

- **status:** PROVED
- **scope:** the deployed KoalaBear field `F_(2130706433^6)`; positive
  near-aligned source-line `(1,1,2)` packets; fixed-moving internal
  template; relative orbit `xi in {b,1/b}`; square allocation
  `c -> 1/b, d -> 1/d`
- **dependencies:**
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction`
  and
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate`
- **consumer:** `rate_half_band_closure` (evidence)

Normalize `a=2`, choose the representative `xi=b`, orient
`(eta,ell)=(c,d)`, and put `w=1/c`. This theorem treats

```text
residual c ~ (W-1/b)^2,       residual d ~ (W-1/d)^2.       (KBNMS-1)
```

Each constant-to-leading condition has two non-incidence branches: two
quadratics in `b` over `c`, and two lines in `b` over `d`. For all
four branch pairs, solve the selected `d`-line and impose the selected
`c`-quadratic and both middle-coefficient conditions. After the common
factors `c=1`, `cd=1`, and `5cd-4c-4d+5=0` are saturated, every
projected factor is a collision/fixed-point factor or one of

```text
17d^2-38d+17,   2d^2-9d+1,   2d+1,   2d^2-3d-1.   (KBNMS-2)
```

The first factor occurs only on a leading-zero branch and forces `b=1/2`.
The second and fourth force `b=1/2` and `cd=1`; the linear factor also
forces `b=1/2`. On the overlap between generic and leading-zero projection
support, five saturated generic fibers are empty and the sixth has
`(c,d)=(14/13,-1/2)` with `b=1/2`. The leading-zero fibers at
`d=-2,-1/2` have unit ideals. Exact reduction modulo `p=2130706433`
preserves every support and basis statement. Hence `(KBNMS-1)` is empty
over `F_(p^6)`.

Together with the six earlier charts, 7 of the 18 affine positive charts
are closed. This node does not delete the other 11 affine charts, the
projective boundary, a negative locus, a packet, or the rate-half target.

## Falsifier

An admissible deployed-field solution of `(KBNMS-1)`, or noncollision
support in any primary or independent replay.
