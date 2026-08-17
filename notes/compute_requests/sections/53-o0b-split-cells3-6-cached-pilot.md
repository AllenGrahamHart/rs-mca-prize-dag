## Preregistered O0b split cells-3/6 cached-input pilot

- **decision:** rerun the 24-representative pilot after removing all
  per-worker SymPy compilation; do not enlarge the representative domain
- **scope:** the same 24 canonical representatives and 56 coarse strata as
  request 51
- **launcher SHA-256:**
  `8a4409c16a44a6119f0e5e2d63fbb2aa0aca768371e1caacba2ab6b0e5169573`
- **checker SHA-256:**
  `c81565e84640732dc5bdbe0f611e95eec58117e27ca777d898e48190c10930a8`
- **string-compiler core SHA-256:**
  `048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03`
- **cached common input SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **representative manifest SHA-256:**
  `409e0e0851f2cef35501123b3dcb5818318380a291864090a7792accf599dfc2`
- **pilot representative-list SHA-256:**
  `a1853f2a70cd7fc46c173f1401e4b7e8820f9fa1c01e8a8b3571bfefa2969c96`
- **envelope:** at most 24 one-CPU workers, 3 GiB each, 240-second
  Singular child wall and 300-second container wall; projected cost below
  `$0.50`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; exact algebra remains remote and every returned row checkpoints

The string compiler consumes the pinned source-sign packet and emits eight
named equations directly in Singular syntax: three common determinants, one
missing-product equation, three residual pairing equations, and one missing
squared-sum equation. It imposes 40 deduplicated ordinary guards and then
saturates by the six-generator product-cofactor ideal. There is no SymPy
dependency or polynomial expansion in a case worker.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_modal.py
```

`PILOT_ALL_UNIT` requires 24/24 complete unit rows, exact packet/case custody,
24 distinct program hashes, final six-cofactor saturation transcripts, and
checker acceptance. A complete nonunit is retained in full. Any timeout or
error remains `INCOMPLETE`; the full 1,416-representative campaign is not
authorized by this preregistration.

**Outcome:** `INCOMPLETE`; global seven-variable saturation rejected. Modal
app `ap-inXJOeBGmGffKFVY29yI3W` produced 23 ordered `TIMEOUT` rows before the
external six-minute wall; the remaining input was preempted and restarted.
The app still had two containers after the client wall, and they were
explicitly stopped with `modal app stop -y`. Result SHA-256:
`4d2471d23f0ac04f5e049b6a84cd08152f85911f5cb72b0b5ae3a436d414accf`.
Incomplete-checker SHA-256:
`77b434e7dd89ffb31ffca3a40b7a11d2956916ad0606c40a1d2cc641451cdc39`.

Every returned worker had an exact program hash and cached-packet hash but an
empty partial stdout: Singular did not finish the initial `slimgb(I)` before
the 240-second child timeout. Thus cached input fixed the first run's symbolic
duplication, but the raw eight-generator seven-variable Gröbner basis is
itself unsuitable. No row has mathematical status, and no batch rerun is
authorized. The bounded replacement is to cache the saturated common-curve
Gröbner basis first and test one outside case against that basis.
