# conditional: dli_odd_phase_reduced_pole_budget

## Predicate nodes

- `dli_odd_phase_budget_ledger_soundness`
- `dli_odd_phase_nontriviality_payload`
- `dli_reduced_pole_harmonic_ledger`

## Claim

Conditional on the nontriviality packet and reduced-pole payload, the actual
DLI odd phases satisfy the reduced-pole budget.

## Proof

The predicate `dli_odd_phase_nontriviality_payload` supplies non-Artin-
Schreier triviality for every central profile, nonzero frequency, harmonic,
and relevant square-root component. That predicate is itself conditional on
the actual polar-obstruction certificates.

The predicate `dli_reduced_pole_harmonic_ledger` supplies reduced
polar-divisor bounds for the same phases, with harmonic total `o(t)`.

The proved node `dli_odd_phase_budget_ledger_soundness` says that complete
coverage by those two payloads proves exactly the reduced-pole budget
statement. Therefore this node follows.
