# Proof

The pairing-5/12 orbit theorem supplies

```text
(0,5), (1,5), (2,5), (2,12).
```

The exact positive-`DE` pairing-12 theorem supplies the remaining labels

```text
(0,12), (1,12).
```

Their union is exactly `{0,1,2} x {5,12}`, with no overlap between the two
new labels and the four-label parent. Hence all six labels and their
`6*4*4=96` raw sign/lane cases are empty.

Under the proved parallel-`DE` action these six labels are exactly three
orbits:

```text
{(0,5),(1,5)}, {(2,5),(2,12)}, {(0,12),(1,12)}.
```

The prior complete block paid 21 labels in 12 orbits. Therefore the
cumulative ledger is `21+6=27` labels in `12+3=15` orbits, leaving
`105-27=78` labels in `60-15=45` orbits. QED.
