# Proof

## Slack and profiles

The general chord inequality gives `L<=floor((31+66)/4)=24`. Put
`Delta=31+66-4L`. The proved relaxed slack recurrence gives

```text
L       24          23  22  21  20  19  18  17
Delta    1           5   9  13  17  21  25  29
min E   infeasible  55  51  47  43  39  35  31.
```

Therefore `L<=17`. Exact enumeration of

```text
sum_j j^2 n_j=31,       sum_j j n_j<=17
```

gives 15 profiles. For the rational cubic Hermite majorant with double
contacts 14 and 57, exact substitution at `V=62` gives the forms

```text
M_3=1302: (74357/79507, 5150/79507, -16528/737751),
M_3=1303: (74359/79507, 5148/79507, -10995/491834).
```

Eight-term rational atanh bounds certify

```text
-(568121/2544224)log 2 +(74357/79507)log(8/7)
 +(5150/79507)log(64/57)+16528/737751 > 0,

-(567993/2544224)log 2 +(74359/79507)log(8/7)
 +(5148/79507)log(64/57)+10995/491834 < 0.
```

Thus every profile whose nested-layer cap is at most 1302 has collision norm
below `2^250`. Eight profiles have larger cap. Their cap/profile/odd-count
ledger is

```text
1906 (3,7)      3       1754 (6,4,1)    7
1626 (9,1,2)   11       1610 (2,5,1)    3
1478 (5,2,2)    7       1470 (11,1,0,1) 11
1362 (1,3,2)    3       1314 (7,2,0,1)   7.
```

## Parity, diameter, and light support

The signed-chord identity is

```text
31=102-D_64+2C.                                      (4)
```

Hence `D_64` is odd. If `d_1,d_2,d_4` count light-light, heavy-light, and
heavy-heavy diameter edges, then `D_64=d_1+4d_2+16d_4`. A diameter class is a
matching and `d_1<=2`, so `d_1=1`. Exactly five non-diameter light-light
chords remain, and modulo two they generate every odd autocorrelation class.
The five profiles with odd count 7 or 11 are impossible, leaving exactly (1).

Matching capacities give `(d_4,d_2)=(0,0),(0,1),(0,2),(1,0),(1,1)`, hence
(3). Each surviving profile has three odd classes among the five non-diameter
light chords. Their multiplicities must therefore be `2,1,1,1`; the other
integer possibility `3,1,1` is geometrically absent.

Translate one light point to zero and enumerate the other three positions.
Of `binom(127,3)=333,375` normalized supports, exactly 960 have one diameter
and three odd non-diameter classes. Their non-diameter multiplicities are all
`2,1,1,1`, and the repeated edges always share a vertex. Canonicalization under
odd units and translation gives exactly the eight representatives (2), with
normalized orbit-size histogram `32:2, 64:2, 128:2, 256:2`.

An independent enumeration in positive circular-gap coordinates expands the
eight printed orbits, proves they are disjoint, and recovers all 960 supports.
This proves the reduction and router. QED.
