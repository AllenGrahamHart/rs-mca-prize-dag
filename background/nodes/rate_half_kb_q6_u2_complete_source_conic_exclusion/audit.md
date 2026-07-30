# Audit

- The divisor proof includes infinity by using binary forms.
- Nonzero source rows and `H(T,x)` are forced by irreducibility; no hidden
  vertical or horizontal component is permitted.
- The degree comparison is exact: `12*4=48=2*24`, so aggregate equality
  really forces every local inequality to saturate.
- All rows `r=0,1,2` are replayed independently by `verify.py` and
  `verify_audit.py`.
- The source PR's Python/Sage certificates and canonical payload are pinned,
  but the local proof does not infer a ledger payment from them.
