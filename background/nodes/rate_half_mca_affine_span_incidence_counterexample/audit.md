# Audit

The primary verifier constructs the line, enumerates every selected maximal
agreement support, checks pair noncontainment, recomputes affine rank and
direction separation, and evaluates all three violated bounds.

The independent verifier uses a separately written constructor and checks
all 100 domain coordinates for every selected slope.  It enumerates all
1,009 constant direction codewords when recomputing the separation maximum.

The counterexample is exact and small.  No Modal or probabilistic search is
used.  The construction also explains the proof gap: local full rank does
not control proper-subspace multiplicity among incident normals.
