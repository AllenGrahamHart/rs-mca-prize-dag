# xr_ledger_exponent_reconciliation

- **status:** TARGET

## Statement

Reconcile averaged_xr's stated shell exponent q^{-min(s,t)} with the proved ledger's c(s,t) = min(s,t-1): determine the correct exponent per shell, propagate through the second-moment sum, and confirm the consumer margins absorb the difference (a full q factor at shells s >= t). Small: the qx13 ledger tables decide it at toy scale.

## Attack surface

recompute the toy pair-ledger at both exponents vs the exact counts

## Falsifier

the toy ledger matching neither exponent
