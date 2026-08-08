# Proof

The pairing-7/10 orbit theorem supplies

```text
(0,7), (1,7), (2,7), (2,10).
```

The exact positive-`DE` pairing-10 theorem supplies the remaining labels

```text
(0,10), (1,10).
```

Their union is exactly `{0,1,2} x {7,10}`, with no overlap between the two
new labels and the four-label parent. Hence all six labels and their
`6*4*4=96` raw sign/lane cases are empty.

Under the proved parallel-`DE` action these six labels are exactly three
orbits:

```text
{(0,7),(1,7)}, {(2,7),(2,10)}, {(0,10),(1,10)}.
```

The prior complete block paid 27 labels in 15 orbits. Therefore the
cumulative ledger is `27+6=33` labels in `15+3=18` orbits, leaving
`105-33=72` labels in `60-18=42` orbits. QED.
