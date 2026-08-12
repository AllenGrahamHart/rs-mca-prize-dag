# Claim contract

- **claim id:** `rate_half_mca_global_core_direction_distance_router`
- **status:** `PROVED`
- **input:** one selected non-global-affine family after whole-line
  global-core cancellation
- **currency:** distinct finite affine slopes on that one shortened line
- **output:** exact support-wise-span payment, direction-distance payment, or
  one named low-direction-distance residual
- **multiplicity:** one whole-line family; no sum over cores or support unions
- **nonclaims:** no payment of the residual, no external first-match atlas,
  no deployed-row or prize closure
- **replay:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_global_core_direction_distance_router/verify.py`
- **independent audit:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_global_core_direction_distance_router/verify_audit.py`
