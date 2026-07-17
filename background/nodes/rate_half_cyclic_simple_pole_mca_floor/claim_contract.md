# Claim contract

- **Claim:** the proved cyclic cap-row list, inserted into the exact
  quantitative simple-pole formula, gives
  `epsilon_ca,epsilon_mca>2^-83` through the longest residual prefix.
- **Quantifiers:** the official `n=2^41`, `k=2^40` row; every finite field
  `q<2^256` admitting the order-`n` multiplicative domain; every integer
  `sigma` with `1<=sigma<=8,594,128,895`.
- **Dependencies:** `rate_half_cyclic_rotated_prefix_floor`; elementary
  polynomial root counting, collision averaging, and Cauchy-Schwarz.
- **Trigger repair:** `L>(q-n)/k` is sufficient for the stronger clean
  `~1/(2k)` floor, not necessary for exceeding the prize target. This node
  uses `L(q-n)/(q(q-n+kL))` exactly and does not use list unsafety as an MCA
  surrogate.
- **Consumers:** the lower bracket for the re-posed rowwise
  `rate_half_band_closure`, including the refutation of its former fixed safe
  point.
- **Nonclaims:** no MCA safe-side theorem, no statement for another rate, and
  no strengthening of the cyclic locator construction itself.
- **Falsifier:** a failed simple-pole hypothesis, an incorrect collision
  degree, failure of either exact inequality in (3), `s=c-1` violating the
  rotated-prefix degree blocks, or a claimed radius outside the conversion
  interval.
- **Upstream crosswalk:** Paper D v13,
  `prop:quantitative-deep-list-floor` and `cor:deep-list-trigger-ceiling`.
