# KoalaBear m2 r4 diagonal c2 (1,1,2) aligned negative q-slice exclusion

- **status:** PROVED
- **scope:** saturated source-line `(1,1,2)` packets in the aligned branch
  `Omega=J_1`, negative source-reciprocity sign only
- **dependencies:**
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_negative_reconstruction_factor_gate`,
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate`
- **consumer:** `rate_half_band_closure`

Normalize the common internal endpoint to `2` and write

```text
J_0={2,1/2,b,1/b},       q(T)=(T-c)(T-d).
```

Every negative reconstruction is fixed-moving on `B=0`, or moving-moving
on `B C=0`, with the factors `(KBNF-2)`. The involution `b->1/b` exchanges
`B` and `C` in the moving-moving template, so it is enough to impose `B=0`.

For the uniquely reconstructed form put `G=U^2-WV^2`. Divide
`Res_T(q,G)` by `(W-w)^4`, make the residual quartic monic, and subtract the
aligned target

```text
((W-1/c)(W-1/d))^2.
```

If `m_j` is the coefficient of `W^j` in this mismatch, direct exact
reconstruction gives, for both normalized templates,

```text
m_0=(cd-1)(cd+1)/(c^2 d^2).                       (KBNA-1)
```

Admissibility gives `cd!=1`, so q-slice passage would force `cd=-1`. On
that specialization the same expansion gives

```text
m_1-m_3=4(c^2-1)/c=-A.                            (KBNA-2)
```

The negative factor theorem proves `A!=0`. Hence the aligned q-slice
identity `(KBQS-1)` cannot hold: **no aligned negative reconstructed
candidate exists**.

This deletes no positive candidate, near-aligned negative candidate, full
packet, diagonal row, owner, payment, KoalaBear row, or Prize result.

## Falsifier

An admissible aligned negative reconstruction satisfying `(KBQS-1)`, failure
of either coefficient identity `(KBNA-1)--(KBNA-2)`, or failure of the
moving-template `B/C` inversion symmetry.
