# E1 N=256 E=28 endpoint exclusion

- **status:** PROVED
- **closure:** exhaustive synthesis of proved reduction and exclusion

No pair-feasible `N=256` folded-profile `(3,4,0)` collision has
autocorrelation variance `V=56`.

The exact E28 reduction leaves precisely

```text
(4,6), (0,7), (3,4,1), (2,2,2),
(4,2,0,1), (1,0,3), (0,3,0,1), (3,0,1,1).
```

The proved joint exclusion removes all eight profiles. Consequently every
unresolved positive-variance vector in this folded profile has

```text
0 < V <= 54,       V even.
```
