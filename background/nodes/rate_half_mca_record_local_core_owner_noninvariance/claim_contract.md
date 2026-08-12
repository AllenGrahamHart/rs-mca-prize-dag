# Claim contract

- **claim id:** `rate_half_mca_record_local_core_owner_noninvariance`
- **status:** `PROVED`
- **quantifier:** one exact `GF(11)` Reed-Solomon received line
- **output:** two overlapping non-affine critical records with different
  intersections of maximal supports
- **route consequence:** record-local core identity alone is not a disjoint
  slope owner
- **nonclaims:** no deployed-row falsifier, first-match compiler, slope
  payment, or prize closure
- **replay:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_record_local_core_owner_noninvariance/verify.py`
- **independent audit:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_record_local_core_owner_noninvariance/verify_audit.py`
