# Claim contract

- **claim id:** `rate_half_mca_rank11_dense_pair_degree18_seed_compiler`
- **status:** `PROVED`
- **input:** an unsafe deployed post-near error-rank-eleven line and the
  proved low-margin minimizing-pair ledger
- **output:** `32` actual low-margin records, eighteen on one fixed pair,
  with common support at most `K-2601` and residual slope degree `18..31`
- **preserved:** field, received line, distinct slopes, exact supports,
  support-wise badness, pair labels, and chronology
- **method:** exact pigeonhole; ten-dimensional component basis; mixed
  one/two-record core forcing; eighteen-root affine-line interpolation pin
- **nonclaims:** no S/A/E payment, rational-owner payment, primitive-spread
  abundance theorem, adjacent-row safety, or prize closure
- **replay:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_dense_pair_degree18_seed_compiler/verify.py`
- **independent audit:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_dense_pair_degree18_seed_compiler/verify_audit.py`
