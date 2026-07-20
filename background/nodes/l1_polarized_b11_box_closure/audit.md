# Audit - L1 polarized B11 box closure

## Checked axes

1. The `ell<=P` branch is retained, so there is no hidden asymptotic
   exception in the gate statement.
2. With `ell>P`, absence of a dense petal contradicts `h>=ell`; it is not
   excluded merely by terminology.
3. If two petals are dense, they are necessarily the two largest supports,
   so their deficits are the B11 `v_(1),v_(2)`.
4. In the one-dense branch, the threshold controls `r`, while the per-petal
   cap `d>=ell-v` is load-bearing in the final `G_R` inequality.
5. `p` includes dense deficits and sparse support sizes exactly once.
6. The conclusion fixes `P,E`; it does not sum a growing sequence of boxes.

## Remaining attack

Count or own the union of growing polarized entropy and growing cofactor
excess, still under the source-coupled reserve rich-fiber condition.
