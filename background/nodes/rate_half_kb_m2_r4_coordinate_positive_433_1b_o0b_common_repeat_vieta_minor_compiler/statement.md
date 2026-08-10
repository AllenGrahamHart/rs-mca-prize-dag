# KoalaBear m2 r4 positive `433-1b/O0b` repeated-BC common compiler

- **status:** PROVED
- **scope:** the common fibers of the `SBC` stratum in `433-1b -> O0b`
- **dependencies:** source-facet signature, complete-fiber Vieta compiler, and
  the `433-1b/O0b` signed-edge atlas

Normalize the common target representatives to `A=1,B=b,C=c`. In `SBC`,
the two `BC` records have one common sign `sigma in {+1,-1}`:

```text
roles:     LA,    AB,   AC,       BC1,       BC2
products: -1,     b,    c, sigma*b*c, sigma*b*c
sums:       0,   1+b,  1+c, b+sigma*c, b+sigma*c.       (KBO0BR-1)
```

The five common source labels form two opposite pairs and one singleton.
There are fifteen role cells and four square-root sign rows per cell. With
the two values of `sigma`, this gives 120 algebra rows. Swapping the two
duplicate `BC` roles partitions the fifteen cells into nine exact orbits:

```text
[0] [1,2] [3] [4,5] [6] [7,8] [9,12] [10,13] [11,14].
```

For each row, the complete-fiber Vieta construction gives a `10 x 8`
matrix. On the principal stratum where its five product rows and loop sum
row have rank six, common rank at most seven is equivalent to the vanishing
of the six `8 x 8` minors obtained by appending each pair of the four
remaining sum rows.

Exact compilation over `F_2130706433` completed every row in raw and
guard-stripped modes. The raw degree histogram, for either `sigma`, is

```text
18:72, 19:84, 21:104, 22:88, 23:4, 24:8.
```

For either sign, stripping only the printed source-label and target-open-set
guards gives

```text
7:8, 8:32, 9:24, 10:72, 11:176, 12:48.
```

The stripped term range is `16..66` for `sigma=-1` and `12..56` for
`sigma=+1`. Each sign has 99 distinct minor digests, and every algebra row
has six distinct nonzero minors.

This is an exact principal-stratum compiler. It does not exclude base-rank
drop, solve a common ideal, append outside records, close `433-1b -> O0b`,
pay distinct slopes, prove K3, or prove either Prize result.

## Falsifier

A missing cell/sign row, an incorrect repeated product or sum, failure of
the rank/minor equivalence, invalid guard division, or a custody mismatch.
