# Audit

The main risk is a false sign elimination: `K(y)=C(z)C(-z)` is necessary
but not sufficient for the chosen `z`. The finite replay therefore solves
and intersects the original quartics in `z`; it never accepts a root from
the sign-free norm alone.

The independent verifier does not trust stored terminal statuses. It uses a
different finite polynomial implementation, recomputes every base-field
root union, rebuilds all tower lifts from the pinned source files, and
rechecks both q quartics. `verify_audit.py` separately enforces the scope,
terminal partition, and zero-common-q ledger.
