# proof: e22_overlap_nested_fiber_residual_identity

Fix nested dyadic scales `M_i<M_j`. The quotient fibers form nested
partitions: every coarse `M_j`-fiber is the disjoint union of `M_j/M_i` fine
`M_i`-fibers.

For a support `R`, let `S_i` be the set of fine `M_i`-fibers fully contained
in `R`, let `U_i` be their union, and let `B_i=R\U_i`. This is the canonical
full-fiber recovery from `e22_cross_scale_support_canonical_form`.

Consider a coarse `M_j`-fiber `C`. If every fine child of `C` lies in `S_i`,
then all points of `C` lie in `U_i`, so `C` is fully contained in `R`.

Conversely suppose `C` is fully contained in `R`. Every fine child `F` of `C`
is then also fully contained in `R`. By the definition of `S_i`, each such
`F` belongs to `S_i`. Thus a coarse fiber is full in `R` exactly when all of
its fine children are selected.

The canonical scale-`M_j` full-fiber part is therefore the union of precisely
those coarse parents whose fine children are all selected. Removing these
coarse parents from `R` leaves two disjoint pieces:

1. the original fine-scale tail `B_i`; and
2. the selected fine `M_i`-fibers whose coarse parent was not completely
   selected.

The pieces are disjoint because `B_i` was defined after removing all selected
fine fibers. Hence, if `r_{i,j}(S_i)` denotes the number of selected fine
fibers in incomplete coarse parents,

```text
|B_j| = |B_i| + M_i * r_{i,j}(S_i).
```

By `e22_cross_scale_support_canonical_form`, raw scale-`M_j` admissibility is
equivalent to `|B_j|<M_j`. Substituting the formula above gives exactly

```text
|B_i| + M_i * r_{i,j}(S_i) < M_j.
```

This proves the nested-fiber residual identity.
