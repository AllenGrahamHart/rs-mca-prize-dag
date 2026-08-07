# Claim contract

- **claim id:** `dli_wcl_ell1_weight6_unsigned_sign_product_router`
- **status:** `PROVED`
- **scope:** reduced signed weight-six relations at the order-512 terminal
  level
- **consumer:** `dli_wcl_slot_1_6_emptiness`
- **proved content:** exact 32-sign aggregation, norm-support identity, two
  product sectors, and `11,650,060` affine-Galois orbits
- **new open content:** control the prime divisors of the unsigned aggregate
  norms at the official `v_2(q-1)>=41` gate
- **falsifier:** a square-root choice changing `Psi_6`, a missed signed lift,
  or a Burnside fixed-point/count mismatch
- **nonclaims:** no aggregate norm has been computed or factored; no cost
  reduction or slot exclusion follows from class compression alone
- **replay:** `tools/ramguard tiny -- python3 background/nodes/dli_wcl_ell1_weight6_unsigned_sign_product_router/verify.py`
- **independent audit:** `tools/ramguard tiny -- python3 background/nodes/dli_wcl_ell1_weight6_unsigned_sign_product_router/verify_audit.py`
- **upstream mapping:** `OURS_ONLY`; finite WCL divisor arithmetic
