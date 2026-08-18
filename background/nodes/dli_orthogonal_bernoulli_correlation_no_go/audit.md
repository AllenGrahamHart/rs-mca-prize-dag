# Audit

- The equations are over the integers, so subtraction may use the factor two.
  The same fixture also works in every odd characteristic before modular
  wraparound is introduced.
- Orthogonality is between the complete `U` and `V` row spaces, not merely
  between one selected pair of rows.
- Tensorization uses disjoint coordinate blocks; it does not assume the two
  events within one block are independent.
- The dense refinement is an invertible change of equation basis, not a
  rotation of the Bernoulli coordinates. It therefore preserves the events
  exactly.
- `H_r` is invertible in odd characteristic because `r` is a power of two;
  no characteristic-dividing determinant case is silently included.
- The no-go scope deliberately omits cyclic phase progression, frequency
  allocation, and primitivity. Those are exactly the structures a surviving
  DLI proof must exploit.
- The `r=3` square-root failure is checked by an integer comparison, with no
  floating-point threshold decision.
