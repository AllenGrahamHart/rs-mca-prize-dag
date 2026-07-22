# Proof

For a printed planted polynomial `f_j`, the receiver equals `f_j` on the
`k-1` core points and on petal `j`, which has `sigma+1` points. These sets are
disjoint, so `f_j` has at least `k+sigma` agreements and lies in `L(U)`.
Taking distinct polynomials removes scalar-label duplicates, hence
`P(U) subset L(U)` with exact size `p(U)`.

The sets `P(U)` and `R(U)=L(U)\P(U)` are disjoint and cover `L(U)`. The
first-match partition adapter gives the same conclusion by taking one paid
predicate, "is a printed plant", and one residual catch-all. Cardinalities
therefore satisfy

```text
|L(U)|=p(U)+N_nonplant(U).
```

Subtracting `p(U)` from `|L(U)|<=B*` proves the displayed equivalence when
`p(U)<=B*`. If `p(U)>B*`, the planted subset alone proves `|L(U)|>B*`.

Now refine `R(U)` into any finite ordered family of structural paid classes
and a final residual. Sound upper bounds on those pieces may be summed to
prove the same `N_nonplant` inequality, but the equality above does not require
the refinement. Conversely, asking directly for an upper bound on
`N_nonplant` does not require proving separate formulas for those pieces. This
establishes the minimal sufficient ledger.

Lemma A remains useful structure: on max-fill cells it shows every member of
`R(U)` touches at least two petals. It is not needed for the two-class identity
and therefore cannot create a hidden scope assumption in this reduction.
