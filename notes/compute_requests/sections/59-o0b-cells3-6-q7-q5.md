## Preregistered O0b cells-3/6 `q3 -> q7 -> q5` transition

- **decision:** test the cheapest supported continuation from the only
  completed single-equation extension
- **scope:** case `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=2,pairing=0)`;
  extend the retained `q3+q7` basis by `q5`
- **launcher SHA-256:**
  `7af2927ea5a209bfb1d0919f5a2a3f2b5ebd114039e33d2ab4c221bd9c30491f`
- **outcome-neutral checker SHA-256:**
  `058482e49eea43ba7369dbd8c9b2c1d54f27d02bc7f550e502dca56fa767dda9`
- **single-extension result SHA-256:**
  `ce0396a9f6d951270a5ec3ba9b8371919020dcac75ca11af488d9fabc5e0edb9`
- **source `q3+q7` basis SHA-256:**
  `679c448e3587f4bb11f39a6742aa7439d9b909ad68cf19834ca463d634c5aceb`
- **cached common input SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **cached outside compiler SHA-256:**
  `048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03`
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.06`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

The reconstructed 128-polynomial source is explicitly marked with Singular's
`isSB` attribute before reduction; custody of the exact `slimgb` output makes
that assertion valid and removes the noncanonical-reduction warning from the
preceding diagnostic. A complete result retains the new basis and authorizes
only the next single-equation transition. A timeout has no mathematical
status and calls for algebraic decomposition of `q5` modulo the pinned source.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_split_cells3_6_q7_q5_modal.py
```

**Outcome:** `INCOMPLETE_CANONICAL_REDUCTION_TIMEOUT`. Modal app
`ap-PsMF23qtEZ5Lg6Ns1QWKJJ` returned the pinned row with status `TIMEOUT`;
result SHA-256:
`6181b927a81f77e973baffdf551628a77e04185ba04613e34900a68843200e64`.
The outcome-neutral checker accepts the exact row and rejects all three
hostile mutations. No normal-form marker was printed: after the valid `isSB`
attribute was set, canonical reduction of `q5` modulo the 128-polynomial
`q3+q7` basis did not finish within 240 seconds. This has no mathematical
status. It rejects further equation-order tuning as the immediate endpoint;
the next route should decompose the three matching resultants into their exact
projective common-root charts before attempting another basis computation.
