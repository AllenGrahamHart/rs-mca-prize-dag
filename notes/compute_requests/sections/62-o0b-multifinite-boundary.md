## Preregistered O0b multi-finite direct-boundary pilot

- **decision:** bypass the timed raw initial bases and test the repeatedly
  observed `b=-1` boundary directly on the four open chart masks
- **scope:** case `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=2,pairing=0)`;
  masks `FFF`, `FFI`, `FIF`, and `IFF`
- **launcher SHA-256:**
  `fefeac8a66f7443193aedc039523dde2f2c1661531971724181b479cdbd45921`
- **outcome-neutral checker SHA-256:**
  `605b0ea8a76640f31270ac92ce8468e4b0888427541283b2a16cb5d4eb317c1c`
- **Rabinowitsch chart-program core SHA-256:**
  `de224a472ce32dc98bb2c52e6aef987ef6864abd4be83e3741477f5a22050d38`
- **seven-chart pilot result SHA-256:**
  `09d854294bb4b0f3d33fc45f140f12ca86eebbb568c1f845a061b4143c50dba0`
- **cached common input SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **global common basis SHA-256:**
  `bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e`
- **cached outside compiler SHA-256:**
  `048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03`
- **envelope:** at most four one-CPU workers, 4 GiB each, 240-second
  Singular child wall and 300-second container wall; projected cost below
  `$0.25`
- **local safety:** unordered result streaming with immediate checkpoints
  under one RAM-guarded Modal client and a 360-second external hard stop

For each chart ideal `I`, the program adds one variable `w` and the exact
Rabinowitsch equation `w*(b+1)-1`. The resulting ideal is unit exactly when
`V(I)` has no point with `b+1 != 0`. This is stronger than applying the other
ordinary guards and is sufficient to close a chart because `b=-1` is already
forbidden. Four checked unit rows would finish all eight charts and close the
representative. A nonunit program is retained; a timeout has no mathematical
status and authorizes only chart-specific algebraic decomposition.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_chart_multifinite_boundary_modal.py
```
