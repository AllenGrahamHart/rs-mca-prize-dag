# Audit

The primary verifier exhausts all 341,376 heavy-position triples in
`Z/128Z`, checks the diameter/equal-length split, and independently evaluates
the quarter-template sign formulas. It also checks the singleton-class
magnitude obstruction, source hashes, and DAG wiring.

The independent audit reconstructs the four cases algebraically without
importing the primary verifier. Hostile mutations allow a second light chord,
retain the missing quarter, and drop the profile cap; each mutation defeats a
load-bearing conclusion.

The finite triple census verifies only elementary cyclic geometry. The proof
does not depend on the census for truth.
