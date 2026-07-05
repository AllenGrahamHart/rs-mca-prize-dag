# ATTACK - dli_reduced_pole_majorant_table_payload

This is now an assembly node. The live DLI reduced-pole leaf is
`dli_reduced_phase_manifest_payload`.

Needed output at the reduced-phase manifest:

- enumerate the DLI tuple set: central profiles, nonzero frequencies,
  harmonics, and square-root components;
- for each row or row class, compute the Artin-Schreier-reduced local polar
  divisor of `P_lambda(sigma(y))`;
- record a majorant for that reduced polar divisor, including any row
  multiplicity or component multiplicity;
- prove the table covers every DLI tuple exactly once or with declared
  disjoint row classes; and
- prove the total majorant over the DLI harmonic ranges is `o(t)`, while
  recording the prime-to-`p` pole witness for the same tuple.

The formal rule converting such a table into the old reduced-pole ledger is
proved in `dli_reduced_pole_majorant_table_soundness`.
