# Audit

## Coverage

The aggregate checker reconstructs the Cartesian product

```text
4 source signs * 4 target lanes * 3 missing roles * 9 matchings = 432
```

and rejects duplicates, omissions, a wrong matching index, or a non-unit row.

## Elimination soundness

- The torus substitution is the termwise ring map (4), not a sampled identity.
- Common `z` factors are removed only under the target guard `z!=0`.
- Every cleared coefficient denominator is tested at every eliminant root.
- Direct fibers use the original reduced equation pairs, not only resultants.
- Roots with `a=0`, `z=0`, or `f=0` are recorded as target boundaries.
- A zero univariate specialization falls back to the stored inner resultant;
  a doubly zero outer cut would remain unresolved and fail the ledger.

## Independent checks

The replay script independently parses every compressed eliminant and
recomputes all `gcd(H,r^p-r)` root sets. The local census checker validates
all 9,456 root dispositions and all 8,736 direct fibers under the 256 MiB
RAMguard profile.

## Residual risk

This is a deployed-field finite theorem inherited from the exact cell-14
parent parameterization. It is not a characteristic-uniform theorem. The
three all-mixed matching indices are outside its claim.
