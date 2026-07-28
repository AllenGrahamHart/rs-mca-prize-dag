# E1 N=256 E=23 four-profile exclusion

- **status:** PROVED
- **closure:** exact finite computation plus proved conductor reduction

At `N=256`, folded profile `(3,4,0)`, and variance `V=46`, all four routed
profiles are impossible collision profiles.  Independent folded-chord and
direct-negacyclic engines each exhaust 158,783,488 vectors and agree exactly:

```text
profile        actual   full conductor   proper conductor
(3,5)            1176              352                824
(2,3,1)           522              108                414
(1,1,2)            46                0                 46
(3,1,0,1)         144               24                120
total             1888              484               1404
```

The conductor theorem excludes all 1,404 proper-conductor representatives.
FLINT and PARI/GP agree on all 484 full-conductor norms, with 176 distinct
values and

```text
N_max = 721495288731652690472090495266069052907254127194382380048009480013819013124,
2*N_max < 2^250 < 3*N_max.
```

Thus no pair-feasible row prime divides a residual norm.
