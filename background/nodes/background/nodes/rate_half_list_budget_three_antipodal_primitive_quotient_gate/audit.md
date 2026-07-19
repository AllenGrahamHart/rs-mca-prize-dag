# Audit

The degree argument uses the reduced map: pairwise coprimality of the `G_i`
is what proves `gcd(R,S)=1`. Without that step, cancellation could invalidate
the quotient-degree obstruction.

The coset argument is stronger than checking one preferred deleted root.
For every choice of one deleted root in each of the four cosets, the first
four geometric-series coefficients have nonzero Vandermonde determinant.

The exact `d=16` replay over `F_97` checks all `4^4=256` such deletion
choices. Every coefficient matrix has rank four. This is a posedness audit;
the general proof is the symbolic Vandermonde argument.

Primitive and nonperiodic are conclusions about this residual only. They do
not assert that the residual is empty.
