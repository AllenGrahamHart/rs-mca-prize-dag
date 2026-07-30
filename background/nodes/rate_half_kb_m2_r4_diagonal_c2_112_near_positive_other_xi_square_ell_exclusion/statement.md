# KoalaBear c2 (1,1,2) near positive other-xi square-ell exclusion

- **status:** PROVED
- **scope:** the deployed KoalaBear field `F_(2130706433^6)`; positive
  near-aligned source-line `(1,1,2)` packets; fixed-moving internal
  template; representative `xi=b`; swapped square allocation
  `c -> 1/d, d -> 1/b`
- **dependencies:**
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction`
  and
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate`
- **consumer:** `rate_half_band_closure` (evidence)

Normalize `a=2`, choose `xi=b`, orient `(eta,ell)=(c,d)`, and put
`w=1/c`. This theorem treats

```text
residual c ~ (W-1/d)^2,       residual d ~ (W-1/b)^2.       (KBNME-1)
```

The product conditions split into two lines in `b` over `c` and two
quadratics in `b` over `d`. For each of the four branch pairs, solve the
selected `c`-line and impose the selected `d`-quadratic and both middle
conditions. After the forbidden common components are removed, every
projected factor is a standard collision/fixed-point factor or one of

```text
17d^2-38d+17,                 2d+1,
11d^3-21d^2-3d+5,            5d^2-8d+5,
2d^2-3d-1,                   11d^2-20d+5,
2d^2-9d+1.                                           (KBNME-2)
```

The `q17` generic fibers are empty and its leading-zero fibers force
`b=1/2`. The cubic and `q11` force `c=1`; both `q5` fibers force `c=-1`.
Every remaining factor in `(KBNME-2)` forces `b=1/2`. Direct/resultant and
independent fraction-free/subresultant certificates reproduce the support
and all candidate ideals modulo `p=2130706433`. Hence `(KBNME-1)` is empty
over `F_(p^6)`.

Together with the seven earlier charts, 8 of the 18 affine positive charts
are closed. This node does not delete the other 10 affine charts, the
projective boundary, a negative locus, a packet, or the rate-half target.

## Falsifier

An admissible deployed-field solution of `(KBNME-1)`, or noncollision
support in any primary or independent replay.
