# Audit

The nested sign-free cuts are only necessary eliminants. The finite replay
does not trust either sign elimination: it solves the original missing
quartic and both original q-polynomials, then evaluates the third pair in
both remaining `sigma_o` lanes for every fixed `sigma_c` row.

The independent verifier does not trust stored terminal statuses. It uses a
separate finite-polynomial implementation, recomputes every degree-5058
base-field root union, rebuilds every tower lift from the pinned source
files, and rechecks all 64 final cuts. Duplicate `sigma_c` norms and opposite
first-source-sign rows are reused only after monic normalization proves the
exact polynomial equality or `r -> -r` reflection. Roots are transported by
the corresponding identity or `r -> -r` bijection. `verify_audit.py`
separately enforces the scope, degree ledger, and terminal partition.
