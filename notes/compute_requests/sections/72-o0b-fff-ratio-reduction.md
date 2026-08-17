## Preregistered O0b `FFF` six-variable ratio reduction

- **decision:** use `q3` and `s=f/e` to eliminate `d,f`, then retain
  the cleared `q7` equation and all three scaled matching resultants
- **scope:** the last open canonical chart `FFF` for
  `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=2,pairing=0)`
- **relation:** necessary superset; each finite common-root condition is
  weakened to scaled quadratic-resultant vanishing
- **launcher SHA-256:**
  `7d6ef24e5c3c50010ea714ef04e1e357887918692c3074c740ff9b9fa84c4232`
- **outcome-neutral checker SHA-256:**
  `86ecfcac32363a0e8546b34cc62d6cba104a57c460ba917df101041f536a7db2`
- **program core SHA-256:**
  `e1e7d17d0269b739d4952d2951f0ea094e819aa3b8c4827e781abff729b196c0`
- **IFF-unit result SHA-256:**
  `5485816c745c18d1514200cc1bba057662c03319f7820883e7010ecb723b93c3`
- **input ledger:** variables `e,s,t,r,c,b` with ordinary `dp` order;
  21-element common basis; equations in order
  `q7,q5,q4,q6`; 16 route guards; guards `e,s,a0m,a2m`; six rank
  cofactors
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.07`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

The exact substitutions are

```text
f = e*s,
d = a0m/(e*a2m).
```

The standalone core verifies the substitutions, all six record values, and
the cleared `q7` numerator. The three scaled resultants retain all finite
roots and may additionally retain roots at infinity, so unit ideal for this
larger locus proves `FFF` empty. Completion with a unit basis closes the
last chart in the canonical representative; nonunit or timeout output has no
closure status.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_ratio_reduction_modal.py
```

**Outcome:** `INCOMPLETE_TIMEOUT`. Modal app `ap-VtWKDIyM7gsbgbG2eyLP2S`
exposed a large-characteristic incompatibility in Singular's block-order
polynomial expansion and performed no valid basis computation. After
switching only to the already-validated ordinary `dp` order, app
`ap-EeRYmLyJl6zlU6zfjeELpW` completed the `q7` stage with
`(dimension 2,basis size 50)` and timed out while adjoining `q5`; result
SHA-256:
`0f9cb1df4d58e5c55ac742beb9d041a7c23ec9d282101c43d67acb4bfabfb4f5`.
The outcome-neutral checker accepts the retained stage transcript and rejects
all three hostile mutations. This has no closure status. The next route
replaces `e` by `E=e^2` for the `q7,q5,q6` subsystem before adjoining
the square root and `q4`.
