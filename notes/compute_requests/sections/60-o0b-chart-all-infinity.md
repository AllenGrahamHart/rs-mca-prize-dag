## Preregistered O0b all-infinity projective-chart pilot

- **decision:** test the smallest leaf of the proved eight-chart resultant
  decomposition
- **scope:** case `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=2,pairing=0)`;
  chart mask `(infinity,infinity,infinity)`
- **launcher SHA-256:**
  `1c9b81d9377c6e06edd5b1953e955c5ebffb0d3a9592485fe00d3c5c11dfbeb3`
- **outcome-neutral checker SHA-256:**
  `c8ce618837d678d19dced46b9ff250d0141d3ac7e61f579372192b4e1a9f9876`
- **projective-chart program core SHA-256:**
  `277ad3a0d4489470eee9cef2c374b28d73aad333149ea415a3e55ea05549f4c5`
- **cached common input SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **global common basis SHA-256:**
  `bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e`
- **cached outside compiler SHA-256:**
  `048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03`
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.06`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

The all-infinity chart replaces each of `q4,q5,q6` by the two corresponding
leading-coefficient equations. It has the original seven variables, the
proved 21-polynomial common basis, `q3`, `q7`, six chart equations, all 40
ordinary guards, and the six rank cofactors. A checked unit result closes only
this one exact chart. A checked nonunit is retained as the next algebraic
target. A timeout has no mathematical status and does not authorize the other
seven charts or another representative.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_chart_all_infinity_modal.py
```

**Outcome:** `COMPLETE_UNIT`. Modal app `ap-qkhSkBXGe1rYbrHca5zY6I`
completed the exact chart in under ten seconds. Result SHA-256:
`545a130914d9896d84a5215865fea7333a2af9f1f7f9d08bfc14d3587770bcaf`.
The outcome-neutral checker accepts the transcript and rejects all three
hostile mutations. The initial chart ideal has dimension 3 and basis size 54.
It remains dimension 3 through the first five guard stages; saturation by
guard 5, `b+1`, yields the unit ideal. Thus every all-infinity solution lies
on the forbidden boundary `b=-1`, and this one chart is closed exactly. The
result authorizes a small pilot across the other seven chart masks for this
same representative, not a second representative or the full quotient.
