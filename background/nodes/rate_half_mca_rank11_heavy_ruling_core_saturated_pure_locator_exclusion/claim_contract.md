# Claim contract

- **claim id:** `rate_half_mca_rank11_heavy_ruling_core_saturated_pure_locator_exclusion`
- **status:** `PROVED`
- **input:** the heavy-ruling degree-24 seed and its exact partial-relative
  router
- **support normalization:** after pair ownership is fixed, choose exact
  size-`m` supports containing their assigned pair cores
- **output:** pure locator excluded; the packet is rational with denominator
  degree at most `67472`, or has `chi>=2299571`
- **preserved:** actual slopes and explanations, deterministic pair-owner
  labels, exact support size, noncontainment, degree `24..31`, and
  support-wise MCA badness
- **nonclaims:** no rational or high-complexity payment, packet-core
  globalization, whole-line owner, adjacent safety, or prize closure
- **replay:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_ruling_core_saturated_pure_locator_exclusion/verify.py`
- **independent audit:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_ruling_core_saturated_pure_locator_exclusion/verify_audit.py`
