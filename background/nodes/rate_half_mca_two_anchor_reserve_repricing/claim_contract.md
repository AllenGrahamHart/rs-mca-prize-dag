# Claim contract

- **claim id:** `rate_half_mca_two_anchor_reserve_repricing`
- **status:** `PROVED`
- **scope:** exact conditional-assembly arithmetic on the two deployed MCA
  adjacent rows
- **dependencies:** the uniform two-anchor `2w` theorem and the proved exact
  full-owner average ceilings
- **output:** a separate near-rational owner, residual exception cap `31`,
  and revised large-owner target `B*-(2w+31)-(n-g)`
- **falsifier:** any failed row, target, margin, source-pin, or exact-sum check
- **nonclaims:** no proof of revised `(A)`, `(S)`, `(E)`, selector, safe row,
  or prize closure
- **replay:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_two_anchor_reserve_repricing/verify.py`
- **independent audit:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_two_anchor_reserve_repricing/verify_audit.py`
- **upstream mapping:** `OVERLAP`; exact threshold-note input for the
  `#1160/#1163` direct S/A/E lineage
