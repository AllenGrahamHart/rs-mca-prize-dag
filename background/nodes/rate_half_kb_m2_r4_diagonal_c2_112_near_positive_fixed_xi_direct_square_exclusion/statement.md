# KoalaBear c2 (1,1,2) near positive fixed-xi direct-square exclusion

- **status:** PROVED
- **scope:** the deployed KoalaBear field `F_(2130706433^6)`; positive
  near-aligned source-line `(1,1,2)` packets; fixed-moving internal template;
  relative orbit `xi=a`; direct square allocation only
- **dependencies:**
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction`
  and
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate`
- **consumer:** `rate_half_band_closure` (evidence)

Normalize the common internal endpoint and `xi` to `a=xi=2`. Orient
`J_1={eta,ell}` as `(c,d)`, so the forced square is `w=1/c`. This theorem
considers the allocation

```text
residual over c = scalar * (W-1/2)^2,
residual over d = scalar * (W-1/d)^2.              (KBNDS-1)
```

For the positive fixed-moving reconstruction, each constant-to-leading
condition factors into two lines in `b`. All four line pairs fail the two
middle-coefficient equations. On the generic part of each left line, two
exact resultants have a gcd whose squarefree support is

```text
(d-2)(d-1)(d+1)(2d-1),                            (KBNDS-2)
```

so every common zero is a forbidden label collision or inversion-fixed
label. Where a left line vanishes identically in `b`, eliminating `c` gives
the same four forbidden `d` factors and one extra point. The extras are

```text
(c,d)=(1/5,7/5),       (c,d)=(-5/7,55/53),        (KBNDS-3)
```

and both satisfy `5cd-4c-4d+5=0`, equivalently the excluded reconstruction
label `z=1`. The same support statements hold after exact reduction modulo
`p=2130706433`, hence over its algebraic closure and over `F_(p^6)`.

Therefore no admissible reconstructed source form in this one chart passes
the necessary q-slice identity.

This does not delete the other 17 affine positive charts: the swapped or
mixed allocation, either other relative `xi` orbit, or the moving-moving
template. It also does not delete either negative locus, the repaired `w=0`
boundary, any full `(1,1,2)` packet, or the rate-half target.

## Falsifier

An admissible KoalaBear-field solution of `(KBNDS-1)` on any of the four
endpoint-line pairs, or a noncollision factor in either independently
computed modular gcd.
