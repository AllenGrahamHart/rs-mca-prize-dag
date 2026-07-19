# Claim contract

- **claim id:** `xr_higher_rank_uniform_split_pencil_reduction`
- **mathematical statement:** every over-budget high-core selector in a
  uniform `u=v=0` rank cell contains the printed arbitrary-rank Maxwell core
  and dual-product-code trade; trade rank two uses at most `2(s-1)` active
  coordinates
- **scope:** high-core P-A, every affine selector rank `s=a+1`, uniform
  flat-nullity cell only
- **consumer:** `xr_highcore_collision_count`
- **status:** `PROVED`
- **proved dependencies:** flat-nullity factorization and the post-strip affine
  pencil/core cap; nondegeneracy uses the consumer's tangent-generic branch
- **new open content:** pay the resulting primitive trade census, and extend
  comparable control to nonuniform `u+v>0` cells
- **falsifier:** a generic uniform selector violating the Maxwell identities,
  or a rank-two trade with `t>a+2` or active union larger than `2a`
- **nonclaims:** no aggregate slope bound, no classification of trade rank at
  least three, and no claim that pencil parameters equal slopes when `t>4`
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/xr_higher_rank_uniform_split_pencil_reduction/verify.py`
- **upstream mapping:** base-field-normalized split-pencil census / exact SPI
  or exchange-degree ledger
