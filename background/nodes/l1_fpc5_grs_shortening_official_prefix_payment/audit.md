# Audit

## Exactness

- `(PF6)` is recomputed from integer endpoints rather than imported from a
  sampled table.
- Every shortening denominator and every floor is integer-exact.
- Defects are summed inside a fixed `(M,t)` group before the single planted
  anchor charge `M`; touched groups and scales are then union-bounded.
- The field test uses `floor(q/2^128)` and the strict cap
  `q<=2^256-1`.

## Negative controls

The replay deliberately checks four blocked scales. Failure of this cap is
recorded only as a route fence and is not interpreted as a lower bound or a
counterexample to the target.

## Residual risk

The theorem is specific to `n=8192`. Later rows require their own exact
aggregation or a symbolic uniform argument.
