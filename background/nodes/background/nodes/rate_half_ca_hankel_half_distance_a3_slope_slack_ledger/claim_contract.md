# Claim contract

- **claim id:** `rate_half_ca_hankel_half_distance_a3_slope_slack_ledger`
- **mathematical statement:** every live half-distance `A=3` generator has
  exact separation rank `e+1`; every counterexample to `T<=rho+2` obeys the
  exact slope-slack, saturation, clean-column, matrix-rank, and product-code
  ledgers, with low-defect norm and quantized component degrees on `h=0`
- **scope:** only budget `B=2^39+1`, generic rank `rho=2^39-1`, and the
  `A=3` degrees `2^37+1<=e<=floor((2^39-1)/3)`
- **dependencies:** two-sided Hankel minimal indices and exceptional-root
  charging
- **consumer:** `rate_half_band_closure`
- **status:** `PROVED`
- **new open content:** exclude or realize the finite `(e,h)` strata; the
  first degree has only `h in {0,1,2,3}` and retains at least `3*2^37+2`
  saturated rows
- **falsifier:** a live half-distance `A=3` pencil with dependent `Q_j`, more
  than `4e+1` supported slopes, or a violation of `(HSL9)--(HSL18)`
- **nonclaims:** no stratum is excluded, the half-distance `A=1` profile is
  untouched, and no larger-budget crossing is determined
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_half_distance_a3_slope_slack_ledger/verify.py`
- **upstream mapping:** base-field-normalized split-pencil census / transpose
  Hankel-SPI slope ledger
