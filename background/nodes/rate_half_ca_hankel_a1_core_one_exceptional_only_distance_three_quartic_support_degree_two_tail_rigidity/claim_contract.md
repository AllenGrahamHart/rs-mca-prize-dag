# Claim contract

- **Claim:** every official degree-two support survivor has at most six
  off-involution exceptional pairs in the antipodal case and at most eight
  in the constant-product case.
- **Scope:** both the ordinary ratio-field branch and the degree-two branch
  obtained after global antiweight absorption.
- **Dependencies:** the degree-two subgroup router, actual internal-slice
  quartics, and antiweight absorption.
- **Consumer:** `rate_half_band_closure`; sharpens the tail input to the
  bounded-error complement trace.
- **Falsifier:** nine tail pairs in either branch, seven antipodal tail
  pairs, three proportional quartics `P_l=c_lD_l^2`, or five distinct
  non-proportional no-fixed-point tails charged to one quartic `P_m`.
- **Nonclaims:** this does not yet classify the degree-`e+d` complement
  traces or the degree-four pullback branch.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_degree_two_tail_rigidity/verify.py`
