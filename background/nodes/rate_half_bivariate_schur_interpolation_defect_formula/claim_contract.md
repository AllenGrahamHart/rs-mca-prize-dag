# Claim contract

- **Claim:** every residual Schur entry is the explicit interpolation defect
  `(SID3)` or unchanged lower-clone entry `(SID4)`.
- **Dependency:** `rate_half_bivariate_top_vandermonde_schur_reduction`.
- **Inputs:** pivot set `P`, domain points, coordinate incidence roots,
  fibre roots, and deficiencies.
- **Output:** `(SID3)--(SID6)`.
- **Consumer:** the residual rank attack on
  `rate_half_band_crossing_location`.
- **Nonclaims:** no universal nonzero minor, no bad-overlap implication, and
  no treatment that discards lower deficiency clones.
- **Falsifier:** disagreement between direct block elimination and `(SID3)`,
  an altered lower clone under elimination, or a failed symmetric-root
  coefficient identity.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_bivariate_schur_interpolation_defect_formula/verify.py`
  and `verify_audit.py`.
