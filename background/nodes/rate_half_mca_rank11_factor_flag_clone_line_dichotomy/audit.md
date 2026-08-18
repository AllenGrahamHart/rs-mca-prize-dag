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
7. The balanced argument packs only active small clone classes. Inactive
   classes have zero incidence, and active classes still form a subpartition
   of the `U` coordinate universe.
8. Residual classes may contribute to several `mu_D` values, but each
   rank-one coordinate triple belongs to exactly one clone class. The proof
   sums weighted triple incidences, not distinct residual classes.
9. The strict alternatives use integer mass: absence of a mass-`L` triple
   means every such triple has mass at most `L-1`.
