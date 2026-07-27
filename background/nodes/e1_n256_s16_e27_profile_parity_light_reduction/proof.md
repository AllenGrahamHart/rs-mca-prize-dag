# Proof

## Slack and profiles

The general chord inequality gives `L<=floor((27+66)/4)=23`. Put
`Delta=27+66-4L`. The proved relaxed slack recurrence gives

```text
L       23    22  21  20  19  18  17  16  15
Delta    1     5   9  13  17  21  25  29  33
min E   --    55  51  47  43  39  35  31  27.
```

Therefore `L<=15`. Exact enumeration of

```text
sum_j j^2 n_j=27,       sum_j j n_j<=15
```

gives 12 profiles. For the rational cubic Hermite majorant with double
contacts 14 and 57, the raw moments at `V=54` are

```text
(1,16,310,6688+M_3).
```

Exact substitution at the sign boundary gives

```text
M_3=443: (73575/79507, 5932/79507, -17807/491834),
M_3=444: (73577/79507, 5930/79507, -26675/737751).
```

Eight-term rational atanh bounds certify

```text
-(618169/2544224)log 2 +(73575/79507)log(8/7)
 +(5932/79507)log(64/57)+17807/491834 > 0,

-(618041/2544224)log 2 +(73577/79507)log(8/7)
 +(5930/79507)log(64/57)+26675/737751 < 0.
```

Thus the exact cutoff is 443. Eleven profiles exceed it. Their
cap/profile/odd-count ledger is

```text
1446 (3,6)        3       1314 (6,3,1)      7
1206 (9,0,2)     11       1186 (2,4,1)      3
1074 (11,0,0,1) 11       1074 (5,1,2)      7
 974 (1,2,2)      3        934 (7,1,0,1)    7
 826 (3,2,0,1)    3        810 (0,0,3)      3
 670 (2,0,1,1)    3.
```

## Parity, diameter, and light supports

The signed-chord identity is

```text
27=102-D_64+2C.                                      (3)
```

Hence `D_64` is odd. Heavy-heavy and heavy-light diameter edges contribute
16 and 4 to `D_64`, while each light-light diameter contributes 1. Diameter
edges form a matching, so the four light vertices contain exactly one
light-light diameter.

The remaining five light-light chords generate every odd autocorrelation
class modulo two. A profile can consequently have at most five odd classes.
Deleting the five ledger entries with 7 or 11 odd classes leaves exactly (1).

Complete enumeration of the `binom(127,3)=333,375` normalized four-point
supports finds, among supports with one diameter, 264 with one odd class, 960
with three, and 14,400 with five. Canonicalization under translation and odd
units gives respectively 11, 8, and 100 orbits. Their multiplicity partitions
are exactly those in the statement; in all 960 three-odd supports, the unique
repeated chord pair shares a vertex. Since every surviving profile has three
odd classes, the eight three-odd representatives form a complete router.

The light diameter consumes two light vertices. The remaining matching can
contain either one heavy-heavy diameter or up to two heavy-light diameters,
subject to disjointness. Their square-mass contributions give precisely
`D_64 in {1,5,9,17,21}`. Substitution in (3) gives (2). QED.
