# Claim contract

- **Claim:** every Pade relation class larger than `4t(t+1)+t` has a
  denominator independent of the orbit coordinate and a quadratic numerator,
  and hence gives the printed three-polynomial common factor.
- **Scope:** bounded-tail involution relation classes over the official base
  field, including absorbed quartic pullbacks; the structural threshold is
  valid for general `t<e`.
- **Dependency:** Pade relation-class reduction.
- **Consumer:** `rate_half_band_closure`; turns the final degree-two leaf into
  an explicit simultaneous univariate Pade gcd bound modulo `P_Z`.
- **Falsifier:** a larger class whose primitive denominator depends on `U`,
  a kernel requiring `U`-degree above `2(t+1)`, or failure of one residual to
  vanish on the class.
- **Nonclaims:** the strict external-factor gcd bounds `172409` and `2127`
  are not yet proved.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_pade_large_class_static_denominator/verify.py`
