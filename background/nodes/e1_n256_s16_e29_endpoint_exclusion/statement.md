# E1 N=256 E=29 endpoint exclusion

- **status:** PROVED
- **closure:** exhaustive synthesis of proved reduction and exclusion

No pair-feasible `N=256` folded-profile `(3,4,0)` collision has
autocorrelation variance `V=58`.

The exact E29 reduction leaves precisely

```text
(5,6), (1,7), (4,4,1), (0,5,1),
(3,2,2), (5,2,0,1), (2,0,3), (1,3,0,1).
```

The proved joint exclusion removes all eight profiles. Consequently every
unresolved positive-variance vector in this folded profile has

```text
0 < V <= 56,       V even.
```
