# Audit

The primary and audit share only the printed sparse checkpoints and deployed
prime. The audit does not import the primary reconstruction helper:

1. It solves the source interpolation fraction-free and verifies the matrix
   identity before reconstructing all four primitive cores.
2. It independently derives both ratio gates, checks the complete minus-gate
   factor census, and reverse-checks reciprocity and irreducibility of the
   plus gate.
3. It rebuilds the degree-352 and degree-772 candidate products from their
   complete irreducible factor ledgers.
4. It checks all 13 generic and 11 boundary fiber records, including the
   `d^2+1` pair whose quartic `b` fibers are entirely forbidden.

The degree-six minus-branch shard eliminates `b` by the reciprocal
quadratic before saturation. This is equivalent to the source system on
that branch and avoids a redundant three-variable Groebner calculation.

The FLINT projection scripts are deterministic over the base prime
`F_2130706433`; the target field is its degree-six extension. Their inputs,
outputs, helper hashes, and all intermediate exact equation caches are
pinned by `verify_runner.py`.
