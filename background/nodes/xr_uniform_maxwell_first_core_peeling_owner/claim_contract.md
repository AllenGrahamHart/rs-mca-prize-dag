# Claim contract

- **claim id:** `xr_uniform_maxwell_first_core_peeling_owner`
- **mathematical statement:** the deterministic process `(PO1)--(PO4)` assigns
  every removed uniform-family block one unique pointed first-core
  certificate and leaves at most `B_0` blocks as in `(PO5)--(PO7)`
- **scope:** every one-per-slope uniform split-pencil family
- **consumer:** `xr_highcore_collision_count`
- **status:** `PROVED`
- **proved dependencies:** Maxwell-core extraction for every dense residual
  and canonical rank-two fundamental-circuit ownership
- **new open content:** count classified pointed certificates, handle their
  higher-rank branch, deduplicate collision components, and treat nonuniform
  cells
- **falsifier:** a residual satisfying `(PO1)` with no minimal core/trade, a
  rank-two trade with no non-anchor pivot, a repeated pointed certificate, or
  a terminal residual above `(PO5)`
- **nonclaims:** no pointed-certificate count and no aggregate slope payment
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/xr_uniform_maxwell_first_core_peeling_owner/verify.py`
- **audit replay:**
  `tools/ramguard tiny -- python3 background/nodes/xr_uniform_maxwell_first_core_peeling_owner/verify_audit.py`
- **upstream mapping:** witness-exhaustive first-match atlas / residual
  balanced-core ray compiler
