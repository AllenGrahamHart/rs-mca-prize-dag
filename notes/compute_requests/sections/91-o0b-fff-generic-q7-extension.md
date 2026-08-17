## Preregistered O0b `FFF` generic `q7` extension

- **decision:** adjoin the exact 24-term `q7` quadratic to the certified
  dimension-16 `q5` quotient
- **scope:** second finite extension in the incremental `q5 -> q7 -> q6`
  route
- **source q5 extension SHA-256:**
  `b5320657fc191da5adf2743ad020ab6a30934fd584f7f3f3a995caf9a712953c`
- **source q7 coefficient SHA-256:**
  `37e2f17f8546e195024c23766f63cd36ba8681c115f3bf18f7410c19c902c45d`
- **program core SHA-256:**
  `a0a7cc0c305491c613aeee6d3cace4a84bc488b725e07b35ae186858f582c4fd`
- **launcher SHA-256:**
  `92edd81728c857a154766f933fe03d5ba59acc265b5d788ed99f3276b239212c`
- **outcome-neutral checker SHA-256:**
  `b8c917a95c6191f6fb5424988b894afa0bd6b388f4ab9e82c7b93991f0e383b5`
- **generated Julia SHA-256:**
  `f0977dece0b591d0e84e2e5a6a054eb2f38d70d43e83f1ded53a38da1d2ed98a`
- **output ledger:** input term count, certified basis and quotient profile,
  full coefficient denominator ledger
- **envelope:** one deterministic task, one CPU, 16 GiB, 600-second Julia
  child wall and 660-second container wall; projected cost below `$0.50`
- **local safety:** one RAM-guarded Modal client under a 720-second external
  hard stop; no local CAS

Completion either gives a finite `q5,q7` algebra for the final `q6` test or
proves the generic subsystem already unit. Transformation denominators remain
open in either case.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 720s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_generic_q7_extension_modal.py
```

**Outcome:** `INCOMPLETE_TIMEOUT`. Modal app
`ap-cPK9VPOH7bzcXjc8ME08LD` constructed the exact 24-term `q7` input but
exceeded the 600-second Julia wall during the Groebner extension. No basis or
mathematical status was produced. Result SHA-256:
`a3d3dd55da213b58af78e415df88c1004348b838e7430c8150234bdb732e0b22`.
The checker accepts the transcript and rejects all three applicable hostile
mutations. Retire the Groebner extension and construct the quadratic
dimension-32 algebra from multiplication matrices instead.
