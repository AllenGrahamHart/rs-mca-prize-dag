# Cycle 217: upstream MCA affine-incidence correction (2026-08-13)

Cycle 216's exact counterexample was reconstructed on current upstream
`main@93fba1be` and exported as draft PR `#1165` at commit `809c8e31`.
The upstream manuscript now states the counterexample in place of the false
theorem and retracts the dependent KoalaBear and Mersenne-31 payments.

Two independently structured standard-library verifiers reconstruct all 31
selected supports.  The second implementation independently chooses legal
coordinates and exhaustively scans all 1009 constant direction codewords.
The manuscript compiles successfully in an isolated output directory.

Open-PR reconciliation found a new stacked PR `#1164`.  Both `#1163` and
`#1164` were given dependency alerts.  Their fixed-core
codeword-affine-span staircase inherits the refuted denominator.  The
selector-free all-LineRay error-affine-core payment in `#1164` is distinct:
its zero-mask/Bollobas set-pair proof does not use the failed incidence step
and remains bankable at its printed scope.

```text
start:                   27be48115
canonical prize:         c8d48cd4b
upstream main:           93fba1be
relevant upstream PRs:   #1163, #1164, #1165
result:                  EXPORTED exact counterexample and correction
DAG delta:               none; Cycle 216 already repaired dependencies
upstream terminal delta: false affine-span MCA compiler publicly retracted;
                         dependent fixed-core payments flagged
delta-star movement:     none
compute:                 exact local arithmetic under RAMguard; no Modal
next route action:       seek a true proper-subspace occupancy or alternate
                         whole-line compiler for the repaired MCA target
```
