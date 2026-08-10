### 2026-08-10 general-t FPC5 slice dimension

The coordinator-replayed round-24 dimension theorem is now a proved DAG node:
`l1_fpc5_tpetal_saturated_slice_dimension`.

For a labelled `t`-petal pair slice with total support degree `h`, locator
degree `d`, `d<h<=2d+1`, and one saturated anchor, the cross-determinant map

```text
(G,B) -> (FB-GW)/Lambda
```

has an `e`-dimensional target and a one-dimensional kernel, where
`e=2d+1-h`. Hence the pair slice and locator image have dimension `e+1`,
and the monic locator chart is an affine `e`-flat. The proof also shows that
locator projection is injective because `h>d`.

Every nonempty large-source cell surviving `(PF6)` satisfies these hypotheses:
`e=r+1>=1`, while the list threshold gives `h>d`. Thus the old arbitrary-`t`
linearization gap is closed for the complete live fixed-cell frontier. No
critical status changes: a dimension-uniform split-point bound and aggregate
owner/profile payment are still required.
