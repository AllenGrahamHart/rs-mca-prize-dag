# Claim contract

- **claim id:** `rate_half_mca_global_core_rank_support_distance_router`
- **status:** `PROVED`
- **input:** one whole-line global-core shortened family, its minimum-lift
  direction support `e=R-j`, and transformed explanation rank `r`
- **output:** the union of exact rank, low-support, and high-support paid
  gates, plus exact first-residual middle intervals
- **nonclaims:** no middle-cell payment, K3 ownership or allocation, row
  close, crossing location, or prize close
- **replay:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_global_core_rank_support_distance_router/verify.py`
- **independent audit:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_global_core_rank_support_distance_router/verify_audit.py`
