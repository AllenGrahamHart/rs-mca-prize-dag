# Audit

- The local condition is checked on the folded parity polynomial, not inferred
  merely from the number of odd lags.
- The primitive root is explicit and its order is checked exactly.
- Fejer positivity applies for every real angle, so no numerical sampling of
  conjugates is used.
- The cubic index is replayed both by direct ordered triples and by the
  independent additive-relation formula in the verifier.
- No coefficient realization or exact norm is claimed.
