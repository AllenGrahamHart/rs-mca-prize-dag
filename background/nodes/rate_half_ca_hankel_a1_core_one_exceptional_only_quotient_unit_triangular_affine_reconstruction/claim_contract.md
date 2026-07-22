# Claim contract

- **Claim:** the clean-fiber correction polynomials `A_W,B_W` are uniquely
  reconstructed by the affine residue tests `(QTA4)--(QTA6)`; a non-affine
  residue excludes the packet.
- **Scope:** the official exceptional-only corrected square, including both
  sharp high-distance endpoint profiles.
- **Dependencies:** the `W_vee` interpolation normal form, reciprocal Bezout
  coprimality, and the full unit equation.
- **Consumer:** the high quotient-distance branch of
  `rate_half_band_closure`.
- **Falsifier:** two affine representatives of one residue class, a valid
  corrected square with a non-affine `rho_k`, or failure of the reconstructed
  coefficients to satisfy the unit equation.
- **Nonclaims:** the deterministic residue sequence is not yet proved to
  fail on either endpoint profile; Hankel compatibility remains to be used.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_unit_triangular_affine_reconstruction/verify.py`
