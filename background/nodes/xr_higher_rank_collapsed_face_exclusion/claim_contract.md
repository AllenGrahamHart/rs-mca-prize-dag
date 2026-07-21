# Claim contract

- **claim id:** `xr_higher_rank_collapsed_face_exclusion`
- **mathematical statement:** the singular minimum-face alternative forces
  every active selected error to vanish on the full `a+2` union, violating
  the post-strip pairwise common-zero cap `a`; hence only regular face
  syzygies occur at minimum union
- **scope:** every uniform `u=v=0` high-core P-A selector cell and every
  affine rank `s=a+1`
- **consumer:** `xr_highcore_collision_count`
- **status:** `PROVED`
- **proved dependency:** the higher-rank minimum-face syzygy dichotomy,
  including its uniform split-pencil and post-strip ancestry
- **new open content:** classify or pay rank-two trades with active union at
  least `a+3`, and trades of rank at least three
- **falsifier:** a collapsed minimum-face packet in which some selected error
  fails to vanish on `X`, or two such active errors whose common zero set
  obeys the post-strip cap
- **nonclaims:** no larger-union trade classification, no trade-rank-three
  estimate, and no aggregate slope payment
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/xr_higher_rank_collapsed_face_exclusion/verify.py`
- **upstream mapping:** base-field-normalized split-pencil census / local
  Plucker-syzygy quotient
