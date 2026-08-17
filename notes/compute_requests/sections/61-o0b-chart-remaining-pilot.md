## Preregistered O0b seven-chart completion pilot

- **decision:** test every remaining leaf of the proved projective-chart split
  for the same representative whose all-infinity chart is closed
- **scope:** case `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=2,pairing=0)`;
  the seven masks in `{finite,infinity}^3` other than all-infinity
- **launcher SHA-256:**
  `99eaffabe8f10e1b303421fdec25f7d958f33f1dcc4e0dc05eac78da04333777`
- **outcome-neutral checker SHA-256:**
  `902c15e5dd3316957efab6342d3feec4df881e9ddb7d7ec1315762f4e007d5fb`
- **projective-chart program core SHA-256:**
  `277ad3a0d4489470eee9cef2c374b28d73aad333149ea415a3e55ea05549f4c5`
- **closed all-infinity result SHA-256:**
  `545a130914d9896d84a5215865fea7333a2af9f1f7f9d08bfc14d3587770bcaf`
- **cached common input SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **global common basis SHA-256:**
  `bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e`
- **cached outside compiler SHA-256:**
  `048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03`
- **envelope:** at most seven one-CPU workers, 4 GiB each, 240-second
  Singular child wall and 300-second container wall; projected cost below
  `$0.40`
- **local safety:** unordered result streaming with immediate checkpoints
  under one RAM-guarded Modal client and a 360-second external hard stop

Each row uses the same common basis, `q3`, `q7`, six exact chart equations,
40 guards, and six rank cofactors. Finite branches add exactly one auxiliary
root variable apiece. Seven checked unit rows, together with the already
closed all-infinity chart, close this representative. A nonunit is retained
as the next algebraic target. Timeouts have no mathematical status and permit
only mask-specific decomposition, not another representative or the complete
quotient campaign.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_chart_remaining_pilot_modal.py
```
