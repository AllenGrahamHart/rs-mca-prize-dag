# proof: e22_residual_profile_generating_function

Fix `M_i<M_j`, and write `P=n/M_j` and `q=M_j/M_i`. The `M_j`-parents are
independent for the purpose of choosing selected full `M_i`-fibers.

Inside one `M_j`-parent there are two cases.

If all `q` fine children are selected, the parent is complete and contributes
one factor `u`.

If the parent is incomplete, then exactly `s` of its `q` fine children may be
selected for any `0<=s<q`. There are `binom(q,s)` such choices, and these
selected fine fibers contribute `z^s` to the residual statistic from
`e22_overlap_nested_fiber_residual_identity`, because selected fine fibers in
incomplete parents remain in the scale-`M_j` tail.

Thus one parent contributes

```text
G_q(u,z) = u + sum_{s=0}^{q-1} binom(q,s) z^s,
```

and all `P` parents contribute `G_q(u,z)^P`. The coefficient
`[u^c z^r]` counts exactly the selected fine-fiber subsets with `c` complete
parents and `r` selected fine fibers in incomplete parents. Such a selected
set contains `cq+r` fine fibers, so there are `Pq-cq-r` unselected fine
fibers left.

A canonical scale-`M_i` tail may choose points only inside unselected fine
fibers, and it may not contain a whole unselected fine fiber; otherwise that
fiber would be full in the support and would have been selected. For one
unselected fine fiber, the possible tail intersections have sizes
`0,1,...,M_i-1`, with `binom(M_i,a)` choices of size `a`. Hence the tail
enumerator over the `Pq-cq-r` unselected fine fibers is

```text
H_i(x)^(Pq-cq-r),
H_i(x)=sum_{a=0}^{M_i-1} binom(M_i,a)x^a.
```

Taking `[x^b]` fixes the fine-scale tail size `b`.

The scale-`M_i` admissibility condition is `b<M_i`. The proved node
`e22_overlap_nested_fiber_residual_identity` says that raw scale-`M_j`
admissibility is exactly

```text
b + M_i*r < M_j.
```

Therefore summing the displayed coefficient product over
`0<=b<M_i` and `b+M_i*r<M_j` counts precisely the canonical scale-`M_i`
data that are raw-admissible at `M_j`, before applying the lower-scale
minimality and pricing-multiplicity filters.
