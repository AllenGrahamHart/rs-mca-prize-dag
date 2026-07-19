# Claim contract

- **claim id:** `f3_h3_high_excess_low_distance_moment_reduction`
- **mathematical statement:** on `P>=33`, product excess is at most `16/83`
  times the distance-four/six edge weight, reducing C36' to `(HLM3)`
- **scope:** every official H3 row and every nonidentity product target in the
  selected `E=14` tail
- **consumer:** `f3_h3_mobius_excess_half`, high-excess fixed-order route
- **status:** `PROVED`
- **proved dependencies:** rich-excess degree ladder and exact
  excess-budget/degree tradeoff
- **new open content:** prove the distance-four/six edge–quotient moment
  `(HLM3)`
- **falsifier:** an integer excess `e>=15` for which the guaranteed centroid
  weight is less than `83e/16`
- **proof route:** optimize the exact centroid weight/excess ratio and retain
  quotient weights
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_h3_high_excess_low_distance_moment_reduction/verify.py`
- **upstream mapping:** primitive shift-pair control / exact second-moment
  ledger
