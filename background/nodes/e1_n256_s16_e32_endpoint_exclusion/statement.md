# E1 N=256 square-mass-16 variance-64 endpoint exclusion

- **status:** PROVED
- **closure:** proof

No pair-feasible `N=256` folded-profile `(3,4,0)` collision has
autocorrelation variance `V=64`.

The exact profile reduction leaves only

```text
(4,7), (0,8), (3,5,1).
```

The zero-odd census excludes `(0,8)`, the joint light-template census and
cubic certificate exclude `(3,5,1)`, and the complete exact norm census
excludes `(4,7)`. These cases are exhaustive. Consequently the remaining
positive even variance frontier is

```text
0 < V <= 62.
```
