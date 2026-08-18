# Audit

1. Triple incidences are weighted by first-owned slope mass; repeated use of
   one class across many triples is intentional and counted on both sides.
2. A rank-three triple has one two-dimensional common kernel in `B`, so its
   complete aggregate mass is capped once by `R_4`.
3. Clone classes partition only nonzero evaluation columns. Base-freeness of
   `B` removes zero columns from the universe.
4. The per-clone mass cap is `R_8`; it is not multiplied by the number of
   residual classes inside that clone.
5. Convex packing uses a partition with total size at most `U`; filling the
   largest allowed classes gives the conservative maximum.
6. Rank at most two is split disjointly into rank one and rank exactly two.
