# Claim contract

- **Claim:** the `O(1)+O(-rho)^(m-1)` elementary-modification branch is
  impossible for the clean `m>1` bidegree; only `(REB2)` remains.
- **Dependency:**
  `rate_half_ca_hankel_clean_endpoint_picard_kernel_elementary_modification_dichotomy`.
- **Output:** exact unique-section splitting `(REB2)--(REB3)`.
- **Consumer:** the clean branch of `rate_half_band_crossing_location`.
- **Nonclaim:** no exclusion of the unique-section branch.
- **Falsifier:** a smooth rational divisor of bidegree `(4m-1,m)` for
  `m>1`, or a failure of the dichotomy to imply rationality in `(REB1)`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_clean_endpoint_rational_elementary_branch_exclusion/verify.py`
  and `verify_audit.py`.
