# E1 N=256 E=20 six-profile exclusion

- **status:** PROVED
- **closure:** exact finite computation plus proved conductor reduction

At `N=256`, folded profile `(3,4,0)`, and variance `V=40`, all six routed
profiles are impossible collision profiles. Independent folded-chord and
direct-negacyclic engines each exhaust 3,056,582,144 vectors and agree
exactly:

```text
profile        actual   full conductor   proper conductor
(4,4)            2588             1090               1498
(0,5)            2160              544               1616
(3,2,1)           888              194                694
(2,0,2)            52                8                 44
(4,0,0,1)          34                0                 34
(0,1,0,1)         704               64                640
total             6426             1900               4526
```

The conductor theorem excludes all 4,526 proper-conductor representatives.
FLINT and PARI/GP agree on all 1,900 full-conductor norms, with 526 distinct
values and

```text
N_max = 1047057848181589561057910777870710713025120091730047736000219719807296950274,
N_max < 2^250 < 2*N_max.
```

Thus no pair-feasible row prime divides a residual norm.
