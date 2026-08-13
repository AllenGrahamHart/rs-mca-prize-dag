# Claim contract

- **Claim:** every center locator is coprime to its corresponding `G`
  fiber, and the center-specialized Pade numerator factors as `(CCP7)`.
- **Inputs:** the off-line-only classified-row roots, the exact
  correction-supported four-core, and the Pade syzygy.
- **Output:** nonvanishing at the padded center, nonvanishing of the cubic
  heavy residual there, and exact center Pade quotients.
- **Consumer:** `rate_half_band_crossing_location`.
- **Nonclaims:** no relation among the three quotient polynomials
  `C_gamma` is asserted.
- **Falsifier:** a center common root of `Qbar` and `G`, or a center
  specialization of `B_src` not divisible by the missing-class locator.
