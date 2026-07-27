# E1 N=256 E=27 endpoint exclusion

- **status:** PROVED
- **closure:** exhaustive synthesis of proved reduction and exclusion

No pair-feasible `N=256` folded-profile `(3,4,0)` collision has
autocorrelation variance `V=54`.

The exact E27 reduction leaves precisely

```text
(3,6), (2,4,1), (1,2,2),
(3,2,0,1), (0,0,3), (2,0,1,1).
```

The proved joint exclusion removes all six profiles. Consequently every
unresolved positive-variance vector in this folded profile has

```text
0 < V <= 52,       V even.
```
