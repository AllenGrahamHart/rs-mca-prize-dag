# Claim contract

- **claim id:** `rate_half_ca_hankel_half_distance_a1_core_slope_slack_ledger`
- **mathematical statement:** every live half-distance `A=1` profile, after
  stripping its proved core `s in {0,1,2}`, has a maximal-separation-rank
  residual generator and obeys the exact Euclidean slope cap, capacity,
  saturation, product-code, sharp-cap norm, and component-chamber ledgers
  `(A1L4)--(A1L16)`
- **scope:** only budget `B=2^39+1`, generic rank `rho=2^39`, and the three
  core-degree ranges in `(A1L3)`
- **dependencies:** two-sided Hankel minimal indices and contracted
  exceptional-root charging
- **consumer:** `rate_half_band_closure`
- **status:** `PROVED`
- **new open content:** exclude or realize the finite core/degree/slack
  strata; at `e=2^37+1` they have only `3+4+4` possible slack values
- **falsifier:** a live `A=1` pencil violating coefficient independence,
  `T<=T_max`, the exact capacity identity, or a sharp-cap chamber
- **nonclaims:** no displayed stratum is excluded and no rate-half crossing
  is determined
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_half_distance_a1_core_slope_slack_ledger/verify.py`
- **upstream mapping:** base-field-normalized split-pencil census / fixed-core
  Hankel-SPI residual ledger
