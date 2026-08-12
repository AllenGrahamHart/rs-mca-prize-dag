# Claim contract

- **claim id:** `rate_half_mca_sparse_direction_heavy_fiber_profile`
- **status:** `PROVED`
- **input:** a codeword-gauged direction with `1<=e<d`, exact
  pair-noncontained witnesses, and transformed explanation affine rank at
  most `r`
- **output:** the cumulative deficit caps `B_h`, profile bound `(HF1)`, and
  exact deployed paid prefixes with adjacent failures
- **nonclaims:** no forced rank/support condition, no global maximality of
  the printed prefixes, no middle-cell or prize closure
- **replay:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_sparse_direction_heavy_fiber_profile/verify.py`
- **independent audit:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_sparse_direction_heavy_fiber_profile/verify_audit.py`
