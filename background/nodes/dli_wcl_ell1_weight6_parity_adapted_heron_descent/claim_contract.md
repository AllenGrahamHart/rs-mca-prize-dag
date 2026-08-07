# Claim contract

- **claim id:** `dli_wcl_ell1_weight6_parity_adapted_heron_descent`
- **status:** `PROVED`
- **scope:** both product-parity sectors of the unsigned `(1,6)` router
- **consumer:** `dli_wcl_slot_1_6_emptiness`
- **proved content:** an all-`K_0` eight-Heron presentation in the even sector
  and four explicit one-quadratic norms in the odd sector
- **new open content:** bound the rational prime support of these `K_0`
  factors at `v_2(q-1)>=41`
- **falsifier:** a parity pattern forcing more mixed pairs, or failure of
  `(PAD2)`
- **nonclaims:** no norm, prime, orbit, or official row is excluded
- **replay:** `tools/ramguard tiny -- python3 background/nodes/dli_wcl_ell1_weight6_parity_adapted_heron_descent/verify.py`
- **independent audit:** `tools/ramguard tiny -- python3 background/nodes/dli_wcl_ell1_weight6_parity_adapted_heron_descent/verify_audit.py`
- **upstream mapping:** `OURS_ONLY`; WCL terminal arithmetic
