# Claim contract

- **claim id:** `rate_half_mca_rank11_heavy_ruling_triple_owner_pole_simple_router`
- **status:** `PROVED`
- **input:** the heavy Segre ruling orientation, exact order-32
  partial-relative theorem, and pole-tolerant scalar-locator semantics
- **selection:** discard pair types with at most two owners; retain three
  slopes from every represented pair and at least 20 from the anchor
- **output:** `chi>=2299571`, or a rational certificate with no common
  domain pole and at most `67472` singleton pole-support incidences
- **preserved:** first-owned slope/pair labels, exact support size,
  core-saturated supports, support-wise badness, and degree `20..31`
- **nonclaims:** no payment of the rational or high-complexity output,
  no packet globalization, whole-line owner, adjacent safety, or closure
- **replay:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_ruling_triple_owner_pole_simple_router/verify.py`
- **independent audit:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_ruling_triple_owner_pole_simple_router/verify_audit.py`
