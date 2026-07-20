# Claim contract

- **scope:** official quotient-distance-three support packets
- **input:** the matching-free boundary values and support-only dual
  row-product residues
- **currency:** the quotient group `F_q^*/(F_q^*)^r` and one fixed-point-free
  label involution
- **output:** an exact matching-free existence test for a perfect matching
  satisfying both gate families, plus aggregate obstructions
  `(JRM7)--(JRM8)`
- **consumer:** `rate_half_band_closure`
- **load-bearing hypotheses:** the derivative formulas for `C(a),C(t)`;
  the boundary equivalence `Y_b=-Y_a`; the exact row product
  `R_(a,b)=-M/(C(a)C(b))`; odd characteristic
- **nonclaim:** the joint matching test does not allocate internal slopes,
  certify row squarefreeness, or imply the external resultant power
- **failure certificate:** a pair whose two original gates disagree with
  the `tau` relation, or a `tau`-invariant label multiset without a
  reconstructible joint-admissible matching
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_joint_boundary_residue_matching_router/verify.py`
- **upstream mapping:** exact finite primitive shift-pair joint boundary and
  power-residue matching gate
