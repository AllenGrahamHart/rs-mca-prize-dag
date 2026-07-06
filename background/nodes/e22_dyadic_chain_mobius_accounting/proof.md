# proof: e22_dyadic_chain_mobius_accounting

By `e22_minimal_scale_partition`, every support class with at least one
admissible dyadic scale has a unique minimal admissible scale. Therefore the
classes counted by the raw scale-`M_j` summand split disjointly according to
their minimal scale:

```text
{R counted at M_j}
  = disjoint union over i<=j of {R counted at M_j and m(R)=M_i}.
```

There are no terms with `i>j`: if a class is counted at `M_j`, then `M_j` is
an admissible scale for that class, so its minimal admissible scale is at most
`M_j`.

The `i=j` part of the disjoint union is exactly the selected minimal-scale
cell at `M_j`, whose size is `N_j`. For `i<j`, the corresponding part is
precisely the cross-scale overlap `O_{i,j}`: classes whose selected minimal
scale is `M_i` but which are also counted by the raw scale-`M_j` summand.
Counting the disjoint union with the declared multiplicity convention gives

```text
A_j = N_j + sum_{i<j} O_{i,j}.
```

Rearranging gives

```text
N_j = A_j - sum_{i<j} O_{i,j}.
```

This is a formal triangular accounting identity on the dyadic scale chain.
It does not compute the overlaps; that remains the arithmetic target
`e22_minimal_scale_overlap_counts`.
