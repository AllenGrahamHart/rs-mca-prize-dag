# Proof

The accumulated-locator theorem lifts every local pair produced by a
nongeneric transition to an original degree-below-`K` codeword pair. Its
lifted support has at least `A` coordinates on which both components agree
with `(u,v)`. Hence every lifted pair belongs to `E_A(u,v)`.

Choose the first terminal event for each processed slope. If that event is a
genuine tangent, the exact residual identity at its terminal pair
`c=(c_0,c_1)` is

```text
p_z=c_0+zc_1.                                          (1)
```

Apply the true-tangent coordinate injection with the discrepancy support of
`c`. This support has size at most `n-A`, so at most `n-A` retained slopes can
be tangent-owned by the fixed pair `c`.

The initial pair cannot own a retained mismatch slope at a later stage. If
`(1)` held for that pair, its initial mismatch polynomial would already be
zero and the slope would have entered the root tangent branch instead of the
nonzero-mismatch descent. Therefore all pairs owning slopes in `Z_tan` are
among at most `E-1` nonroot members of `E_A(u,v)`.

Assigning each slope only to its first terminal pair and deduplicating equal
lifted pairs now gives

```text
|Z_tan|<=sum_(nonroot c in E_A(u,v))(n-A)
       <=(n-A)max(E-1,0),
```

which proves `(GEO2)`. Notice that neither branch depth nor the number of
locator flags appears in this sum.

The set `E_A(u,v)` is exactly the common-support list of the two-fold
interleaved code at received word `(u,v)`. Its size is at most the worst
two-fold list size. The sub-square-root interleaving theorem applied to the
ordinary worst list `L_A` proves `(GEO4)`, and under `L_A^2<q` it identifies
the worst interleaved list with `L_A`. Substitution in `(GEO2)` proves
`(GEO5)`.

Finally, `(GEO6)` makes the right side of `(GEO5)` at most `16n^3`. If
`L_A<=n^2+1`, it is at most `(n-A)n^2<n^3`, since `A>0`. QED.
