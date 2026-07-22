# Claim contract

- **Claim:** identically singular Pade circuits are exactly the subsets of
  unique bounded-degree rational relation classes, with the printed
  intersection, size, shadow, and official large-class bounds.
- **Scope:** every bounded-tail involution support branch after the Pade
  circuit reduction, including absorbed quartic pullbacks.
- **Dependency:** bounded-error Pade-circuit reduction.
- **Consumer:** `rate_half_band_closure`; converts the zero-circuit leaf into
  one explicit fixed-factor bound.
- **Falsifier:** a zero circuit admitting no relation, one admitting two
  distinct primitive relations, two classes meeting in more than `2t`
  points, a class larger than `e+t`, or failure of either official shadow
  integer.
- **Nonclaims:** the required `172409`/`2127` upper bounds are not proved
  here.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_pade_relation_class_reduction/verify.py`
