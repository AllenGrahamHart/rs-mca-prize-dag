# Audit

The quadratic resultant and sign-free cuts are only necessary eliminants.
The finite replay does not trust either elimination: it solves the original missing
quartic and both original q-polynomials, then evaluates the third pair in
both remaining `sigma_o` lanes for every fixed `sigma_c` row.

The independent verifier does not trust stored terminal statuses. It uses a
separate finite-polynomial implementation, recomputes every degree-3864/3868
base-field root union, rebuilds every tower lift from the pinned source
files, and rechecks all 16 final cuts. Duplicate source-sign norms and opposite
first-source-sign rows are reused only after monic normalization proves the
exact polynomial equality or `r -> -r` reflection. Roots are transported by
the corresponding identity or `r -> -r` bijection. `verify_audit.py`
separately enforces the scope, degree ledger, and terminal partition.
