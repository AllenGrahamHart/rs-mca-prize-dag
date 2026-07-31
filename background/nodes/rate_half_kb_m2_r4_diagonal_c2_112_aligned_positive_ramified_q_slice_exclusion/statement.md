# KoalaBear c2 (1,1,2) aligned positive ramified q-slice exclusion

- **status:** PROVED
- **scope:** the positive-sign aligned source-line branch with forced source
  ramification `w=0`
- **requires:**
  `rate_half_kb_m2_r4_diagonal_c2_112_ramified_complete_source_repair` and
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate`
- **consumer:** `rate_half_band_closure` (evidence edge)

Normalize

```text
J_0={2,1/2,b,1/b},        q(T)=T^2+tT+p,
w=0,                      lambda=lambda_scale.
```

For each of the fixed-moving and moving-moving internal templates, exact
ramified reconstruction leaves three UFD allocations of the two residual
quadratics: `same`, `swap`, and `mixed`. The exact relative scales are

```text
fixed-moving:
  lambda=3(2b-1)(p-1)(p+2t+4),

moving-moving:
  lambda=-3(b-1)(b+1)(p-1)(p+2t+4)(5p+4t+5).
```

After substituting these scales and removing only factors proved nonzero on
the admissible open set, each allocation gives four equations. Direct
saturation over `F_2130706433` is the unit ideal in all six cases. The
moving equations are reciprocal quartics in `b`; the exact descent
`s=b+1/b` makes them quadratics before saturation.

Thus no aligned positive reconstructed source form with `w=0` passes the
necessary q-slice identity. Together with the separate aligned-negative
deletion, this removes the complete aligned forced-ramified branch.

This does not delete aligned positive forms with `w!=0`, the near-aligned
homogeneous boundary, another packet, or the rate-half target.
