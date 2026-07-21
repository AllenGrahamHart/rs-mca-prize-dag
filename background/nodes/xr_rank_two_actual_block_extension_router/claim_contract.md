# Claim contract

- **claim id:** `xr_rank_two_actual_block_extension_router`
- **mathematical statement:** the full block parity space splits as
  `(AR2)--(AR5)`; after unique support interpolation, actual block extensions
  are exactly the `tau_i`-subsets of the external residual zero set and are
  counted by `(AR9)`
- **scope:** each fixed support/slope row of every uniform rank-two trade
- **consumer:** `xr_highcore_collision_count`
- **status:** `PROVED`
- **proved dependencies:** common-cofactor support extension and the selected
  trade-row received-pair parity router
- **new open content:** enumerate support/slope data, enforce compatibility of
  several extensions, first-core ownership, and cross-core aggregation
- **falsifier:** a block parity polynomial without decomposition `(AR2)`, an
  actual extension outside `(AR8)`, or an extension count different from
  `(AR9)`
- **nonclaims:** no family-level intersection count and no slope payment
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/xr_rank_two_actual_block_extension_router/verify.py`
- **upstream mapping:** witness-exhaustive first-match atlas / exact extension
  payment
