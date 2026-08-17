## Preregistered O0b `FFF` generic `q5` coefficient-1 resume

- **decision:** retry only the sole open coefficient `C1` with its identical
  generated Julia program and a bounded 660-second child wall
- **scope:** complete the middle coefficient of the generic `q5` quadratic;
  do not recompute completed `C0,C2`
- **source frontier SHA-256:**
  `29a3236a322bf5ec1b797615fed99ccbb0b584981656eec04bd41da00989700c`
- **generated Julia SHA-256:**
  `bcb63f54ccdf2441f7e2cfe7475589209bfc59d41bce73c4b6f07f1b167ab792`
- **launcher SHA-256:**
  `deffef33d4335323f938b1aea6be783c8c1d978536999aa0fd746069765a604f`
- **outcome-neutral checker SHA-256:**
  `82d55452bdb88823b494af4ffce651f48379782d41c1ad843cd30ef7d70a8538`
- **envelope:** one deterministic task, one CPU, 8 GiB, 660-second Julia
  child wall and 720-second container wall; projected cost below `$0.30`
- **local safety:** one RAM-guarded Modal client under a 780-second external
  hard stop; no local CAS

If this retry times out, the direct normal-form route for `C1` is retired in
favor of evaluation through the four 8-by-8 quotient multiplication
matrices.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 780s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_generic_q5_c1_resume_modal.py
```

**Outcome:** preregistered; not yet run.
