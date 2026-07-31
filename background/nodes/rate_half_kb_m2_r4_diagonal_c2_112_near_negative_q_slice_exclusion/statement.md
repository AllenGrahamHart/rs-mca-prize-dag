# KoalaBear c2 (1,1,2) near-aligned negative q-slice exclusion

- **status:** PROVED
- **scope:** every negative-sign near-aligned saturated source-line `(1,1,2)`
  candidate, including the forced-ramified `w=0` branch
- **requires:**
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_negative_reconstruction_factor_gate`
  and
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate`
- **consumer:** `rate_half_band_closure` (evidence edge)

Normalize

```text
J_0={2,1/2,b,1/b},       q(T)=(T-c)(T-d),
Omega={xi,d},             xi in {2,1/2,b}.
```

The negative factor gate reduces both internal templates to `B=0`; the
moving-template `C=0` locus is its image under `b->1/b`. On `B=0` the two
reconstructed forms have the same `z,V` and opposite `U`, hence the same
`G=U^2-WV^2`. Its monic q-slice residual quartic has constant coefficient
one. The near target therefore forces `(xi*d)^2=1`. The `xi*d=1` branch is
always a label collision.

On the remaining `xi*d=-1` branch, exact elimination gives:

```text
xi=2:    d=-1/2, projection (c+2)^4(13c-14)^4;
xi=1/2:  d=-2,   projection (2c+1)^4(14c-13)^4;
xi=b:    2cd^2-2cd+2c-d^2+4d-1=0,
          projection d^2(d-1)^6(d+1)^6(d+2)^4
                     (d^3-6d^2+3d-2)^4.
```

The first two projections reconstruct only `w=-1,+1`. In the last row,
`d=0,+/-1` are forbidden, `d=-2` forces `b=1/2`, and the cubic reconstructs
only `w=-1`. Direct saturation modulo `2130706433` by these forbidden
factors is the unit ideal in all three rows. Thus no admissible near-aligned
negative candidate passes the necessary q-slice identity.

This does not delete the homogenized positive `w=0` boundary, another
packet, or the full rate-half target.
