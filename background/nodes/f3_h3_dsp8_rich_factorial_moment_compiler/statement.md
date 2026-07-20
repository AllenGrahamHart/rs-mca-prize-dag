# DSP8 rich factorial-moment compiler

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_dsp8_correlation_bound`
- **dependencies:** `f3_h3_disjoint_distance_six_split_pencil_router`,
  `f3_h3_dsp8_primitive_shift_pair_adapter`,
  `f3_h3_dsp8_global_overlap_cover_payment`

For the antipodal-free and antipodal target classes `c in {0,A}`, put

```text
F_25^c=sum_(t in class c,P(t)>=25)P(t)(P(t)-2)R(t),
M_21=sum_(t!=1)P(t)(P(t)-1)R(t).
```

Then the decorated disjoint primitive shift-pair correlation obeys

```text
10K_25^0+17K_25^A
 <=(1/4)(10F_25^0+17F_25^A)
 <=(17/4)M_21.                                    (RFC1)
```

Consequently either of the estimates

```text
40(10F_25^0+17F_25^A)<=76599n^2,                 (RFC2)
680M_21<=76599n^2                                 (RFC3)
```

implies the uniform DSP8 target and hence closes the analytic C36' route.
The older background target `M_21<=69n^2` is strictly stronger than `(RFC3)`:
the present sufficient unweighted constant is
`76599/680=112.645588...`.

This theorem proves only the compiler. It supplies no estimate for
`F_25^0,F_25^A`, or `M_21`.
