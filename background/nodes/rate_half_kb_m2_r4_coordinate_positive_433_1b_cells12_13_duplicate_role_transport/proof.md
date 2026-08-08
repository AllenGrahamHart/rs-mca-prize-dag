# Proof

Cell `12` has singleton `BC-` and matching `(LA,AB),(AC,BC+)`; cell `13`
has the same singleton and matching `(LA,AC),(AB,BC+)`. Under `B/C` exchange,
the common target products and sums are exchanged in exactly those roles.
The `BC-` sum changes sign, which is compensated by `t -> -t`; all source
labels are unchanged. Direct symbolic expansion checks all five common
product, signed-sum, and label triples in all four source-sign rows.

Gauge `D,E,F` by `sigma_c`. Then the outside atlas

```text
DE, DE, -DE, DF, sigma_o EF, BF, sigma_c CF
```

is fixed except for exchange of its last two entries. The same is true of
the seven squared sums, and the full target guard divisor is preserved up to
units. For each missing record, the induced permutation of the six residual
positions maps the 15 perfect matchings bijectively to themselves. This is
checked in all four target lanes, yielding 420 lane/label bijections and,
after the four source-sign rows, 1680 principal systems.

The cited global theorem excludes product-rank drop in both cells. Therefore
emptiness of every principal cell-12 system transports to principal cell 13,
and rank-drop emptiness completes the implication. QED.
