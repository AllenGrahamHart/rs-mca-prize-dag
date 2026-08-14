# Audit

1. Normalize by the unknown record count before using `N_min`.
2. Retain both shadow constraints; neither implies the other.
3. Enumerate every piece endpoint and resource intersection exactly.
4. Verify the dual coefficients are nonnegative and dominate every corank.
5. Check both boundary resource equalities and individual-cap slack.
6. Compare unrounded rational values before printing floor/ceiling gaps.
7. Stop at the first reversal `K'=15671`.
