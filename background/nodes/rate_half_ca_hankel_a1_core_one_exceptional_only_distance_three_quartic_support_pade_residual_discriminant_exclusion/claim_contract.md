# Claim contract

- **Claim:** the degree-`1..4` aligned residual pencil is impossible, so the
  complete all-deficient quartic-support branch is excluded.
- **Scope:** all bounded-tail involution branches, including absorbed
  degree-four pullbacks and antiweight.
- **Dependencies:** aligned residual degree-four reduction and pullback
  absorption.
- **Consumer:** `rate_half_band_closure`; closes the support-side obstruction
  on the saturated `A=1,s=1,e=2m-1` distance-three face.
- **Falsifier:** a good internal specialization not proportional to its
  square norm, nonzero residual discriminant, or two distinct squarefree
  residual divisors surviving `(QPRD4)`.
- **Nonclaims:** other rate-half faces and post-support internal/external
  constraints are not closed by this theorem.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_pade_residual_discriminant_exclusion/verify.py`
