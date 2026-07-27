# Audit

The primary verifier reconstructs the three candidate profiles, the raw chord
magnitude census, the odd-class supply bound, and the diameter ledger. It also
checks source hashes and DAG wiring.

The independent audit does not import the primary verifier. It repeats the
parity count from the coefficient magnitudes and applies hostile mutations to
the unit supply, profile list, diameter matching, and signed identity.

The proof is characteristic-independent: modulo two is used only for integer
parity of the signed chord products, not arithmetic in the row field.
