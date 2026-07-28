# E1 N=256 E=21 seven-profile exclusion

- **status:** PROVED
- **closure:** exact finite computation plus proved conductor reduction

At `N=256`, folded profile `(3,4,0)`, and variance `V=42`, all seven routed
profiles are impossible collision profiles. Independent folded-chord and
direct-negacyclic engines each exhaust 2,203,120,896 vectors and agree
exactly:

```text
profile        actual   full conductor   proper conductor
(5,4)            6400             3608               2792
(1,5)            1676              488               1188
(4,2,1)          1658              456               1202
(0,3,1)           252               16                236
(3,0,2)           348               68                280
(5,0,0,1)          44                4                 40
(1,1,0,1)          76                0                 76
total            10454             4640               5814
```

The conductor theorem excludes all 5,814 proper-conductor representatives.
FLINT and PARI/GP agree on all 4,640 full-conductor norms, with 1,365 distinct
values and

```text
N_max = 1067431210213337343847285566520999617146298326197261566762764923557911188994,
N_max < 2^250 < 2*N_max.
```

Thus no pair-feasible row prime divides a residual norm.
