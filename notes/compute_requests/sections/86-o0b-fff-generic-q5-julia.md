## Preregistered O0b `FFF` incremental generic `q5`

- **decision:** normal-form `q5` modulo the certified generic base and adjoin
  only that quadratic-in-`s` equation
- **scope:** first stage of the incremental `q5 -> q7 -> q6` route
- **source generic result SHA-256:**
  `c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e`
- **source packet SHA-256:**
  `fbeda61593e73cdcb7bf1e2baa1ebe8b098a7025f834135b3e02d2c291d50cd9`
- **program core SHA-256:**
  `7f4845437a558d10ae9a68ad51592bdaea0801eaea17a4abc05a411b944ad2e6`
- **launcher SHA-256:**
  `66da2de96e2e45d12afa5f2d293d02729215d1d60623e72e4c8866ccb4cdfcd8`
- **outcome-neutral checker SHA-256:**
  `847cd8e77d582a58fbc728cfe9e5a3427076f14362ebeca7afa8984bc5eb0b2c`
- **generated Julia SHA-256:**
  `f8b3a2ff817e5651f48c74b3421201a45305de1c7877cf7c23e2a2e1a9caeb5a`
- **input ledger:** ten base polynomials, quotient dimension eight, one
  equation, fiber variables `s,x,r,c,b`
- **output ledger:** full `q5` normal form and hash; certified extended basis;
  quotient profile; combined normal-form and basis coefficient denominators
- **envelope:** one deterministic task, one CPU, 8 GiB, 300-second Julia
  child wall and 360-second container wall; projected cost below `$0.20`
- **local safety:** one RAM-guarded Modal client under a 420-second external
  hard stop; no local CAS

The normal-form and output-basis denominators are retained separately.
Transformation pivots remain open, and no generic stage alone promotes
`FFF`.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 420s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_generic_q5_julia_modal.py
```

**Outcome:** `INCOMPLETE_TIMEOUT`. Modal app
`ap-G2DYAjHI53OT1Ui7998KuR` exceeded the 300-second Julia wall before the
raw `q5` normal form completed. It produced no normal form, basis, or
mathematical status. Result SHA-256:
`5565e674db92a598d78f9bafcfdf7f2ffab04536ff8e99a223b2e0d9521fe46f`.
The checker accepts the transcript and rejects all three applicable hostile
mutations. Retire raw-resultant reduction and import the already certified
three-coefficient `q5` bank instead.
