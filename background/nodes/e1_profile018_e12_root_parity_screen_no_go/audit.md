# Audit

- The local condition is checked on the folded parity polynomial, not inferred
  merely from the number of odd lags.
- The primitive root is explicit and its order is checked exactly.
- Fejer positivity applies for every real angle, so no numerical sampling of
  conjugates is used.
- The cubic index is replayed both by direct ordered triples and by the
  independent additive-relation formula in the verifier.
- SymPy's exact subresultant engine replays the degree-128 resultant in well
  under one second; reciprocal pairing is checked by an exact integer square.
- No coefficient realization is claimed.
