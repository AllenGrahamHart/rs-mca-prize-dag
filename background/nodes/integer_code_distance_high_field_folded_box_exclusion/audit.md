# Audit

- The crude bound `256^32=2^256` is not consumed.
- If any folded coefficient is odd, discreteness improves the squared mass
  from `256` to at most `253`.
- If all coefficients are even, division by two is load-bearing: the odd row
  prime divides `N(W)` if and only if it divides `N(W/2)`.
- Characteristic-zero nonvanishing follows from `deg W<deg Phi_128`; it is
  not inferred from a failed finite-field search.
- This theorem certifies a kernel, not a value-set cardinality. A consumer
  must still prove that its quotient cell is large enough for the row budget.
- No computation or survival evidence is used in the proof.
