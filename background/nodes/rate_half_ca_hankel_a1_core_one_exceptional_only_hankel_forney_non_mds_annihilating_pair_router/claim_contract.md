# Claim contract

- **Claim:** complementary maximal-minor failure yields two independent
  elements of `U_q` with complementary zero sets and zero product, whose
  gcds with `A` obey the exact factor dichotomy `(HNA3)--(HNA4)`.
- **Scope:** the non-MDS branch of the exceptional self-dual code.
- **Dependencies:** the MDS-Schur router and the reduced Forney algebra.
- **Consumer:** the high-distance branch of `rate_half_band_closure`.
- **Falsifier:** a non-MDS packet for which every complementary singular pair
  fails to produce `(HNA1)`, or whose gcd locators violate `(HNA3)--(HNA4)`.
- **Nonclaims:** no lower bound is asserted for the nonzero coordinates of
  either element, and no official exclusion is claimed.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_non_mds_annihilating_pair_router/verify.py`
