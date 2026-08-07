# Audit

- Every dependency is `PROVED` and explicitly contains `F07-R02` in its
  literal scope.
- The cell is not inferred from the old `F04/F07` fingerprint equality.
- Companion inversion is intentionally deferred to a downstream composition
  so this direct closure remains independently auditable.
