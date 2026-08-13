# Audit

- The incidence blocks are chosen with exact size `A`; equal row sums are
  load-bearing because they put the all-ones vector in `col(B)` and improve
  the rank ceiling from `n+1` to `n`.
- `H` need not be positive semidefinite.  The trace-rank inequality used in
  the proof is valid for every real symmetric matrix.
- The square-deficit estimate uses integrality: `0<=delta<=c` implies
  `delta^2<=c delta`.
- The ordinary list counts explanations, and the deficit owner argument is
  applied separately to recover slopes.
- KoalaBear stops because the Gram denominator changes sign.  Mersenne
  stops for the different reason that the still-valid upper bound exceeds
  the budget.
- No denominator failure or budget failure is reported as an unsafe-row
  witness.
- The exact scans use negligible memory and no Modal compute.
