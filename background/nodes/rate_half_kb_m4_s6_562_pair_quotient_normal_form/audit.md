# Audit

The primary verifier rebuilds the degree-six pair determinant, adjoint
resultant factor degrees, rational normalization, branch factorizations, and
field descent, then compares them with a hash-bound certificate and hostile
mutations.

The independent verifier uses a separate `Fraction` polynomial and
rational-function implementation. It checks the printed parameter lies on the
pair curve, reconstructs both remainder ratios, verifies the branch factors
and coprimality, and replays the challenge-field argument.
