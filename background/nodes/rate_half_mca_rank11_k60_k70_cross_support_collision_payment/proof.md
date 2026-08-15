# Proof

Fix `K'` in `60..71`, put `q=K'-10`, and retain the baseline incidence
caps, all core-offset rank-nine marks, every kernel corank, the complete
55-shadow deficit ledger, and sharp isolated demand.

For each source `c=2,3,4,5`, the exact maximum defect `s_c` ranges over
`0..q`.  Intersect every inherited source, same-support, and cross-support
cap.  The cross-support collision cap is used only for `s_c<q` and targets
`d` satisfying `c+d<=11`.  If `s_4+s_5<q`, also intersect support four with
the joint external-carrier cap.  Retain every support-`6..9`
terminal/fallback branch.

Group supports as

```text
(2,3),       (4,5),       (6,7,8,9).
```

Within each group, identify duplicate cap vectors and discard a vector only
when another is componentwise at least as large.  Nonnegative deficit
weights and later cap intersections make this Pareto compression exact.
Exhausting the three frontiers gives the active branch

```text
s_2=s_3=s_4=s_5=ceil(q/2),       c6F/c7F/c8F/c9F.       (1)
```

For each row, combine the resulting premium `P` with unchanged rank-nine
marks `G` and the residual record floor `R` as

```text
full-rank capacity=floor((G+R P)/55).
```

Adding every kernel-corank capacity and comparing with

```text
R C(m,11)-C(n,11)
```

gives positive gaps on `60..70`; the minimum is the printed `K'=70` gap.
The cleared record coefficient and floor-record cross are positive on all
eleven rows, so the contradiction persists above the record floor.

At `K'=71`, the same exact computation again selects `(1)`, now with all
four defects equal to `31`.  Its premium exceeds the exact safe ceiling and
complete capacity exceeds demand by the printed amount.  QED.
