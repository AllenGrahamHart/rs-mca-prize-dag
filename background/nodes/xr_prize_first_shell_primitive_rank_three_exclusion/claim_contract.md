# Claim contract

- **claim id:** `xr_prize_first_shell_primitive_rank_three_exclusion`
- **mathematical statement:** first-shell rank-three trades have the simple
  edge-zero normal form `(P3E2)` and positive full-core deficit at every
  prize row; together with the rank-one/two exclusions, the primitive first
  shell is empty
- **scope:** all three prize P-A rows and every affine kernel rank `a`
- **consumer:** `xr_highcore_collision_count`
- **status:** `PROVED`
- **proved dependencies:** arbitrary-rank uniform split-pencil reduction and
  the prize primitive rank-two shell band
- **new open content:** proper local first-shell circuit ownership, RowC
  rank-three primitive trades, higher shells, higher trade rank, nonuniform
  cells, and aggregate slope payment
- **falsifier:** a full prize Maxwell core with a first-shell trade, a
  rank-three zero-set family violating `(P3E2)`, or failure of `(P3E4)`
- **nonclaims:** no proper-circuit count, RowC exclusion, or critical status
  promotion
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/xr_prize_first_shell_primitive_rank_three_exclusion/verify.py`
- **upstream mapping:** base-field-normalized split-pencil census / primitive
  first-shell circuit exclusion
