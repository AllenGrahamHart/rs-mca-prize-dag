# Claim contract

- **Claim:** adjoining `Xq_0` to the coefficient plane gives the common
  orthogonal complement, on which the Hankel pencil has ranks zero and one.
- **Scope:** the official exceptional-only face in the local coordinate
  `z=E/H`.
- **Dependencies:** the coefficient bi-isotropic plane and kernel-plane
  transversality.
- **Consumer:** the high-distance and component classifiers under
  `rate_half_band_closure`.
- **Falsifier:** a coefficient vector pairing nontrivially with `v` under
  `M_1`, unequal orthogonal complements, or restricted rank other than
  `(0,1)`.
- **Nonclaims:** no classification of the common isotropic plane or endpoint
  exclusion is asserted.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_coefficient_rank_one_flag/verify.py`
