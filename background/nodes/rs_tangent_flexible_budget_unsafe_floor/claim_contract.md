# Claim contract

## Proved

- One line has at least `n-a` distinct bad slopes at radius `1-a/n` whenever
  `k<a<n` and `n-a<=q`.
- `n-a>floor(q/2^t)` is a strict unsafe certificate at target `2^-t`.
- The theorem is valid over arbitrary finite fields and evaluation sets.

## Not proved

- Failure of the sufficient inequality is not a safety certificate.
- No quotient/E1, averaged-occupancy, or cap witness is asserted.
- No proposed safe agreement or adjacent endpoint is validated by this theorem
  alone.

## Falsifier

A valid row and agreement satisfying the premises for which the constructed
line has fewer than `n-a` distinct bad slopes, or an endpoint conversion that
fails strictness, falsifies the node.
