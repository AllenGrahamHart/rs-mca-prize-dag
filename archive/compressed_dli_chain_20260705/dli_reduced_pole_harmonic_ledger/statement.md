# dli_reduced_pole_harmonic_ledger

- **status:** CONDITIONAL
- **closure:** proof

## Statement

For every actual DLI odd-evaluation phase after Artin-Schreier reduction,
provide reduced polar-divisor bounds whose sum over all central profiles,
nonzero frequencies, DLI harmonics, and square-root components is `o(t)`.

This is reduced to:

- `dli_reduced_pole_majorant_table_soundness`, which proves that a complete
  certified majorant table implies the reduced-pole harmonic ledger; and
- `dli_reduced_pole_majorant_table_payload`, which remains to construct the
  actual DLI reduced-pole majorant table and prove its harmonic total is
  `o(t)`.

## Falsifier

A phase or harmonic range whose reduced polar-divisor contribution makes the
total conductor budget non-negligible.
