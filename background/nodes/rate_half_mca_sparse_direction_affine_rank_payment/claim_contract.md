# Claim contract

- **claim id:** `rate_half_mca_sparse_direction_affine_rank_payment`
- **status:** `PROVED`
- **input:** one codeword gauge, support size `1<=e<d`, and transformed
  explanation affine rank at most `r`
- **output:** ambient-independent bound `(SR1)` and exact deployed walls
- **nonclaims:** no forced rank/support condition, no middle-cell payment,
  no row or prize closure
- **replay:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_sparse_direction_affine_rank_payment/verify.py`
- **independent audit:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_sparse_direction_affine_rank_payment/verify_audit.py`
