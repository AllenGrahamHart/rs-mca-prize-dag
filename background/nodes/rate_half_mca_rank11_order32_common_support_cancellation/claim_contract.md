# Claim contract

- **claim id:** `rate_half_mca_rank11_order32_common_support_cancellation`
- **status:** `PROVED`
- **input:** the 32 actual records emitted by
  `rate_half_mca_rank11_heavy_pair_order32_seed_compiler`
- **output:** a common-support-free 32-record support-wise MCA-bad family in
  `RS[F,D\C,K-|C|]` at agreement `m-|C|`
- **preserved:** field, slopes, labels, exact supports after deletion,
  support-wise badness, received-line chronology, `n-K`, `m-K`, and critical
  order 32
- **residual range:** `4923<=K-|C|<=1048576`
- **surviving frontier:** a uniform partial-relative/same-owner theorem on
  the punctured evaluation domain, or a route that restores deployed-domain
  structure before classification
- **nonclaims:** no automatic specialization of the deployed dyadic theorem,
  no S/A/E classification or payment, no row or prize conclusion
- **replay:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_order32_common_support_cancellation/verify.py`
- **independent audit:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_order32_common_support_cancellation/verify_audit.py`
