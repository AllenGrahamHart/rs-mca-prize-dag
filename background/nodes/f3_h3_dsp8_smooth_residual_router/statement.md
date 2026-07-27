# DSP8 smooth residual router

- **status:** PROVED
- **closure:** exact ledger subtraction
- **consumer:** `f3_h3_dsp8_correlation_bound`
- **dependencies:** `f3_h3_dsp8_unit_trace_elliptic_curve_router`,
  `f3_h3_dsp8_nodal_cube_preimage_envelope`,
  `f3_h3_dsp8_global_overlap_cover_payment`

Split the raw trace-curve ledger into smooth and singular parts:

```text
G_25^c=G_sm^c+G_sing^c,       c in {0,A},
W_sm=10G_sm^0+17G_sm^A,
W_sing=10G_sing^0+17G_sing^A.                       (SRR1)
```

The current uniform DSP8 target in raw `G=4K` normalization is

```text
W_sm+W_sing <=(48536/25)n^2.                        (SRR2)
```

The proved Mattarei nodal payment therefore gives the following sufficient
smooth residuals:

```text
p=2 (mod 3):  W_sm <=(45636/25)n^2,
p=1 (mod 3):  W_sm <=(36086/25)n^2.                 (SRR3)
```

In particular the uniform assertion

```text
W_sm <=(36086/25)n^2                                (SRR4)
```

proves `(DSP8-U)` and closes the analytic C36' route. Equivalently, in
smooth primitive shift-pair normalization,

```text
10K_sm^0+17K_sm^A <=(18043/50)n^2.                 (SRR5)
```

This node proves the reduction only. It supplies no estimate for the smooth
elliptic trace-pair count.

