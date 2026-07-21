# Claim contract

- **claim id:** `xr_trade_circuit_arity_segre_atlas`
- **mathematical statement:** a support-minimal row-scaling trade of rank `r`
  has `r+2<=t<=2r+1` active blocks; every rank-two trade decomposes into the
  exact four/five-point Segre circuits `(CA2)--(CA4)`
- **scope:** every uniform `u=v=0` high-core split-pencil cell
- **consumer:** `xr_highcore_collision_count`
- **status:** `PROVED`
- **proved dependency:** the arbitrary-rank uniform split-pencil reduction
- **new open content:** first-match ownership and aggregate count of the
  four/five-block circuits, rank-at-least-three circuit classification, and
  nonuniform cells
- **falsifier:** a row-scaling circuit outside `(CA1)`, a rank-two trade not
  decomposable into arity four/five circuits, or a circuit violating `(CA4)`
- **nonclaims:** no circuit-embedding count, slope payment, or cross-core
  canonicalization
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/xr_trade_circuit_arity_segre_atlas/verify.py`
- **upstream mapping:** base-field-normalized split-pencil census / exact
  primitive shift-pair circuit atlas
