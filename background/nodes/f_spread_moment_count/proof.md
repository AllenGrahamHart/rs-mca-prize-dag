# f_spread_moment_count proof

Assume the dual distance `w*(P-perp)` is greater than `r`. By
`f_dual_distance_frame`, every `r`-subset of traces is independent. Therefore
an `r`-subset of domain points can be the root set of at most one locator in
the flat `P`; otherwise two distinct flat points would meet on those `r`
independent trace conditions.

For each locator `ell in P cap D_j`, let `mult(ell)` be its number of roots in
the domain. Count pairs

```text
(ell, T)
```

where `ell in P cap D_j` and `T` is an `r`-subset of roots of `ell`. The
independence condition injects these pairs into the set of all `r`-subsets of
the `n` domain points, so

```text
sum_{ell in P cap D_j} binom(mult(ell), r) <= binom(n,r).
```

Every member of `D_j` has `mult(ell) >= j` under the support convention used
by this node, hence

```text
#(P cap D_j) binom(j,r) <= binom(n,r).
```

Thus

```text
#(P cap D_j) <= binom(n,r) / binom(j,r).
```

For fixed or logarithmic `r`, this is polynomial in `n`. The proof does not
claim a useful bound when `r` grows linearly; that regime is deliberately
routed to descent/structure nodes.
