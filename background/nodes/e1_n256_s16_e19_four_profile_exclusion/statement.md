# E1 N=256 E=19 four-profile exclusion

- **status:** PROVED
- **closure:** exact finite computation plus proved conductor reduction

At `N=256`, folded profile `(3,4,0)`, and variance `V=38`, all four routed
profiles are impossible collision profiles. Independent folded-chord and
direct-negacyclic engines each exhaust 158,783,488 vectors and agree exactly:

```text
profile        actual   full conductor   proper conductor
(3,4)             370              112                258
(2,2,1)           182               24                158
(1,0,2)            10                0                 10
(3,0,0,1)          12                0                 12
total              574              136                438
```

The conductor theorem excludes all 438 proper-conductor representatives.
FLINT and PARI/GP agree on all 136 full-conductor norms, with 40 distinct
values and

```text
N_max = 1096349292027446593481621675930218905147073043465918102751396673154250061826,
N_max < 2^250 < 2*N_max.
```

Thus no pair-feasible row prime divides a residual norm.
