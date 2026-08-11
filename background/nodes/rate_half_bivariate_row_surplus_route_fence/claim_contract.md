# Claim contract

- **Claim:** all ten canonical deficiency-aware matrices of the published
  `m=1`, `q=17` five-slope witness are `15 x 6` of rank five.
- **Dependencies:** the exact `m=1` witness and the deficiency-aware matrix
  reduction.
- **Output:** `(BRS2)` and a route fence against raw overdetermination.
- **Consumer:** the rank attack on `rate_half_band_crossing_location`.
- **Nonclaims:** no official-scale counterexample, no assertion that rank
  defect persists for `m>1`, and no refutation of a structured rank theorem.
- **Falsifier:** a failed witness equation, a pair union containing the
  deficient point, a nonzero matrix-kernel product, or a zero printed minor.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_bivariate_row_surplus_route_fence/verify.py` and
  the independent Cramer-rule audit `verify_audit.py`.
