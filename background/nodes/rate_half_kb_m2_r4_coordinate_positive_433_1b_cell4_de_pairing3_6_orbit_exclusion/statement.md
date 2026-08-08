# Statement

## Claim `(KBP1B4-DE-P36-1)`

In the deployed positive `433-1b -> O0a` cell-4 outside atlas, the following
four labeled missing/matching slices are empty:

```text
(xi,pairing) = (0,3), (1,3), (2,3), (2,6).             (1)
```

The first three slices are the proved pairing-3 theorem. Exchange of the two
identical positive `DE` records has the two relevant orbits

```text
{(0,3),(1,3)},  {(2,3),(2,6)}.                         (2)
```

Thus (2) transports the proved `(2,3)` slice to `(2,6)`. With four source
signs and four target lanes, (1) contains

```text
4 slices * 4 source signs * 4 target lanes = 64 raw cases.
```

Together with the nine proved first-pair slices, 13 of the 105 cell-4
missing/matching labels are paid. In the 60-orbit quotient, those labels
occupy eight paid orbits, leaving 92 labels in 52 live orbits.

The involution exchanges `xi=0` and `xi=1` while fixing the matching index.
It therefore does **not** transport either positive omission from pairing 3
to pairing 6. Those two pairing-6 slices remain open.

## Falsifier

A different orbit for any label in (1), a source/target sign dependence in
the involution, or a claim that `(0,6)` or `(1,6)` follows from this
composition.
