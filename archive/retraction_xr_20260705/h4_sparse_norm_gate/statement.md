# h4_sparse_norm_gate

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/x30_finite_p_norm_gate.md']

## Statement

The h=4 8-sparse cyclotomic norm-gate residue is excluded at the official rows:
after the paid antipodal branch, no official row prime divides an uncharged
resultant `Res(Phi_n, f)` for an 8-sparse signed exponent word `f`.

For downstream consumers, this node is used in the generalized x83 form recorded
in `dag.json`: official row primes divide no cleared obstruction norm in any
live h-window; the h=4 8-sparse resultant is the named base case.

## Attack surface

The resultant `Res(Phi_n, f)` is explicit. A falsifier is an official row prime
dividing one of these uncharged resultants.

## Ledger

A3 plus the closure assembly reduce the h=4 residue, and its x83-generalized
window form, to the row-independent good-reduction exceptional set and the row
GCD tests.
