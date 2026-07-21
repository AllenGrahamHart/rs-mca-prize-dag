# Claim contract

- **claim id:** `xr_rank_two_extension_family_collision_ledger`
- **mathematical statement:** actual rank-two block extensions have the exact
  pairwise intersection formula `(EC3)`, pair slack `(EC4)`, aggregate
  collision budget `(EC5)`, and finite compatibility characterization `(EC6)`
- **scope:** every actual extension family of a fixed uniform rank-two shell
- **consumer:** `xr_highcore_collision_count`
- **status:** `PROVED`
- **proved dependencies:** shell zero-fiber disjointness and exact per-row
  external-zero extension routing
- **new open content:** count compatible support families and packing-ledger
  solutions, assign first-core ownership, and aggregate cores
- **falsifier:** a compatible block family violating `(EC3)--(EC5)`, or a
  family satisfying `(EC4)--(EC6)` but violating a pairwise block cap
- **nonclaims:** no packing bound or slope count
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/xr_rank_two_extension_family_collision_ledger/verify.py`
- **upstream mapping:** witness-exhaustive first-match atlas / exact extension
  and split-pencil ledger
