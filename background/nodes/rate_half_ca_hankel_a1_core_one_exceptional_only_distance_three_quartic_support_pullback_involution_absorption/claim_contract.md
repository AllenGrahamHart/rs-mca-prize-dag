# Claim contract

- **Claim:** every quartic pullback survivor is globally a six-tail
  antipodal or eight-tail constant-product matching, with stronger `2/4`
  bounds on the antiweight-derived branch.
- **Scope:** all classified pullbacks `F(X^2)`, `F(X^4)`, and `F(X+c/X)` in
  both ordinary and antiweight-derived common-field branches.
- **Dependencies:** quartic deck classification, antiweight absorption, and
  the internal-slice proportional-quartic cap.
- **Consumer:** `rate_half_band_closure`; removes the independent quartic
  pullback leaf and routes it to the static simultaneous-gcd obstruction.
- **Falsifier:** twelve captured non-orbits in the reciprocal branch, ten in
  the antipodal branch, failure to find one exact deck orbit, or a final
  matching with more than eight/six tails.
- **Nonclaims:** the simultaneous Pade gcd bound is not proved here.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_pullback_involution_absorption/verify.py`
