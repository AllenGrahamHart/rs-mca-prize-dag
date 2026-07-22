# Claim contract

- **Claim:** the absolutely irreducible Laurent-end quartic curve cannot
  contain the official `e-148` matched fibers.
- **Scope:** the official prime-field degree-four support branch.
- **Dependency:** completed degree-four irreducible/reducible routing.
- **Published input:** Corvaja--Zannier Theorem 2, pinned in `source.md`.
- **Consumer:** `rate_half_band_closure` and the symbolic support classifier.
- **Falsifier:** an absolutely irreducible Laurent-end curve with at least
  `2(e-148)` ordered points in `mu_N x mu_N`, or failure of a printed degree,
  genus, support, differential, or integer margin.
- **Nonclaims:** cyclic/dihedral pullbacks and the bounded-tail degree-two
  matching remain open.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_laurent_gcd_exclusion/verify.py`
