# Claim contract

- **claim id:** `f3_h3_low_distance_quotient_incidence_router`
- **mathematical statement:** the high-excess low-distance moment is exactly
  `2|I_4|+|I_6|` for the four-variable/two-membership system `(LQI2)`, while
  distance four has the three-variable covers `(LQI5),(LQI6)`
- **scope:** every official H3 row on the selected `P>=33` tail
- **consumer:** `f3_h3_mobius_excess_half`, low-distance moment route
- **status:** `PROVED`
- **proved dependencies:** high-excess low-distance moment reduction and
  distance-four cross-overlap router
- **new open content:** prove the exact bound `(HLM3)` for these incidence
  systems
- **falsifier:** an edge–quotient record not reconstructed uniquely by
  `(LQI2)`, or a distance-four record outside both covers
- **proof route:** canonical orientation and rational elimination
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_h3_low_distance_quotient_incidence_router/verify.py`
- **upstream mapping:** primitive shift-pair control / exact second-moment
  ledger
