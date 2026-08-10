# Proof

The five product rows have six columns. Deleting one column at a time gives
six signed `5 x 5` determinants, whose vector lies in the matrix kernel by
Laplace expansion. The compiler constructs all six determinants for each of
the fifteen role cells and the two repeated-BC signs.

Each determinant is made primitive and repeatedly divided only when exact
division succeeds by a source-label difference or one of
`r,t,b,c,b+-1,c+-1,b+-c`. All thirty cases complete. In cells 3 and 6,
columns 1 and 4 have no residual polynomial after these divisions, so each
corresponding raw determinant is a nonzero scalar times a product of guards.
It cannot vanish on the guarded open set. Thus rank is at least five, and as
there are five rows it is exactly five. QED.
