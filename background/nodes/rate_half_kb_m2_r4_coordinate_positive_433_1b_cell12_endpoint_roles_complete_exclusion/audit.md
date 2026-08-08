# Audit

Run `verify.py` and `verify_audit.py` in this directory.  The first verifies
immutable custody and complete Cartesian coverage.  The second independently
replays every source compatibility identity and target-lane index, compares
the two result ledgers, and includes hostile completeness mutations.
