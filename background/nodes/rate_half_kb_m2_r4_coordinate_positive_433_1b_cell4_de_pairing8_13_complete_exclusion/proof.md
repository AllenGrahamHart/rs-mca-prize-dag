# Proof

The pairing-8/13 orbit theorem supplies

```text
(0,8), (1,8), (2,8), (2,13).
```

The exact positive-`DE` pairing-13 theorem supplies the remaining labels

```text
(0,13), (1,13).
```

Their union is exactly `{0,1,2} x {8,13}`, with no overlap between the two
new labels and the four-label parent. Hence all six labels and their
`6*4*4=96` raw sign/lane cases are empty.

Under the proved parallel-`DE` action these six labels are exactly three
orbits:

```text
{(0,8),(1,8)}, {(2,8),(2,13)}, {(0,13),(1,13)}.
```

The prior complete block paid 33 labels in 18 orbits. Therefore the
cumulative ledger is `33+6=39` labels in `18+3=21` orbits, leaving
`105-39=66` labels in `60-21=39` orbits. QED.
