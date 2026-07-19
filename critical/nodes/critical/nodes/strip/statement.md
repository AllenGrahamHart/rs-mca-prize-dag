# strip

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s3b_ii_strip_periodic.md']

## Statement

The strip-periodic decomposition used by `mca_safe` is exact up to the named
GAP-1 residual.  Rate-preserving periodic strata are removed and counted by the
quotient recursion; the remaining `K_M`-stable escape mass is either
equivariant/quotient-recursive or non-equivariant multi-isotypic.  The latter
contributes at most `poly(n) * FM` once `gap1_noneq_mass` holds.  The GAP-2 seam
between the line-side strip and support-side quotient recursion is classified by
`gap2_seam`, so no periodic bucket is double-counted or silently omitted.

Equivalently, after the strip, the periodic contribution consumed by `mca_safe`
is

```text
rate-preserving quotient columns + O(poly(n) * FM)
```

with all non-rate-preserving seam buckets left on the aperiodic side and carrying
no quotient-recursion boost.

## Ledger (migrated notes)

combinatorics PROVED; completeness rests on GAP-1 pricing
