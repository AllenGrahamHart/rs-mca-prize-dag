# Claim contract

- **Claim:** exceptional-root evaluation of the Hankel coefficient plane is
  an `e`-dimensional weighted self-dual code with complementary-minor law
  `(HSD5)`.
- **Scope:** the official exceptional-only face, including both sharp
  high-distance endpoint profiles.
- **Dependencies:** the rank-one coefficient flag and nonzero exceptional
  source representation.
- **Consumer:** the high-distance branch of `rate_half_band_closure`.
- **Falsifier:** evaluation dimension other than `e`, a nonzero weighted Gram
  entry, a basis whose complement is not a basis, or failure of `(HSD5)`.
- **Nonclaims:** no general classification of weighted self-dual codes and no
  endpoint exclusion are asserted.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_exceptional_self_dual_evaluation_code/verify.py`
