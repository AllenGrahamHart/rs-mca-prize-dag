# Positive 433-1a aligned outside-product probe

This is exact finite-field evidence for the aligned `xi=eta` specialization
of `433-1a -> O0b`.  It is not a deployed-field theorem and does not cover
the near-aligned `xi in L^c` branch.

For each common survivor, the probe reconstructs the unique quadratic
product ratio from the rank-five common product block.  It places the
singleton's missing mate at `eta`, lets any of the five internal outside
products occupy that record, and asks whether the remaining six target
products can be assigned to three distinct unused antipodal source-label
pairs.  Target representatives and unused source pairs range over the
whole small field, so survival is only a necessary relaxed completion.
The original three runs imposed no outside sum row.

## Exact counts

```text
prime  common/cycle survivors  survivors with completion  target triples
13                         48                          0               0
17                        368                          0               0
29                       1072                         48             160
```

At `F_29`, only role cells `5` and `12` survive.  Aggregated over four
root-sign rows:

```text
cell  cycle sign  common points with completion  target triples
5             -1                              8              16
5             +1                             16              32
12            -1                              8              64
12            +1                             16              48
```

Cells `0,1,3,4,9,11,14` have zero completion at `F_29`; every tested cell
has zero completion at `F_13` and `F_17`.  Modal runs:

```text
F13  ap-GbxO9Tzy9FDXWd2iXX7urQ
F17  ap-qsdj1fpjiAdp2fcONyLWT9
F29  ap-AfDUnxANc4VDtbuKAv219S
```

## Exact-elimination boundary

One aligned cell-3 ideal over `F_2130706433` was tested with all common sum
rows, the forced mate product, three paired-product constraints, and the
full admissibility saturation.  A direct source-variable presentation
timed out at 130 seconds (`ap-E6pJY7vJcqMmRTbdjiXkQ9`).  Replacing the six
source equations by three explicit quadratic resultants still exhausted
the 180-second Modal function cap (`ap-ZAFf2iYtIe9hzMCa6lMD0g`).

These timeouts reject a raw all-case Groebner fanout as the next route.
They do not imply that the ideal is nonunit or that any packet exists.

## Missing-mate sum refinement

The common loop and any nonloop common sum row reconstruct the full common
coefficient kernel.  A second exact `F_29` run also imposed the
square-root-free sum equation at the aligned missing mate.  It retained
only:

```text
cell  cycle sign  common points  target triples
5             +1              8              16
```

Every product survivor in cell `5`, cycle `-1`, and in both signs of cell
`12` fails this first outside sum equation.  Thus the aggregate aligned
frontier falls from `48` common points and `160` target triples to `8` and
`16`.  This remains finite-field evidence under the same relaxed target and
source choices; the six other outside sum rows are not imposed.

Clean replay: `ap-zH5YzdeJ1cG4hfyK6Q9eTJ` (72/72 cases complete).

## Near-aligned refinement

The near-aligned mode places `xi` at a record distinct from the internal
`eta` record, removes the forced `xi` record, and pairs the remaining six
records over the three unused source deck pairs.  It imposes the same
squared sum at `xi`.

```text
prime  common/cycle survivors  product points  product triples  sum points  sum triples
13                         48               0                0           0            0
17                        368               0                0           0            0
29                       1072              88              288          32           64
```

The `F_29` missing-mate-sum survivors are exactly:

```text
cell  cycle sign  common points  target triples
4             -1             16              32
5             +1              8              16
12            -1              8              16
```

All 72 cases at each prime completed.  Modal runs:

```text
F13  ap-WmRDAbdJ2aYTgHG83lIHP8
F17  ap-k9y0M76KmbUE4qf16AhLNz
F29  ap-3u9hr5P3djUL4LhW10TZHm
```

These are exact counts for the finite-field relaxation only.  In
particular, `F_13/F_17` emptiness does not delete a deployed-field cell, and
the `F_29` survivors have not passed the other six outside sum rows.
