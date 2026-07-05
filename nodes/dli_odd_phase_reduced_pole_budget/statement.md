# dli_odd_phase_reduced_pole_budget

- **status:** CONDITIONAL
- **closure:** proof

## Statement

For every central profile, nonzero frequency, and DLI harmonic, the actual
odd-evaluation phase

```text
P_lambda(sigma(y))
```

on each relevant square-root component is not of Artin-Schreier-trivial form
`g^p-g+c`, and its Artin-Schreier-reduced polar divisor has harmonic total
`o(t)`.

This is reduced to:

- `dli_odd_phase_budget_ledger_soundness`, which proves coverage and harmonic
  summation soundness;
- `dli_odd_phase_nontriviality_payload`, which reduces Artin-Schreier
  nontriviality to the actual polar-obstruction payload; and
- `dli_reduced_pole_harmonic_ledger`, which reduces the reduced-pole harmonic
  total to the actual majorant-table payload.

## Falsifier

An actual central-profile component where the phase is `g^p-g+c`, or where
the reduced polar-divisor harmonic total exceeds the DLI budget.
