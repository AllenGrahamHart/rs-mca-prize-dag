# Cycle 348: MCA rank-11 exact petal partition (2026-08-15)

Cycle 347 bounded each petal charge by its worst charge per coordinate.
This cycle retains the same proved residual geometry but solves the integer
petal partition exactly, closing 106 additional rows.

## Exact packing

Write `a=m'-j-1` and `D_1=981105`. The disjoint petals obey

```text
0<=s_p<=a,       sum_p s_p<=D_1+a,
q_j(s)=s(j-9)+C(s,2).
```

Convex transfers merge any two partial petals or fill one to size `a`.
Thus the relaxed partition maximum consists of

```text
r=1+floor(D_1/a) full petals and b=D_1 mod a remaining coordinates.
```

For fixed `a`, the resulting charge is a line in `K'`. On the claimed
interval the quotient `floor(D_1/a)` has four blocks, and convexity within
each block reduces the global comparison to eight endpoints. Their gaps
below the `a=67472` line at `K'=15634` are

```text
0, 676268727, 676325879, 3265037774,
3265407519, 6322001175, 6322245154, 7515065748.
```

Since every competing line has larger slope, these nonnegative gaps at the
last row prove `a=67472` is maximal at every earlier row. Its partition has
fifteen full petals and remainder `36497`, yielding

```text
W_B<=981105*(1048577*K'+34798536326).
```

## Boundary

Exact arithmetic gives

```text
K'=15528: demand=50114371326035640,
           cap   =50115667510540110;

K'=15529: demand=50120589875892136,
           cap   =50116696274677695.
```

The non-Reed--Solomon factor in the demand/cap ratio has forward numerator

```text
1048577*K'^2+69598121229*K'-77044697164886.
```

After shifting `K'=15529+x`, all three coefficients are positive. The
crossing therefore persists through `15634`; prior proved cuts cover every
higher row.

The primary certificate replays all 15,625 rows, the four quotient blocks,
eight endpoint gaps, and eight hostile mutations. An independent audit
scans all 15,625 admissible ceilings at the worst row and checks 1,782
small convex partitions with a separate dynamic-programming oracle.

```text
result:                PROVED rank-nine closure on K'>=15529
newly closed rows:     15529..15634 (106 rows)
remaining rank nine:  10..15528
new premise:           none
compute:               constant-memory exact integers under RAMguard
next route action:     exploit cross-chart incidence or a second owner
                       resource on the surviving low interval
```
