# Claim contract

- **Claim:** every bounded-tail degree-two survivor yields the printed
  Pade-circuit determinants and forces the exact incidence lower bound on
  identically singular circuits.
- **Scope:** official antipodal `t<=6` and constant-product `t<=8` branches,
  including absorbed quartic pullbacks; the algebraic formulas hold for any
  `t` with `e>=2(t+1)`.
- **Dependencies:** bounded row codegree, tail rigidity, calibrated internal
  trace values, and the exact external split design.
- **Consumer:** `rate_half_band_closure`; replaces an uncontrolled
  degree-`e+t` complement family by one explicit determinantal obstruction.
- **Falsifier:** a complement violating `(QPCIR2)`, a selected subset with
  `Delta_S(u)!=0`, determinant degree above `2(t+1)`, or failure of either
  official integer inequality.
- **Nonclaims:** no upper bound for identically zero circuit determinants is
  proved here; that is the remaining degree-two leaf.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_bounded_error_pade_circuit_reduction/verify.py`
