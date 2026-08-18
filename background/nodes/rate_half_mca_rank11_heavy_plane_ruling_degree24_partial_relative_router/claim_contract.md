# Claim contract

- **claim id:** `rate_half_mca_rank11_heavy_plane_ruling_degree24_partial_relative_router`
- **status:** `PROVED`
- **input:** the actual degree-24 order-32 packet from
  `rate_half_mca_rank11_heavy_plane_ruling_degree24_order32_seed`
- **normalization:** use the exact common-support cancellation already
  proved by the parent; do not invoke the narrower maximal-core adapter
- **output:** pure locator, scalar-locator rational/denominator-root, or
  `chi>=2299571` on the original exact heavy-ruling supports
- **preserved/lifted:** slope degree `24..31`, denominator degree at most
  `67472`, affine locator scalars, monic locators, slopes, first ownership,
  received line, and support labels
- **nonclaims:** no branch payment, local-core synchronization, whole-line
  owner, adjacent safety, or prize closure
- **replay:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_plane_ruling_degree24_partial_relative_router/verify.py`
- **independent audit:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_plane_ruling_degree24_partial_relative_router/verify_audit.py`
