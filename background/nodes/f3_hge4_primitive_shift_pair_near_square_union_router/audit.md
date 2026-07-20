# Audit

- Used odd characteristic when dividing by two and taking the centered
  polynomial; every official row has odd prime characteristic.
- Required `d_U^2` to be nonzero. The zero case would repeat one locator and
  would not give disjoint supports.
- Reconstructed factors from the squarefree union locator, so both factors
  are automatically split over `H` and disjoint.
- Proved uniqueness of the centered polynomial before using the union
  stabilizer action.
- Distinguished a free union orbit from the antipodal swap orbit. The latter
  has `n/2` unions but still lifts to one free ordered-pair orbit of size `n`.
- Counted distinct anchored unions, not the `2h` scale choices before
  stabilizer deduplication.
- The primitive test remains load-bearing. Nonprimitive unions can have larger
  stabilizers and are charged to quotient recursion instead.
- The candidate-space factor compares complete anchored raw spaces; it is an
  algorithmic reduction, not a bound on survivors.

