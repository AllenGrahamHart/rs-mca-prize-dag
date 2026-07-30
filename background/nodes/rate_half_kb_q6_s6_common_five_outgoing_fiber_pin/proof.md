# Proof

Use the notation of Corollaries 9.25 and 9.27 of the pinned equality-wall
source theorem. Corollary 9.25 constructs the invariant-coordinate label set
`I`, the invariant-fiber image `L`, and the five-point source-pole set
`K`, with

```text
K subset I intersect L.
```

This proves `(KBF-1)`.

For a source label `j notin I`, Corollary 9.27 gives the exact vertical
outgoing divisor

```text
O_j=psi^* K + b Z_j.                                (1)
```

Thus every point `pi` over every `alpha_k`, `k in K`, is a root of
`F_out(alpha_j,X)` for all six labels `j notin I`.

For `x in I`, the same corollary gives

```text
O_x=psi^*(
  {alpha_1,...,alpha_12}
  minus (K union {alpha_(tau(x))})
).                                                  (2)
```

No point over a label in `K` occurs in `(2)`. Hence at `pi` the outgoing
horizontal fiber contains every label in `I^c` and no label in `I`.
There are six labels in `I^c`, equal to the `T`-degree of `F_out`, so
the root divisor is exactly `(KBF-2)`. Every component root is a root of
the product `F_out`, proving the final assertion. QED.
