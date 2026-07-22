# Audit

- The rank-three bound uses the pair-Lagrange fiber identities, not only the
  external incidence counts.
- The matrix rank is exactly the pair-locator span dimension because
  quadratic evaluation on more than two distinct active rows is injective;
  the Mobius dichotomy supplies the exact rank-two/rank-three split.
- Every row and column scaling in the proof is explicitly nonzero on the
  external chart.
- The quotient-space statement is equivalent to the evaluation statement
  because `I` is squarefree and split at the distinct internal slopes.
- The verifier replays the inverse-locator rank at `e=3,4,5` directly from
  the pair-Lagrange fiber ratios.
- Its negative control is a 27-block, 12-slope, simple `e=4` design with the
  exact `(row degree,column degree)=(4,9)` ledger. Its complement polynomials
  have full rank nine, above `e+4=8`, and every four-point residue evaluation
  has rank four. This guards against silently deriving either gate from
  biregularity alone.
