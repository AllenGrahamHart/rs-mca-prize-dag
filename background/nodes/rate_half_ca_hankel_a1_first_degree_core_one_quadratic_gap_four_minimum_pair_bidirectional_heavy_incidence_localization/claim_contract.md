# Claim contract

- **Claim:** both oriented minimum-pair row families have rank two; their
  gcds exchange endpoints, all residual root sets are mutually disjoint,
  and every residual root has zero heavy deficit.
- **Inputs:** exact light-row saturation, actual error supports, the complete
  coefficient-chain nullspace, minimum distance `2rho+1`, packet deficit
  `e-6`, and projective linearity of a codeword pencil.
- **Outputs:** bidirectional coupling `(BHL3)`, deficit-free residuals
  `(BHL4)`, exact slack `(BHL5)`, line-deficit cap `(BHL7)`, and the
  arm-specific gcd floors `(BHL8)--(BHL9)`.
- **Falsifier:** a padded heavy point in an actual error support, a positive-
  deficit residual root off the endpoint line, a shared cross-orientation
  residual root, or a missing-incidence total exceeding the light-row
  support degree.
- **Nonclaims:** the unused slack is not asserted empty, the heavy factor is
  not asserted to divide either gcd, and the `rho+3` pair is not excluded.
