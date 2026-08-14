# Claim contract

- **claim id:** `rate_half_mca_rank11_shortened_partial_relative_router`
- **status:** `PROVED`
- **input:** the non-affine degree-18 order-32 seed from
  `rate_half_mca_rank11_dense_pair_degree18_seed_compiler`
- **normalization:** complete maximal-common-core cancellation, retaining
  actual support-wise noncontained witnesses
- **output:** pure locator, scalar-locator rational/denominator-root, or
  `chi>=2299571` on the original exact KoalaBear supports
- **preserved/lifted:** slope degree `18..31`, denominator degree at most
  `67472`, affine locator scalars, monic locators, original slopes, received
  line, and support labels
- **nonclaims:** no S/A/E payment, coherence over every 32-subset,
  whole-line owner, adjacent safety, or prize closure
- **replay:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_shortened_partial_relative_router/verify.py`
- **independent audit:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_shortened_partial_relative_router/verify_audit.py`
