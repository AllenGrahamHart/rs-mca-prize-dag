# Result

The two-type-1 projective-fibre mechanism is proved, but its endpoint payoff
is now exactly calibrated:

```text
baseline fibre sum = 6m,
baseline outside spend = 2m+1,
baseline total cap = 9m/2,
required fibre sum = 25m/4,
missing fibre mass = m/4.
```

At the official `m=2^37`, the mechanism supplies spend
`274877906945` and total cap `618475290624`, exceeding the target
`549755813888` by `68719476736`. Closure through this argument requires an
additional `34359738368` points in the two named fibres, or the same total
deficit in their type-1 root-set sizes.

The route is narrowed, not closed. The next theorem must force the calibrated
concentration, obtain extra spend from overlap slack beyond `(TFC3)`, or use
a collective inequality that does not reduce to uniform pointwise spend.
