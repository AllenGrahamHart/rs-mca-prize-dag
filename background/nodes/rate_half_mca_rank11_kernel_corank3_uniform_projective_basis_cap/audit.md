# Audit

The primary verifier recomputes the recurrence floor by residue-class sums,
checks its small-grid recurrence identity, and scans all `1048567` official
shortening rows with exact integers.  The independent audit uses direct
recurrence unfolding on a finite grid and separately checks the pinned Modal
result and official endpoint divisions.

The Modal run used one 512 MB container with a 60-second limit.  It is an
exact finite corroboration, not a heuristic random search.
