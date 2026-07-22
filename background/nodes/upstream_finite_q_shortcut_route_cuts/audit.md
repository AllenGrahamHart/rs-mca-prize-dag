# Audit

The import uses the active Grande Finale source, not the archived v2/v3 copy.
Source and Lean table hashes are pinned in `route_cuts.json`.

Two overclaims are explicitly rejected:

1. the printed moment floors do not survive arbitrary first-match pruning
   unchanged; `tau` belongs in the denominator through `(RC1)`;
2. the moving-root theorem is valid on each proved pencil but does not create
   a pencil cover or line-count payment.

The specialized Route-D no-go packages are not imported merely because they
exist. They need an exact current local consumer and row/partition crosswalk
before becoming DAG evidence.
