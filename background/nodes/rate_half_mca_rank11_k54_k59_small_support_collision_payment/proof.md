# Proof

Fix `K'` in `54..60`, put `q=K'-10`, and retain the baseline incidence
caps, all core-offset rank-nine marks, every kernel corank, the complete
55-shadow deficit ledger, and sharp isolated demand.

For each `c=2,3,4,5`, the exact maximum defect `s_c` ranges over `0..q`.
Intersect the inherited source and cross-support caps with the proved
same-source collision cap.  If `s_4+s_5<q`, also intersect support four
with the joint external-carrier cap.  No joint cap is used otherwise.

Group supports as

```text
(2,3),       (4,5),       (6,7,8,9).
```

The first two groups contain `(q+1)^2` raw choices each.  The last group
contains `5*4*3*2=120` terminal/fallback choices.  Within each group,
identify duplicate cap vectors and discard a vector only when another is
componentwise at least as large.  Nonnegative deficit weights and later cap
intersections make this Pareto compression exact.  On each row, the three
frontiers have respectively `1,1,7` vectors.

Exhausting their Cartesian product gives the active branch

```text
s_2=s_3=s_4=s_5=floor(q/2),       c6F/c7F/c8F/c9F.       (1)
```

For each row, combine the resulting premium `P` with unchanged rank-nine
marks `G` and the record floor `R` as

```text
full-rank capacity=floor((G+R P)/55).
```

Adding all kernel-corank capacities and comparing with

```text
R C(m,11)-C(n,11)
```

gives positive gaps on `54..59`; the minimum is the printed `K'=59` gap.
The cleared record coefficient and floor-record cross are positive on all
six rows, so the contradiction persists above the record floor.

At `K'=60`, the same exact computation again selects `(1)`, now with all
four defects equal to `25`.  Its premium exceeds the exact safe ceiling,
and complete capacity exceeds demand by the printed amount.  QED.
