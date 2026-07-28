# E1 N=256 E=26 endpoint exclusion

- **status:** PROVED
- **closure:** exhaustive synthesis of proved reduction and exclusions

No pair-feasible `N=256` folded-profile `(3,4,0)` collision has
autocorrelation variance `V=52`.

The exact E26 reduction leaves precisely six two-odd profiles

```text
(2,6), (1,4,1), (0,2,2), (2,2,0,1), (1,0,1,1), (1,0,0,0,1)
```

and four six-odd profiles

```text
(6,5), (5,3,1), (4,1,2), (6,1,0,1).
```

The proved branch exclusions remove all ten profiles. Consequently every
unresolved positive-variance vector in this folded profile has

```text
0 < V <= 50,       V even.
```
