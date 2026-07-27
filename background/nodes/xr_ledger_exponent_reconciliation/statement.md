# xr_ledger_exponent_reconciliation

- **status:** see dag.json (single source of truth; dag status PROVED) [header retrofit 2026-07-10, catch #69 — was: TARGET]

## Statement

For two size-`(k+t)` supports at exchange distance `s`, the exact pair
codimension is

```text
t+min(s,t).
```

Thus `q^(-min(s,t))` is the conditional cost of the second event, while
`min(s,t-1)` is the anchored/projective ledger convention. This node proves
the dictionary only; it does not prove the slope-resolved de-correlation or
variance estimate sought by `averaged_xr`.

## Replay

Recompute the pair ledger by exact finite-field row reduction at all printed
`(k,t,s)` fixtures.

## Falsifier

the toy ledger matching neither exponent
