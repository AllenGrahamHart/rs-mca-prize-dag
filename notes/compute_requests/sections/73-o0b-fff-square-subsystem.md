## Preregistered O0b `FFF` square subsystem

- **decision:** replace `e` by `E=e^2` and test the necessary
  `q7,q5,q6` subsystem before adjoining `q4`
- **scope:** a strict necessary superset of the last open canonical
  `FFF` chart
- **relation:** necessary superset; `q4` is deliberately omitted and the
  two retained finite pairs are weakened to scaled resultants
- **launcher SHA-256:**
  `62df8e472a5409912e53d435da221750f3f1a44ad159e9f38c4355fe89df80ff`
- **outcome-neutral checker SHA-256:**
  `9c9ac1a611856cac9477be9701aa4aba77756cce17901667899c5e094d7227ae`
- **program core SHA-256:**
  `c5eca188068083699e94ba321858710f5225f423380a71821f9cea90135c4e72`
- **ratio-timeout result SHA-256:**
  `0f9cb1df4d58e5c55ac742beb9d041a7c23ec9d282101c43d67acb4bfabfb4f5`
- **input ledger:** variables `E,s,t,r,c,b`; 21-element common basis;
  equations in order `q7,q5,q6`; 16 route guards; guards
  `E,s,a0m,a2m`; six rank cofactors
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.07`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

The substitution turns the cleared `q7` equation into

```text
lm*bm^2*E - (a0m + E*a2m)^2 = 0.
```

The `q5` resultant depends only on `s` and the base; the `q6`
resultant depends on `E,s`. Every `FFF` solution maps into this subsystem,
so a checked unit basis closes `FFF` without needing `q4`. A nonunit
result becomes the finite or lower-dimensional input for adjoining
`e^2=E` and `q4`; timeout has no proof status.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_square_subsystem_modal.py
```

**Outcome:** `INCOMPLETE_TIMEOUT`. Modal app `ap-ZyjARWuvmq8EWOITABCBu5`
completed the `q7` stage with `(dimension 2,basis size 54)` and timed out
while adjoining `q5`; result SHA-256:
`cefc9fc49863ab0d20291c7cc009553bc45b8eb2946550c97c3daca154b595af`.
The outcome-neutral checker accepts the retained stage transcript and rejects
all three hostile mutations. Replacing `e` by `E` does not remove the
`q5` bottleneck. The next architecture reduces `q5` explicitly modulo
the common basis and adjoins it before `q7`.
