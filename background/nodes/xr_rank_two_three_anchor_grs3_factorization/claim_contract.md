# Claim contract

- **claim id:** `xr_rank_two_three_anchor_grs3_factorization`
- **mathematical statement:** every coefficient-rank-three rank-two trade has
  the slope-linear polynomial form `(TG1)`, with a unique full-support dual
  `GRS_3` weight polynomial `(TG3)` and explicit fundamental-circuit weights
  `(TG4)`
- **scope:** the `q=3` branch of every uniform rank-two split-pencil trade,
  on every active-union shell
- **consumer:** `xr_highcore_collision_count`
- **status:** `PROVED`
- **proved dependencies:** uniform polynomial-pencil representation and the
  canonical three/four-anchor owner
- **new open content:** count realized tuples `(X,P,Q,H)`, prove selected-block
  embedding coverage, select the first core/trade, and aggregate across cores
- **falsifier:** a `q=3` trade not expressible by `(TG1)--(TG3)`, nonunique
  `H`, or a canonical four-circuit whose weights violate `(TG4)`
- **nonclaims:** no support census, quotient payment, or statement that every
  abstract tuple is realizable
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/xr_rank_two_three_anchor_grs3_factorization/verify.py`
- **upstream mapping:** base-field-normalized split-pencil census / exact
  primitive shift-pair ledger
