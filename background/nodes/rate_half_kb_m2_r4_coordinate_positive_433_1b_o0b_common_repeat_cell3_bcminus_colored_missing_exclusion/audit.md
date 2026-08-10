# Audit

`verify.py` does not trust the printed root lists.  It recomputes the
base-field part of every unique norm and guard polynomial as
`gcd(P,q^p-q)`, compares it with the product of all listed linear factors,
rebuilds all 136 incidences and eight union values, and directly replays the
complete genus-two `y` fibers and boundary guards.  `verify_audit.py`
injects omitted roots, false statuses, altered coordinates, a dropped
ledger row, and a fake survivor.
