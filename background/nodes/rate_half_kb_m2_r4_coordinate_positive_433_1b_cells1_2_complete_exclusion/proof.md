# Proof

The product-rank-drop complete-exclusion theorem removes both cells whenever
the five product rows have rank at most four.  Otherwise their rank is five,
so one of the six maximal cofactors is nonzero.

The generated chart census is the full Cartesian product of cells `1,2`,
the four source-root sign pairs, and the six maximal-cofactor charts.  The
role metadata in every row agrees with `(KBP1B12-1)`.  Each chart ideal
contains all six stripped common minors and an inverse equation for the
common guard times its selected cofactor.  Thus every guarded principal
common packet would give a zero of at least one chart ideal.

Singular returns the unit ideal in all 48 cases, with no timeout or fallback.
Therefore no principal common packet exists in either cell.  Combining the
principal and rank-drop branches proves complete exclusion. QED.
