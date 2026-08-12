# Audit

The primary checker reconstructs every listed explanation from all 120
seven-subsets, proves uniqueness, verifies exact maximal supports, checks
same-support noncontainment, recomputes both cores, and rejects global
affinity.

The independent checker instead enumerates all `11^5=161051` codewords for
each listed slope and reconstructs the pair interpolants with modular
Gaussian elimination. It does not reuse the primary support-first search.

Both checkers fail closed under mutations of the received line,
coefficients, support, core, and record membership.
