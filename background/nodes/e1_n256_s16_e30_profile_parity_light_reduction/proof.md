# Proof

## Slack and profiles

The general chord inequality gives `L<=floor((30+66)/4)=24`. Put
`Delta=30+66-4L`. The proved relaxed slack recurrence gives

```text
L       24  23  22  21  20  19  18
Delta    0   4   8  12  16  20  24
min E   54  50  46  42  38  34  30.
```

Therefore `L<=18`. Exact enumeration of

```text
sum_j j^2 n_j=30,       sum_j j n_j<=18
```

gives 18 profiles. For the rational cubic Hermite majorant with double
contacts 14 and 57, the raw moments at `V=60` are

```text
(1,16,316,6976+M_3).
```

Exact substitution gives

```text
M_3=1087: (74161/79507, 5346/79507, -38165/1475502),
M_3=1088: (74163/79507, 5344/79507, -907/35131).
```

Eight-term rational atanh bounds certify

```text
-(580665/2544224)log 2 +(74161/79507)log(8/7)
 +(5346/79507)log(64/57)+38165/1475502 > 0,

-(580537/2544224)log 2 +(74163/79507)log(8/7)
 +(5344/79507)log(64/57)+907/35131 < 0.
```

Thus the exact cutoff is 1087. Thirteen profiles exceed it. Their
cap/profile/odd-count ledger is

```text
1908 (6,6)       6       1764 (9,3,1)     10
1748 (2,7)       2       1644 (12,0,2)    14
1600 (5,4,1)     6       1500 (14,0,0,1)  14
1476 (8,1,2)    10       1468 (1,5,1)      2
1340 (4,2,2)     6       1324 (10,1,0,1)  10
1236 (0,3,2)     2       1180 (6,2,0,1)    6
1128 (3,0,3)     6.
```

## Parity, diameter, and light supports

The signed-chord identity is

```text
30=102-D_64+2C.                                      (3)
```

Hence the number `d_1` of light-light diameter edges is even. Four light
vertices have at most two such edges. If `d_1=2`, the light support is two
antipodal pairs; its four remaining chords occur in two doubled folded
classes, so it has no odd class. Every profile in the ledger has a positive
even number of odd classes, hence `d_1=0`.

There are six non-diameter light chords, and modulo two they generate every
odd autocorrelation class. Thus profiles with odd count 10 or 14 are
impossible, leaving exactly (1).

Complete enumeration of the `binom(127,3)=333,375` normalized four-point
supports gives 8,168 with two odd classes and 280,720 with six. The two-odd
branch has partitions `2,2,1,1` on 7,920 supports and `3,2,1` on 248.
Canonicalization under translation and odd units gives 87 two-odd orbits,
split 82 and 5 by those partitions. The six-odd supports have partition
`1,1,1,1,1,1`. Since canonicalization uses at most four anchors and 64 odd
units, each normalized orbit has size at most 256, proving the 1,097-orbit and
21,773,185,792-vector lower bounds. An independent positive-gap enumeration
expands the 87 printed orbits disjointly and recovers all 8,168 supports while
independently recounting the six-odd branch.

Finally, matching capacities with `d_1=0` give
`D_64 in {0,4,8,12,16,20}`. Substitution in (3) gives (2). QED.
