# dli_reduced_pole_majorant_table_soundness

- **status:** PROVED
- **closure:** proof

## Statement

If a table covers every central profile, nonzero frequency, DLI harmonic, and
square-root component; gives a certified upper bound for the
Artin-Schreier-reduced polar divisor of each covered phase; and proves that
the sum of those majorants over the DLI harmonic ranges is `o(t)`, then
`dli_reduced_pole_harmonic_ledger` holds.

## Falsifier

A complete certified majorant table with total `o(t)` while the actual
reduced-pole harmonic ledger fails.
