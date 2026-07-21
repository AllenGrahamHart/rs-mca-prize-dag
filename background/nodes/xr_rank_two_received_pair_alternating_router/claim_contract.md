# Claim contract

- **claim id:** `xr_rank_two_received_pair_alternating_router`
- **mathematical statement:** actual agreement forces the unified pairing
  identity `(RP2)`; the three-anchor interaction matrix is alternating as in
  `(RP4)--(RP5)`, while the four-anchor interaction matrix vanishes as in
  `(RP6)`
- **scope:** every uniform rank-two trade arising from an actual selected
  split-pencil family
- **consumer:** `xr_highcore_collision_count`
- **status:** `PROVED`
- **proved dependencies:** the actual uniform agreement normalization and the
  complete three/four-anchor coefficient atlases
- **new open content:** impose the remaining `h-1` block parity constraints,
  count compatible support-extension families, first-core ownership, and
  cross-core aggregation
- **falsifier:** an actual rank-two selected family violating `(RP2)`, a
  three-anchor interaction matrix not alternating, or a nonzero four-anchor
  interaction vector
- **nonclaims:** the parity-row converse is not full agreement-block
  realization
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/xr_rank_two_received_pair_alternating_router/verify.py`
- **upstream mapping:** witness-exhaustive first-match atlas / residual
  balanced-core ray compiler
