# Audit

The primary verifier rebuilds the degree-six remainder determinant, the
quintic pair curve, its conic normalization, the degree-15 quotient, all
factor identities, and the challenge-field parity argument. It compares the
result with a hash-bound certificate and rejects hostile mutations.

The independent verifier uses only `fractions.Fraction` and a separate
polynomial/rational-function implementation. It reconstructs the quadratic
remainders after substituting the printed `y(u),z(u)`, verifies the quotient
by cross multiplication, checks the three branch factorizations and their
coprimality, and replays the field descent.
