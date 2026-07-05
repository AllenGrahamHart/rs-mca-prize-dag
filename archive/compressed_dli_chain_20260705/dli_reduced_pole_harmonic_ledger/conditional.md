# conditional: dli_reduced_pole_harmonic_ledger

## Predicate nodes

- `dli_reduced_pole_majorant_table_soundness`
- `dli_reduced_pole_majorant_table_payload`

## Claim

Conditional on the actual reduced-pole majorant table payload, the DLI
reduced-pole harmonic ledger holds.

## Proof

The predicate `dli_reduced_pole_majorant_table_payload` supplies a table
covering every central profile, nonzero frequency, DLI harmonic, and relevant
square-root component. Each table entry is a certified upper bound for the
Artin-Schreier-reduced polar divisor of the actual phase

```text
P_lambda(sigma(y)).
```

The same payload proves that the sum of those majorants over the DLI harmonic
ranges and components is `o(t)`.

The proved predicate `dli_reduced_pole_majorant_table_soundness` says that a
complete table with certified domination and `o(t)` total implies exactly the
reduced-pole harmonic ledger. Therefore this node follows.
