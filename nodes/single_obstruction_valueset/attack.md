# ATTACK — single_obstruction_valueset (medium; character-sum proof)
Claim: for h>20 at official-shape rows, the first obstruction O_{h-1} on
anchored cores takes >= C(n,h)/budget distinct values (small fibers). The scan
(notes/modal_single_obstruction...py) DE-RISKS (evidence, cannot close; uses
calibration primes). The PROOF (per attack surface) is via CHARACTER SUMS or
the norm structure: O_{h-1} is a symmetric-function map; its fibers are small
iff the associated exponential sum has cancellation. This is a sibling of DLI
(equidistribution of a low-degree map) — the same Weil/norm machinery. Try:
bound the fiber size by a character-sum estimate over anchored cores; small
fibers <=> value-set nearly full. If heavy collisions appear at a calibration
row (scan), the lemma is falsified -> fall back to per-h certificates.
