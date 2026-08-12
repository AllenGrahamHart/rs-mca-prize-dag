# Claim contract

- **claim id:** `rate_half_mca_codeword_direction_gauge_rank_router`
- **status:** `PROVED`
- **input:** one selected support-wise MCA family and one codeword gauge `b`
- **output:** exact witness/badness equivalence, affine-rank shift at most one,
  and deployed transformed-rank payment walls
- **nonclaims:** no forced rank drop, direction-defect payment, first-match
  atlas, deployed-row closure, or prize closure
- **replay:** `tools/ramguard local -- python3 background/nodes/rate_half_mca_codeword_direction_gauge_rank_router/verify.py`
- **independent audit:** `tools/ramguard local -- python3 background/nodes/rate_half_mca_codeword_direction_gauge_rank_router/verify_audit.py`
