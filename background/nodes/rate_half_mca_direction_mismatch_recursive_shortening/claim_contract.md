# Claim contract

- **claim id:** `rate_half_mca_direction_mismatch_recursive_shortening`
- **status:** `PROVED`
- **input:** one shortened support-wise MCA family, a minimum direction
  syndrome lift, and a uniform child bound
- **output:** the recurrence `(RS1)` and its exact deployed paid envelopes
- **multiplicity:** double-counted witness-coordinate incidences inside one
  family; no sum over separate cores
- **guard:** `0<=j<d`, exactly where every witness meets the minimum-lift
  support
- **nonclaims:** no payment for `j>=d` or beyond the certified envelope
- **replay:** `tools/ramguard local -- python3 background/nodes/rate_half_mca_direction_mismatch_recursive_shortening/verify.py`
- **independent audit:** `tools/ramguard local -- python3 background/nodes/rate_half_mca_direction_mismatch_recursive_shortening/verify_audit.py`
