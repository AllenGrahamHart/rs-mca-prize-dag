# Claim contract

- **Claim:** clean-incidence second jets reconstruct `W_vee,t` on every
  clean fiber and force all normalized derivative polynomials `D_gamma` onto
  one affine parameter line, equal to the unit-reconstructed corrections.
- **Scope:** both official sharp high quotient-distance endpoint profiles.
- **Dependencies:** reciprocal first complement, clean first jets, the
  `W_vee` interpolation normal form, and the unit-remainder reconstruction.
- **Consumer:** the high-distance branch of `rate_half_band_closure`.
- **Falsifier:** a valid corrected square violating `(QSJ2)`, nonunique
  derivative interpolation, non-affine clean-slope data, or disagreement
  between the Hermite and unit correction pairs.
- **Nonclaims:** the affine consistency or comparison is not yet proved to
  fail for either endpoint profile.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_clean_fiber_second_jet_hermite_gate/verify.py`
