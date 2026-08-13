# Claim contract

- **Claim:** at every finite degree-preserving locator fiber, the regular
  Hankel block, the Pade Bezoutian, and the contact-algebra presentation
  have identical local Smith invariants.
- **Dependencies:** the contracted Pade numerator and moment-kernel
  identities.
- **Output:** `(BCM3)--(BCM4)`.
- **Consumer:** the exact nonreduced collision router.
- **Nonclaims:** no degree-drop or infinity chart; no conversion of divisor
  length into invariant factors without computing the local module.
- **Falsifier:** a unit-leading locator for which the Bezout Gram identity
  or contact-module Smith factors differ.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_pade_bezout_contact_module_presentation/verify.py`.
