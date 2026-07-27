# Proof

## Slack and integer profiles

The general chord inequality gives `L<=floor((E+66)/4)=24`. For a proposed
value of `L`, the exact global slack is

```text
Delta=E+66-4L.
```

The proved relaxed slack recurrence gives the complete boundary trace

```text
L       24  23  22  21  20  19
Delta    3   7  11  15  19  23
min E   53  49  45  41  37  33.
```

Thus `L<=19`. Enumerating the nonnegative integer solutions of

```text
sum_j j^2 n_j=33,       sum_j j n_j<=19
```

gives 21 profiles. The abstract nested-layer third-moment caps greater than
the cubic cutoff are

```text
2246 (5,7)       2086 (8,4,1)     2082 (1,8)
1950 (11,1,2)    1918 (4,5,1)     1786 (13,1,0,1)
1782 (0,6,1)     1778 (7,2,2).
```

Every other profile has cap at most 1638.

Use the rational cubic Hermite majorant to `log` with double contacts 14 and
57. At `V=66`, exact substitution and range reduction give at `M_3=1732`

```text
-(543033/2544224) log 2
+(74749/79507) log(8/7)
+(4758/79507) log(64/57)
+601/38829 > 0,
```

whereas at `M_3=1733` the corresponding expression is

```text
-(542905/2544224) log 2
+(74751/79507) log(8/7)
+(4756/79507) log(64/57)
+7589/491834 < 0.
```

Eight-term rational atanh bounds certify both strict signs. Therefore every
profile whose abstract cap is at most 1732 has collision norm below `2^250`
and is impossible on a pair-feasible row.

## Parity and the diameter

The seven coefficient magnitudes are always

```text
2,2,2,1,1,1,1.
```

There are six unit-product chords, namely the chords among the four light
positions. Reduction of every non-diameter signed autocorrelation coefficient
modulo two gives

```text
A_d = number of light-light chords in class d  (mod 2). (4)
```

The signed-chord identity at `E=33` is

```text
33=102-D_64+2C.                                       (5)
```

Thus `D_64` is odd. Diameter chords form a matching. Among four light
vertices there can be zero, one, or two light-light diameter edges, while all
other diameter products have even square mass. Oddness therefore forces
exactly one light-light diameter. Only five unit chords remain in (4), so the
number of odd `A_d` is at most five. Applying this to the eight profiles above
the cubic cutoff removes `(8,4,1)`, `(11,1,2)`, `(13,1,0,1)`, and `(7,2,2)`,
whose odd counts are respectively `9,13,13,9`. This leaves exactly (1).

If five coefficients are odd, all five available unit chords must lie in
distinct non-diameter classes, proving the diameter-Sidon assertion.

After the forced light-light diameter, two light and three heavy vertices
remain. With no heavy-heavy diameter there are at most two heavy-light
diameters; with one heavy-heavy diameter there is at most one. Therefore

```text
D_64=1+4d_2+16d_4,
(d_4,d_2) in {(0,0),(0,1),(0,2),(1,0),(1,1)}.
```

This is the set in (3), and (5) gives the displayed cross sums. QED.
