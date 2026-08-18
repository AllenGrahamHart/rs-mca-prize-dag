## Preregistered O0b `FFF` `R76` multiplication determinant

- **decision:** replace the timed 32-dimensional inverse-based norm by the
  direct quadratic resultant `R76=Res_E(q7,q6)` in the 16-dimensional `q5`
  quotient and test whether multiplication by `R76` is invertible
- **scope:** exact generic-fiber emptiness plus a retained symbolic
  determinant polynomial for exceptional-fiber routing
- **source multiplication-bank SHA-256:**
  `3d216da7d91c82a1360f932673ce3529278c90f81e6a8a6767f14a34ad73a45e`
- **source q7-coefficient SHA-256:**
  `37e2f17f8546e195024c23766f63cd36ba8681c115f3bf18f7410c19c902c45d`
- **source block-program SHA-256:**
  `fff178007fdea5ae7c14a0bee59fde6053aacc1a47f7a23f5d0c3bc654ab6224`
- **program core SHA-256:**
  `ac73c2251e90e6a84b45574dd171474c682586ff56415206d3453f355d49e33f`
- **launcher SHA-256:**
  `d3b296eb0ef62a7260ed725233ee17e390679f45c3bcadfad76eaa1e853d0a9b`
- **outcome-neutral checker SHA-256:**
  `c638bd5b045f92670b47b84046cf3b99652edca69965663917365fb71483ad3d`
- **generated Julia SHA-256:**
  `5f72b5b9f53b6a1c6d9138052fbd9e6f379b4fa617b47ad72d5daa98989c5eb9`
- **resultant identity:** write `q6(E)=y0+y1 E+y2 E^2`; then
  `R76=(D2*y0-D0*y2)^2-(D2*y1-D1*y2)*(D1*y0-D0*y1)`
- **route advantage:** no inversion of `D2` is used. If multiplication by
  `R76` is invertible, `q7` and `q6` cannot have a common root, including at
  fibers where the quadratic leading coefficient degenerates.
- **witness control:** at `t=2`, the determinant must equal `244686406`,
  independently forced by `1573108971^2 * 443644136` in the prime field
- **full output:** numerator and denominator coefficient ledgers of the
  16-by-16 `R76` multiplication determinant
- **envelope:** one deterministic task, one CPU, 24 GiB, 1,800-second Julia
  child wall and 1,860-second container wall; projected cost below `$0.25`
- **local safety:** one RAM-guarded Modal client under a 1,920-second external
  hard stop; no local CAS

Launch command:

```text
RAMGUARD_TIMEOUT=34m tools/ramguard modal -- \
  timeout --signal=TERM --kill-after=15s 1920s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_r76_multiplication_determinant_modal.py
```

**Outcome:** `TIMEOUT` after the full symbolic matrix. Modal app
`ap-9BUD9SrIBSZusMY2nn9i8h` independently recovered the exact witness

```text
det(M_R76)|_(t=2) = 244686406
```

and built the complete 16-by-16 symbolic `R76` multiplication matrix; all
256 entries are nonzero rational functions. The timeout occurred only inside
the final matrix determinant and emitted no rational-entry or determinant
ledger. Result SHA-256:
`7b889840b303ea9e61961f53eb608134081dadc5fa5e138f7a903bc319d2be07`.
The checker accepts the fail-closed witness and rejects all four hostile
mutations. The next computation must bank the 256 rational entries before
attempting a denominator-cleared polynomial determinant.
