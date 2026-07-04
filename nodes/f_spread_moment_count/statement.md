# f_spread_moment_count

- **status:** PROVED
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s3b_iii_3_fibers_and_noanchor.md#1']

## Statement

If w*(P-perp) > r: every r-subset of traces meets in exactly one point, so sum of C(mult, r) <= C(n,r), giving #(P cap D_j) <= C(n,r)/C(j,r) ~ (n/j)^r. HONEST SCOPE: poly(n) only for r = O(log n); in-band deficiencies r ~ n 2^-9 exceed this — high dimension MUST route through descent/structure, not moments.

## Ledger (migrated notes)

PROVED 2026-07-04 by the injective r-subset incidence count; scope remains fixed/small r.
