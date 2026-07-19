# Claim contract

- **Claim:** maximal separation rank `m+1` of the full strict-endpoint
  generator, together with residual parameter degree `b`, forces the dominant
  component to have separation rank at least `ceil((m+1)/(b+1))`, hence at
  least five under the exact defect ledger.
- **Scope:** geometric separation rank after scalar extension for the
  irreducible factors of the official first strict endpoint.
- **Dependencies:**
  `rate_half_ca_hankel_endpoint_rational_normal_kernel_curve` supplies
  `sr(Q)=m+1`; `rate_half_ca_hankel_endpoint_component_defect_localization`
  supplies `b<=floor((O-E)/4)<=m/4-1`.
- **Consumer:** the strict `e=m`, `A=3` branch of
  `rate_half_band_closure`.
- **Nonclaims:** tensor-rank submultiplicativity is used only for the
  two-factor separation rank; no rank-five classification or endpoint
  contradiction is asserted.
- **Next exact gate:** combine rank at least five with the Hankel coefficient
  chain, multiplicative-domain hyperplanes, and low-defect norm identity.
