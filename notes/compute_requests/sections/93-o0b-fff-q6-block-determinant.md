## Preregistered O0b `FFF` `q6` block determinant

- **decision:** represent the quadratic `q7` extension as a 32-dimensional
  block algebra and test whether multiplication by the final necessary
  equation `q6` is invertible
- **scope:** exact generic-fiber emptiness for the sole remaining O0b chart;
  exceptional transformation and determinant fibers remain separate
  obligations
- **source multiplication-bank SHA-256:**
  `3d216da7d91c82a1360f932673ce3529278c90f81e6a8a6767f14a34ad73a45e`
- **source q7-coefficient SHA-256:**
  `37e2f17f8546e195024c23766f63cd36ba8681c115f3bf18f7410c19c902c45d`
- **program core SHA-256:**
  `fff178007fdea5ae7c14a0bee59fde6053aacc1a47f7a23f5d0c3bc654ab6224`
- **launcher SHA-256:**
  `7a2dc088c8a9667dde5ec73e5408552d0fc11f6c719ec46b7f5b51a45f570261`
- **outcome-neutral checker SHA-256:**
  `65e2b29fbfc728a2494a137d7d50e5a0d7c2d2fcab5db6bb719fb5f94c2ef19d`
- **generated Julia SHA-256:**
  `d6e3b1aae07a3e89f24c0b65b120d064f665541611dfa858de9db8fd55f754cd`
- **algebra:** first certify `det(M_D2) != 0`; then use
  `M_E=[[0,-M_D2^-1 M_D0],[I,-M_D2^-1 M_D1]]`; verify the exact `q7`
  matrix identity; evaluate `q6`; take its 32-by-32 regular determinant
- **partial-result discipline:** before symbolic determinants, evaluate the
  complete construction exactly at `t=2` over `GF(2130706433)`. A nonzero
  `q6` determinant there proves the rational determinant is not identically
  zero. The witness is flushed and retained even if the later symbolic
  determinant times out.
- **full output:** exact numerator and denominator coefficient ledgers for
  `det(M_D2)` and `det(M_q6)`, suitable for the next exceptional-root pass
- **internal checks:** five source matrices commute; every source denominator
  is defined at the witness; `D2` is a unit; the 32-dimensional `q7` identity
  vanishes; the witness and symbolic `q6` determinants are nonzero
- **envelope:** one deterministic task, one CPU, 24 GiB, 1,200-second Julia
  child wall and 1,260-second container wall; projected cost below `$0.25`
- **local safety:** one RAM-guarded Modal client under a 1,320-second external
  hard stop; no local CAS

Launch command:

```text
RAMGUARD_TIMEOUT=24m tools/ramguard modal -- \
  timeout --signal=TERM --kill-after=15s 1320s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_q6_block_determinant_modal.py
```

**Outcome:** pending.
