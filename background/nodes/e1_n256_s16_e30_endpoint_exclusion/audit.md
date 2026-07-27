# Audit

The verifier checks that the exact reduction contains eight distinct profiles,
that each appears in exactly one exclusion group, and that all six required
dependencies are `PROVED`. It also mutates the coverage partition by dropping,
duplicating, and inventing profiles; all three malformed partitions are
rejected.
