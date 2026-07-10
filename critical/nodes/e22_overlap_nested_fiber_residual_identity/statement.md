# e22_overlap_nested_fiber_residual_identity

- **status:** PROVED
- **closure:** proof

## Statement

Let `M_i<M_j` be dyadic quotient scales in the E22 domain, so every
`M_j`-fiber is a disjoint union of `q=M_j/M_i` many `M_i`-fibers.

For a support `R`, recover the canonical scale-`M_i` data

```text
R = B_i disjoint_union U_i,
```

where `U_i` is the union of all full `M_i`-fibers contained in `R` and
`B_i=R\U_i`. Let `S_i` be the selected full `M_i`-fibers. A full `M_j`-fiber
is contained in `R` exactly when all of its `M_i`-children lie in `S_i`.

Consequently the canonical scale-`M_j` tail is

```text
B_j
  = B_i disjoint_union
    {selected M_i-fibers whose M_j-parent is not completely selected},
```

and hence

```text
|B_j| = |B_i| + M_i * r_{i,j}(S_i),
```

where `r_{i,j}(S_i)` is the number of selected `M_i`-fibers whose
`M_j`-parent is not completely selected. Therefore `R` is raw-admissible at
scale `M_j` exactly when

```text
|B_i| + M_i * r_{i,j}(S_i) < M_j.
```

## Falsifier

A coarse `M_j`-fiber fully contained in `R` without all of its `M_i`-children
selected, or a support for which the displayed residual-tail formula for
`|B_j|` fails.
