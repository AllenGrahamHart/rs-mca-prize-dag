# Audit

The proof was checked against the following failure modes:

1. The two-top-anchor case includes both boundary layers and uses the worst
   missed allowance `s+2`.
2. With one top anchor, the anchor is charged separately before the sharper
   outside-core cap is applied to the exact first boundary layer.
3. With no top anchor, one intersecting pair of missed sets raises every
   triple intersection from `K-1` to `K`; if no such pair exists, literal
   pairwise disjointness gives the cap `floor(e/(s+1))`.
4. Every synchronized layer has unit slope ownership under `2(s+2)<e`.
5. The primary verifier reconstructs every cumulative cap through `H`; the
   independent audit uses a separately written suffix-minimum calculation.
6. The next support is rejected because its residue is zero, not labeled
   unsafe.

All computation is exact constant-memory integer arithmetic under RAMguard.
