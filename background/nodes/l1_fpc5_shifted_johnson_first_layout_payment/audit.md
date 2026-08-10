# Audit

The audit checked the composition points most likely to be overcounted or
silently dropped:

1. selected contributors are reclassified in the canonical first layout;
2. later source layouts contribute only first-layout anchors;
3. touched subsets and exact defects are disjoint reconstructed cells;
4. `binom(M,t)` and `binom(b,u)` are both retained;
5. the `M` anchor remainder is added once for a union of defects;
6. the rate-`1/16` failure test is performed after touched-set aggregation,
   not at fixed-cell level.

The primary verifier solves the exact integer threshold by monotone binary
search. The independent audit checks the rounded powers and the six cap
failures directly from adjacent integer ceilings.
