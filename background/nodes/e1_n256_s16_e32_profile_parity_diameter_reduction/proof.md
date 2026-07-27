# Proof

## Slack and integer profiles

The general chord inequality gives `L<=floor((E+66)/4)=24`. For a proposed
value of `L`, the exact global slack is

```text
Delta=E+66-4L.
```

The proved relaxed slack recurrence gives the complete boundary trace

```text
L       24  23  22  21  20  19  18
Delta    2   6  10  14  18  22  26
min E   56  52  48  44  40  36  32.
```

Thus `L<=18`. Enumerating the nonnegative integer solutions of

```text
sum_j j^2 n_j=32,       sum_j j n_j<=18
```

gives 18 profiles. The abstract nested-layer third-moment caps above the
cubic cutoff are

```text
2072 (4,7)       1920 (0,8)       1916 (7,4,1)
1784 (10,1,2)    1760 (3,5,1)     1624 (12,1,0,1)
1624 (6,2,2).
```

Every other profile has cap at most 1496.

Use the rational cubic Hermite majorant to `log` with double contacts 14 and
57. At `V=64`, exact substitution and range reduction give at `M_3=1517`

```text
-(555577/2544224) log 2
+(74553/79507) log(8/7)
+(4954/79507) log(64/57)
+27947/1475502 > 0,
```

whereas at `M_3=1518` the corresponding expression is

```text
-(555449/2544224) log 2
+(74555/79507) log(8/7)
+(4952/79507) log(64/57)
+4646/245917 < 0.
```

Eight-term rational atanh bounds certify both strict signs. Therefore every
profile whose abstract cap is at most 1517 has collision norm below `2^250`
and is impossible on a pair-feasible row.

## Parity and the diameter

The seven coefficient magnitudes are `2,2,2,1,1,1,1`. There are six
unit-product chords among the four light positions. Reduction of every
non-diameter signed autocorrelation coefficient modulo two gives

```text
A_d = number of light-light chords in class d  (mod 2). (4)
```

The signed-chord identity at `E=32` is

```text
32=102-D_64+2C.                                      (5)
```

Thus `D_64` is even. If `d_1,d_2,d_4` count light-light, heavy-light, and
heavy-heavy diameter edges, then

```text
D_64=d_1+4d_2+16d_4.
```

A diameter class is a matching, so `d_1<=2`, and parity forces
`d_1 in {0,2}`. Exhausting the matching capacities gives

```text
(d_1,d_2,d_4) =
(0,0,0),(2,0,0),(0,1,0),(0,2,0),(0,3,0),
(0,0,1),(2,0,1),(0,1,1).
```

These are exactly the eight values in (3), and (5) gives the stated `C`.

At most `6-d_1<=6` non-diameter unit chords can occupy odd distance classes.
This removes the four above-cutoff profiles having 8 or 12 odd coefficients
and leaves exactly (1). If `d_1=2`, a four-odd residual must place each of its
four remaining unit chords in a distinct class. If `d_1=0`, it has exactly
four odd classes among six unit chords. A zero-odd residual has even
multiplicity in every class by (4). QED.
