# KoalaBear c2 (1,1,2) near positive reciprocal-xi square exclusions

- **status:** PROVED
- **scope:** the deployed KoalaBear field `F_(2130706433^6)`; positive
  near-aligned source-line `(1,1,2)` packets; fixed-moving internal template;
  relative orbit `xi=tau(a)`; both square allocations
- **dependencies:**
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction`
  and
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate`
- **consumer:** `rate_half_band_closure` (evidence)

Normalize `a=2`, take `xi=1/2`, orient `(eta,ell)=(c,d)`, and put `w=1/c`.
This theorem treats both allocations

```text
direct:   residual c ~ (W-2)^2,     residual d ~ (W-1/d)^2,
swapped:  residual c ~ (W-1/d)^2,   residual d ~ (W-2)^2.   (KBNTS-1)
```

For all four endpoint-line pairs in either allocation, the two
middle-coefficient resultants have squarefree support contained in

```text
d in {2,1,-1,1/2}.                                (KBNTS-2)
```

In the direct allocation, the full leading-zero loci add only

```text
(c,d)=(5,5/7),       (c,d)=(-7/5,53/55),          (KBNTS-3)
```

and both points force `5cd-4c-4d+5=0`, equivalently `z=1`. The independent
opposite elimination also finds `c=-2`, whose fiber forces `d=2` or `1/2`.
In the swapped allocation, the first leading-zero locus has the same
quadratic `z=1` component as the fixed-`xi` swapped chart; the second has
only forbidden support.

Exact reduction modulo `p=2130706433` preserves every support statement.
Therefore both reciprocal-`xi` square charts are empty over `F_(p^6)`.
Together with the four earlier charts, 6 of the 18 affine positive charts
are closed. This node does not delete the other 12 affine charts, the
projective boundary, a negative locus, a packet, or the rate-half target.

## Falsifier

An admissible deployed-field solution of either allocation in `(KBNTS-1)`,
or noncollision support in any primary or independent replay.
