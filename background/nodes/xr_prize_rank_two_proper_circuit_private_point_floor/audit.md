# Audit

- `(PF2)` is valid with arbitrary outside multiplicity. It does not assume
  the zero-defect multiplicity-one/two normal form.
- The correction `+2C+I` is retained before taking the weaker rank floor.
- Reused active-zero points are not private: every other circuit support
  contains them because the zero fibers are disjoint.
- Each added host block absorbs at most `a` private points from each circuit
  row. The proof does not charge its whole size independently to every row.
- The exact prize caps `384,448,960` are applied only to prize rows.
- The full-core and proper-circuit cases are composed only after the Segre
  circuit decomposition supplies a proper four/five-block circuit.
- The printed floors are necessary exclusions, not existence claims.
- No Modal or large local computation is used.
