# Audit

- The parent reduction proves that exactly three profiles survive at `V=64`.
- DAG requirement edges include the parent and exactly the three corresponding
  profile exclusions.
- The `(0,8)` exclusion is an empty exact census; `(3,5,1)` is below the exact
  cubic threshold; `(4,7)` is below the row prime by exact norm census.
- Source hashes pin all four statements used by the synthesis.
- Primary and independent endpoint verifiers reject an omitted profile,
  downgraded dependency, stale `V<=64` frontier, or non-green child.

This synthesis performs no computation beyond lightweight packet and DAG
checks.
