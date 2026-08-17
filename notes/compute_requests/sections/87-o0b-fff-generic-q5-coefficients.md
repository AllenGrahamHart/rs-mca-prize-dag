## Preregistered O0b `FFF` generic `q5` coefficient normals

- **decision:** reduce the three certified coefficients of
  `q5=C0+C1*s+C2*s^2` independently in the eight-dimensional generic base
- **scope:** exact replacement for the retired raw-resultant normal form
- **source q5 bank SHA-256:**
  `25b3ac23d74e0bb710c50d636048c0f95ea4b94d51f3c5e02634cbfdfddf5f6e`
- **source generic result SHA-256:**
  `c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e`
- **program core SHA-256:**
  `d421246f3510b6738c21a45e10532d0b86441377ab27cb5ec17ba736c58a1b37`
- **launcher SHA-256:**
  `3e0793200520967f073f45cfba0fd7fc3150ee8e72521ec6e1a0a803fa3d9fc8`
- **outcome-neutral checker SHA-256:**
  `c520ba5ddc9b41c4201956d271b2be9c9376cb6d2358005a63ed7db80b7e0f48`
- **generated Julia SHA-256 values:**
  `6d5f6107ae3b41ff0976fe9cbc04a51d63be849e39bc604ae65c6009caf266e0`,
  `bcb63f54ccdf2441f7e2cfe7475589209bfc59d41bce73c4b6f07f1b167ab792`,
  `97b935a28c16421fa1ba539f62e97b9d1f4c41394644647e6f1d9a449877f74e`
- **input ledger:** coefficient hashes
  `98f5a959174f9899da07cb09736ef86dc449e1513821a6741dce19e749bfe913`,
  `b7defd8474f7a3b04011776833e0b4b9dce44de2c88e41633b797d4b9ce1cf9a`,
  `3f1f3db22008656b9e98b1966ad0f6f3cff897544d02b48d1ddfc14b6e48990e`
- **output ledger:** one full normal form and rational coefficient ledger per
  coefficient; exact source and generated-program hashes
- **envelope:** three parallel deterministic tasks, one CPU and 6 GiB each,
  300-second Julia child wall; projected aggregate cost below `$0.50`
- **local safety:** one RAM-guarded Modal client under a 420-second external
  hard stop; no local CAS

Completion of all three rows permits exact reconstruction of the generic
quadratic in `s`. A timeout remains local to that coefficient and does not
invalidate completed siblings.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 420s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_generic_q5_coefficients_julia_modal.py
```

**Outcome:** partial exact completion. Modal app
`ap-fjg7OlClGiYgb3VTpj1ygf` completed coefficients 0 and 2; each generic
normal form has fiber degree two and exactly eight quotient-basis terms.
Their hashes are

```text
C0 e008780fd3d46e30c2471900384068de9b384cf3f3a99fbb038d00364b3428c3
C2 e890823e9f38e2919f38a73bcd0b7d20c52882e5ea069a05abfa147f637f8ce8
```

Coefficient 1 timed out before output and remains open. The result SHA-256 is
`29a3236a322bf5ec1b797615fed99ccbb0b584981656eec04bd41da00989700c`.
The checker accepts statuses `[COMPLETE,TIMEOUT,COMPLETE]`, verifies both
complete coefficient ledgers, and rejects all four hostile mutations. Retry
only coefficient 1 under a longer bounded wall.
