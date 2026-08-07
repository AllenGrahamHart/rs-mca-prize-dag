# Claim contract

- **claim id:** `dli_wcl_ell1_weight6_pair_heron_norm_router`
- **status:** `PROVED`
- **scope:** any pairing of a reduced order-512 weight-six support
- **consumer:** `dli_wcl_slot_1_6_emptiness`
- **proved dependency:** the unsigned sign-product router
- **proved content:** exact partition of 32 sign classes into eight Heron
  factors and the three-quadratic norm identity
- **new open content:** exploit the six-term Heron factors to exclude official
  prime divisors without enumerating or factoring one aggregate norm per orbit
- **falsifier:** one missing/duplicated sign class, an incorrect Heron factor,
  or a pairing for which the quadratic norm identity fails
- **nonclaims:** no prime factor, orbit, or official row is excluded
- **replay:** `tools/ramguard tiny -- python3 background/nodes/dli_wcl_ell1_weight6_pair_heron_norm_router/verify.py`
- **independent audit:** `tools/ramguard tiny -- python3 background/nodes/dli_wcl_ell1_weight6_pair_heron_norm_router/verify_audit.py`
- **upstream mapping:** `OURS_ONLY`; WCL terminal arithmetic
