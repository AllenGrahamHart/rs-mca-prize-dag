# Lineage

- The global quadratic quotient and compact kernel supply the exact source
  algebra and direct-lift maps.
- Same-sign `paired(q,q)` factored into rational branches in the preceding
  xi3 theorems. The opposite-sign equation instead becomes an even quartic,
  quadratic in `x=q^2`.
- A first implementation using repeated six-dimensional inversions timed out
  at 300 seconds. Caching the single quartic leading-coefficient inverse and
  descending through parity reduced representative pairing 3 to 74-140
  seconds per source row.
- Representative pairings 4 and 5 are not claimed: the current
  quartic-versus-quadratic implementation for pairing 4 still timed out at
  300 seconds and requires a lower-growth compiler.
- The result remains background evidence toward `rate_half_band_closure`.
