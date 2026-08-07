# Claim contract

- **claim id:** `dli_wcl_ell1_weight6_conductor_block_norm_gcd_fence`
- **status:** `PROVED`
- **scope:** signed weight-six supports over `Q(zeta_512)` and every
  parity-adapted Heron presentation after maximal two-adic conductor descent
- **consumer:** `dli_wcl_slot_1_6_emptiness`
- **proved content:** exact lower-conductor ownership for all-one-parity
  supports; exact factorization of every mixed-parity base-field block norm
  into two or four complete signed rational norms; no cross-pairing block-gcd
  compression
- **new open content:** exclude official prime divisors of individual
  minimal-conductor signed norms, or add an independent obstruction
- **falsifier:** a support whose maximal descent remains one-parity, a
  parity-adapted block not stable in the asserted form, or a block norm not
  divisible by every signed norm it owns
- **nonclaims:** no signed norm, characteristic, official row, or WCL slot is
  excluded
- **replay:** `tools/ramguard tiny -- python3 background/nodes/dli_wcl_ell1_weight6_conductor_block_norm_gcd_fence/verify.py`
- **independent audit:** `tools/ramguard tiny -- python3 background/nodes/dli_wcl_ell1_weight6_conductor_block_norm_gcd_fence/verify_audit.py`
- **upstream mapping:** `OURS_ONLY`; Przemek's active workboard has no WCL
  tower terminal
