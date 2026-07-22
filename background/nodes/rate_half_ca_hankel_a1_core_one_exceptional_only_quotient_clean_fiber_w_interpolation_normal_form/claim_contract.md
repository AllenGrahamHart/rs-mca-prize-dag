# Claim contract

- **Claim:** first-jet data on all clean fibers determine `W_vee` modulo
  `P_cl`, leaving exactly two degree-at-most-`r-1` correction polynomials.
- **Scope:** the exceptional-only corrected square, including both sharp
  high-distance endpoint profiles.
- **Dependencies:** clean-fiber first-jet transversality and the inherited
  bidegree bound on the complement weld.
- **Consumer:** the high quotient-distance branch of
  `rate_half_band_closure`.
- **Falsifier:** two different degree-at-most-`r-1` clean-fiber
  interpolants, failure of coefficientwise divisibility by `P_cl`, or a
  quotient of parameter degree greater than one.
- **Nonclaims:** the two correction polynomials are not yet classified, and
  the endpoint is not excluded by interpolation alone.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_clean_fiber_w_interpolation_normal_form/verify.py`
