# Proof

## Slack and profiles

The general chord inequality gives `L<=floor((29+66)/4)=23`. Put
`Delta=29+66-4L`. The proved relaxed slack recurrence gives

```text
L       23  22  21  20  19  18  17
Delta    3   7  11  15  19  23  27
min E   53  49  45  41  37  33  29.
```

Therefore `L<=17`. Exact enumeration of

```text
sum_j j^2 n_j=29,       sum_j j n_j<=17
```

gives 17 profiles. For the rational cubic Hermite majorant with double
contacts 14 and 57, the raw moments at `V=58` are

```text
(1,16,314,6880+M_3).
```

Exact substitution at the sign boundary gives

```text
M_3=872: (73965/79507, 5542/79507, -3091/105393),
M_3=873: (73967/79507, 5540/79507, -14401/491834).
```

Eight-term rational atanh bounds certify

```text
-(593209/2544224)log 2 +(73965/79507)log(8/7)
 +(5542/79507)log(64/57)+3091/105393 > 0,

-(593081/2544224)log 2 +(73967/79507)log(8/7)
 +(5540/79507)log(64/57)+14401/491834 < 0.
```

Thus the exact cutoff is 872. Thirteen profiles exceed it. Their
cap/profile/odd-count ledger is

```text
1746 (5,6)        5       1606 (8,3,1)      9
1598 (1,7)        1       1490 (11,0,2)    13
1454 (4,4,1)      5       1350 (13,0,0,1)  13
1334 (7,1,2)      9       1334 (0,5,1)      1
1210 (3,2,2)      5       1186 (9,1,0,1)    9
1054 (5,2,0,1)    5       1014 (2,0,3)      5
 954 (1,3,0,1)    1.
```

## Parity, diameter, and light supports

The signed-chord identity is

```text
29=102-D_64+2C.                                      (3)
```

Hence `D_64` is odd. Heavy-heavy and heavy-light diameter edges contribute
16 and 4 to `D_64`, while each light-light diameter contributes 1. Diameter
edges form a matching, so four light vertices have at most two such edges.
Their number is therefore exactly one.

The remaining five light-light chords generate every odd autocorrelation
class modulo two. A profile can consequently have at most five odd classes.
Deleting the five ledger entries with 9 or 13 odd classes leaves exactly (1).

Complete enumeration of the `binom(127,3)=333,375` normalized four-point
supports finds, among supports with one diameter, 264 with one odd class, 960
with three, and 14,400 with five. Canonicalization under translation and odd
units gives respectively 11, 8, and 100 orbits. Their multiplicity partitions
are exactly those in the statement; in all 960 three-odd supports, the unique
repeated chord pair shares a vertex. Since no surviving profile has three odd
classes, the 11 one-odd and 100 five-odd representatives form a complete
router for (1).

The light diameter consumes two light vertices. The remaining matching can
contain either one heavy-heavy diameter or up to two heavy-light diameters,
subject to disjointness. Their square-mass contributions give precisely
`D_64 in {1,5,9,17,21}`. Substitution in (3) gives (2). QED.
