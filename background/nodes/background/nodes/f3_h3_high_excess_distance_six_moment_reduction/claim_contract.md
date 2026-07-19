# Claim contract

- **claim id:** `f3_h3_high_excess_distance_six_moment_reduction`
- **mathematical statement:** on `P>=33`, excess is at most `8/21` times
  the distance-six edge count, so `(H6M3)` implies C36'
- **scope:** every official H3 row on the selected `E=14` tail
- **consumer:** `f3_h3_mobius_excess_half`, final distance-six route
- **status:** `PROVED`
- **proved dependencies:** distance-four fiber-degree cap and exact
  excess-budget/degree tradeoff
- **new open content:** prove `(H6M3)` for the canonical distance-six
  edge–quotient incidence
- **falsifier:** an excess `e>=15` with fewer than `21e/8` distance-six edges
  under the proved small-vector and distance-four bounds
- **proof route:** combine the linear distance-four cap with the norm-one
  antipodal saving in the quadratic centroid weight
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_h3_high_excess_distance_six_moment_reduction/verify.py`
- **upstream mapping:** primitive shift-pair control / exact second-moment
  ledger
