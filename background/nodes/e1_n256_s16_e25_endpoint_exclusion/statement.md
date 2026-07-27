# E1 N=256 E=25 endpoint exclusion

- **status:** PROVED
- **closure:** exhaustive synthesis of proved reduction and exclusion

No pair-feasible `N=256` folded-profile `(3,4,0)` collision has
autocorrelation variance `V=50`.

The exact E25 reduction leaves precisely

```text
(5,5), (1,6), (4,3,1), (0,4,1), (3,1,2),
(5,1,0,1), (1,2,0,1), (0,0,1,1), (0,0,0,0,1).
```

The proved joint exclusion removes all nine profiles. Consequently every
unresolved positive-variance vector in this folded profile has

```text
0 < V <= 48,       V even.
```
