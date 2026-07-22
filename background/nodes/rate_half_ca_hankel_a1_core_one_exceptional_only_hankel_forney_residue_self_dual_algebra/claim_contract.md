# Claim contract

- **Claim:** normalized incidence coefficients form a self-dual half-space
  in `F[X]/(A)` for the explicit Forney residue unit `C`, with product-space
  dichotomy `(HFR7)`.
- **Scope:** both sharp high-distance endpoint profiles.
- **Dependencies:** the split self-dual frame and general-distance Forney
  numerator normal form.
- **Consumer:** the high-distance branch of `rate_half_band_closure`.
- **Falsifier:** a nonunit in `(HFR2)`, failure of the normalized Gram law,
  product span outside the residue hyperplane, or nonunique `C` when the
  product span has codimension one.
- **Nonclaims:** neither the codimension-one nor degenerate product branch is
  classified at official scale.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_residue_self_dual_algebra/verify.py`
