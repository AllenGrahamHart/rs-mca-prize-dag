# dli_odd_phase_budget_ledger_soundness

- **status:** PROVED
- **closure:** proof

## Statement

Suppose a DLI odd-phase ledger covers every tuple

```text
(central profile, nonzero frequency, harmonic, square-root component)
```

used by the DLI odd-evaluation Weyl sums. If the ledger:

- marks every covered phase as not Artin-Schreier-trivial; and
- gives reduced polar-divisor bounds whose harmonic total is `o(t)`;

then `dli_odd_phase_reduced_pole_budget` holds.

## Falsifier

A complete ledger with all phases marked nontrivial and harmonic total `o(t)`
while some required phase is Artin-Schreier-trivial or the true reduced-pole
total exceeds the ledger budget.
