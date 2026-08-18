# Cycle 509: dimension-three pair-overlap moment floor

## Result: PROVED lower endpoint

After complete common-core shortening, the 520 residual pair cores have size
`67470+K'` in `1048576+K'` coordinates. Distinct cores intersect in at most
`K'-1` coordinates. If `d_x` is the residual core multiplicity, then

```text
sum_x C(d_x,2)<=C(520,2)(K'-1).
```

Balancing the fixed incidence sum minimizes the left side. Exact integer
division over the three floor intervals `a=33,34,35` excludes every row
through `K'=4835`. The endpoint transition is

```text
gap(4835)=-2110,       gap(4836)=115260.
```

Together with the rich-plane recurrence ceiling this gives

```text
4836<=K'<=595763,       452813<=|J|<=1043740.
```

The first 87 admissible rows, `K'=4836..4922`, overlap numerically with the
large-shared-core payment regime. This cycle does not transport that theorem:
its source interface quantifies over all low-margin minimizing pairs, while
the pair-pencil branch currently selects 520 quotient pair types.

## Burn-down

```text
starting local pin:       d6e0165c1
canonical prize pin:      0dd5b3244
upstream PR #1170 pin:    23b60807
DAG delta:                +1 PROVED pair-moment node, +2 edges
critical status delta:    none
compute spend:            none
closed interface:         dimension-three residual dimensions 3..4835
next action:              audit selected-pair coverage against payment quantifiers
```

## Nonclaims

- no shortened residual row is paid;
- numerical overlap with `K'<=4922` is not a source-interface theorem;
- dimension four, rank eleven, and the prize problems remain open.
