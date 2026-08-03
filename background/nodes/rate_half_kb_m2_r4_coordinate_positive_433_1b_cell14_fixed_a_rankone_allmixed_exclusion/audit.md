# Audit

## Coverage

The aggregate census reconstructs

```text
4 source signs * 4 target lanes * 3 missing roles * 3 matchings = 144
```

and rejects an omitted, duplicate, non-unit, or unresolved row.

## Elimination soundness

- The torus substitution is the exact termwise map (2).
- Cleared torus monomials are valid under `z,f!=0`.
- Every coefficient denominator and route guard is tested at every root.
- Double resultants are necessary conditions only; every degenerate
  specialization is reopened before exclusion.
- A shared projection factor is checked on its original equation fibers and
  then divided exactly before the residual system is tested.
- The weighted substitution `w=z/f^2` is exhaustive because `f!=0`.
- Any zero cut, live field root, guarded witness, or unclassified boundary
  remains unresolved and fails the census.

## Independent checks

The 24-shard replay independently parses every compressed eliminant and
recomputes every `gcd(H,r^p-r)` root set. The census validates 2,992 root
dispositions, 960 common-factor roots, 960 weighted branches, and every
custody digest on Modal. Local verification only streams hashes and reads the
small census artifact.

## Residual risk

This is an exact theorem over the deployed prime and inherits the parent
cell-14 parameterization. It is not a characteristic-uniform theorem and does
not transfer by itself to other role cells or prize rows.
