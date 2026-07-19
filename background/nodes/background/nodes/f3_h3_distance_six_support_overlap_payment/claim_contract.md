# Claim contract

- **claim id:** `f3_h3_distance_six_support_overlap_payment`
- **mathematical statement:** support-overlapping generic distance-six edges
  have the two cubic one-parameter covers `(DSO2),(DSO3)` and number at most
  six per target; an antipodal target has at most two additional edges; hence
  the disjoint estimate `(DSO7)` implies C36'
- **scope:** every official H3 row, using the `E=6`, `P>=25` analytic interface
- **consumer:** `f3_h3_mobius_excess_half`
- **status:** `PROVED`
- **proved dependencies:** distance-four norm profile and orientation,
  antipodal-tail cutoff frontier, and exact quotient-block mass identity
- **new open content:** prove `(DSO7)` for the four-variable/two-membership
  distance-six incidence restricted to six disjoint signed atoms
- **falsifier:** a fixed product fiber with seven overlapping generic--generic
  distance-six edges, an antipodal vertex with three distance-six neighbors,
  or a support-overlap pattern outside `(DSO2),(DSO3),(5P),(5R)`
- **nonclaims:** no bound for the disjoint incidence and no C36' promotion
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_h3_distance_six_support_overlap_payment/verify.py`
- **upstream mapping:** primitive shift-pair control / exact second-moment
  exceptional-stratum payment
