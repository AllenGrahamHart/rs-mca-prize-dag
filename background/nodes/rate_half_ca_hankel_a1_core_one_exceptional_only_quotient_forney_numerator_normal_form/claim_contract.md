# Claim contract

- **scope:** every minimal quotient support on the official `A=1`, core-one,
  exceptional-only sharp-cap profile
- **input:** the first-order kernel equation, quadratic transversality, exact
  row saturation, and a minimal quotient support `T`
- **currency:** weighted GRS syndrome duality and the top Lagrange coefficient
- **output:** the unique degree-`h-3` numerator `F` in `(QFN3)--(QFN7)`
- **consumer:** `rate_half_band_closure`
- **load-bearing hypotheses:** the exceptional locator `A` is monic and
  squarefree; `T` is disjoint from its roots and minimal; `Theta_2!=0`; the
  source representations and first-order kernel equation are the ones in
  the proved exceptional-only packet; every exceptional root is a simple
  parameter root in its saturated row
- **nonclaim:** no support polynomial `B_T` is classified, counted, or
  excluded
- **failure certificate:** a minimal support whose weights violate `(QFN4)`,
  an exceptional root violating `(QFN5)`, or a numerator with degree or
  leading coefficient different from `(QFN3)`
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_forney_numerator_normal_form/verify.py`
- **upstream mapping:** exact finite primitive shift-pair GRS/Forney key
  equation
