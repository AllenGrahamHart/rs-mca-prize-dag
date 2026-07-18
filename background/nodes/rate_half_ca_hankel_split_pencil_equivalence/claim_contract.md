# Claim contract

- **Claim:** exact equivalence between RS proximity syndromes and split
  locator kernels of a Hankel matrix, including the common-support and
  column-far slope-pencil forms.
- **Quantifiers:** every Reed-Solomon code, every `1<=r<=n-k`, and every
  received word or pair.
- **Dependencies:** the standard Vandermonde parity-check presentation of RS
  codes and elementary linear recurrences.
- **Consumer:** the CA-only post-quadratic range of
  `rate_half_band_closure`.
- **Nonclaims:** no bound on the number of supported slopes and no import of
  `spi_point_counting`.
- **Falsifier:** a radius-`r` syndrome with no split kernel locator, or a
  split kernel locator whose syndrome cannot be represented on its roots.
