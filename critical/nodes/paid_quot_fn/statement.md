# paid_quot_fn

- **status:** see dag.json (single source of truth; dag status PROVED)
- **statement provenance:** written 2026-07-27 (empty-statement remediation / sketch-tagged re-grade);
  see notes/wave24_integration_20260727/STATEMENT_REMEDIATION.md and SKETCH_TAGGED_REGRADE.md

## Statement

THE QUOTIENT PAID COLUMN IS INTERVAL-VALUED, NOT POINT-VALUED. Partitioning the quotient column into zones (a), (b), (c): `qfloor_exact` supplies the exact floor rule above the norm threshold and `acl_count` the characteristic-zero aligned-class count, making zones above the threshold point-valued computable counts. Zone (b) — the value-set collision question — is NOT closed in this DAG. Accordingly this node proves only Paid_quot(A) in [lower_quot(A), upper_quot(A)], where the lower endpoint is the certified exact-floor/ACL count and the upper endpoint is the recorded collision-safe envelope for the unresolved zone. This interval object is exactly what `paid_closure` and the downstream `zone_b` branch consume. NONCLAIM: no point-valued zone-(b) conclusion. [statement written 2026-07-27 from this node's own proof.md]
