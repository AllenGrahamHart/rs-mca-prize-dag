# Claim contract

- **claim id:** `xr_higher_rank_minimal_face_syzygy_dichotomy`
- **mathematical statement:** a minimum-union rank-two trade is either an
  exact regular Plucker face syzygy or carries a common `k+2` near-tangent
  core; no partially singular face pattern exists
- **scope:** uniform `u=v=0` high-core selector cells at every affine rank
  `s=a+1`
- **consumer:** `xr_highcore_collision_count`
- **status:** `PROVED`
- **proved dependency:** arbitrary-rank uniform split-pencil reduction
- **new open content:** pay the common `k+2` near-tangent branch and the
  post-quotient trades with active union at least `a+3` or rank at least three
- **falsifier:** a minimum-union rank-two trade with a proper nonempty set of
  singular selected facets, or a regular relation outside `(MF5)`
- **nonclaims:** no count of near-tangent cores, no payment of larger-union
  rank-two trades, and no aggregate slope bound
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/xr_higher_rank_minimal_face_syzygy_dichotomy/verify.py`
- **upstream mapping:** base-field-normalized split-pencil census / local
  Plucker-syzygy quotient
