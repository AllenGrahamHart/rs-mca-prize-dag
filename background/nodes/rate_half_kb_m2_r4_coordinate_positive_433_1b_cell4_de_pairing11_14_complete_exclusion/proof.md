# Proof

The pairing-11/14 orbit theorem supplies

```text
(0,11), (1,11), (2,11), (2,14).
```

The exact positive-`DE` pairing-14 theorem supplies the remaining labels

```text
(0,14), (1,14).
```

Their union is exactly `{0,1,2} x {11,14}`, with no overlap between the two
new labels and the four-label parent. Hence all six labels and their
`6*4*4=96` raw sign/lane cases are empty.

Under the proved parallel-`DE` action these six labels are exactly three
orbits:

```text
{(0,11),(1,11)}, {(2,11),(2,14)}, {(0,14),(1,14)}.
```

The prior complete block paid 39 labels in 21 orbits. Therefore the
cumulative ledger is `39+6=45` labels in `21+3=24` orbits, leaving
`105-45=60` labels in `60-24=36` orbits. QED.
