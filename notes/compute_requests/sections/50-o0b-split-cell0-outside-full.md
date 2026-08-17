## Preregistered O0b split cell-0 complete outside campaign

- **decision:** decide the changed O0b outside ideal on every canonical
  equal-sign cell-0 component representative
- **scope:** all 708 representatives covering 2,520 component cases and
  1,260 underlying raw labels
- **launcher SHA-256:**
  `04ae51440703ad0116e33ce6a4c7f3312eff748cd8c3fa1a1d326c4d465f5d48`
- **checker SHA-256:**
  `74770cfadbfa1275fe58fbee187b40e00cea8e8526ff3dc07347a8011c8046b5`
- **outside-core SHA-256:**
  `5cd86020b601b68e9a4295d55d057ec0e029dede334397e6bc51f9d840e5561f`
- **representative manifest SHA-256:**
  `658ae5f1f3c0667df2cece818e0c89a752ce9cdf7c4f6f421fc4a721134b8fa4`
- **full representative-list SHA-256:**
  `23d7e403e420307b5466ffaf6d2af59d0cf9a4a93766b4d0bcf68231aba1a741`
- **pilot authorization:** app `ap-4ye2CkHWY93ZYrySLOibPR`, 24/24 exact
  unit ideals, result SHA-256
  `796378e75e7eee01924c8f7b64ccfb1dc6af07adf9db945b59b8e59728b32507`
- **envelope:** at most 64 concurrent one-CPU, 2-GiB workers; 180-second
  Singular child and 210-second container walls; one 285-second external
  campaign hard stop; conservative simultaneous-resource cost below `$0.50`
- **local safety:** one RAM-guarded Modal client; results checkpoint in
  canonical order after every returned row

This run changes only `--scope all`. The complete PROVED router, component
relations, exact equations, guard set, image, and solver are byte-identical to
the successful pilot. The external stop bounds total active container time by
`64*285` seconds even if hard rows queue or time out. An interrupted run keeps
its ordered prefix and authorizes resumption only after an exact remaining-
case router is recorded.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 285s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_split_cell0_component_outside_modal.py \
  --scope all
```

`COMPLETE_OUTSIDE_EXCLUDED` requires 708/708 `COMPLETE` unit rows, exact
ordered case and source hashes, and checker acceptance. It authorizes a
separate PROVED outside-exclusion node after an independent algebraic audit
of the generated equations and guard semantics. A complete nonunit row is a
retained candidate locus, not a counterexample until replayed against the raw
system. Any timeout, remote error, malformed row, client interruption, or
missing representative is `INCOMPLETE` and causes no status promotion.

**Outcome:** `COMPLETE_OUTSIDE_EXCLUDED`. Modal app
`ap-iPfRgFxqrpfuNMG1WzzxIZ` completed all 708 representatives; result
SHA-256: `6aed35275a09c9ceaa55f2e47ad07409f7d3ed0ffd8f77010ce080ba862b95aa`.
Every row is `COMPLETE`, every sequentially saturated ideal is unit, and
there are 708 distinct program hashes. The independent audit checks the
ordered representative cover, exact O0b edge table, contiguous Singular
transcripts, stable unit tails, and guard profile `30:354,31:354`, with 3/3
hostile mutations rejected. The Modal client printed a nonfatal asynchronous-
generator shutdown warning after the complete checkpoint; it exited zero and
the checker accepts 708/708 rows. The separate PROVED cell-0 exclusion node
consumes this certificate.
