# E1 N=256 E=22 eight-profile exclusion

- **status:** PROVED
- **closure:** exact finite computation plus proved conductor reduction

At `N=256`, folded profile `(3,4,0)`, and variance `V=44`, all eight routed
profiles are impossible collision profiles.  Independent folded-chord and
direct-negacyclic engines each exhaust 26,219,123,456 vectors and agree
exactly:

```text
profile        actual   full conductor   proper conductor
(6,4)           15924             9688               6236
(2,5)            5228             2550               2678
(5,2,1)          4532             2074               2458
(1,3,1)          1096              242                854
(4,0,2)           790              368                422
(0,1,2)            22                0                 22
(6,0,0,1)         104               28                 76
(2,1,0,1)         302               52                250
total            27998            15002              12996
```

The conductor theorem excludes all 12,996 proper-conductor representatives.
FLINT and PARI/GP agree on all 15,002 full-conductor norms, with 5,991
distinct values and

```text
N_max = 1336721602285440319478157639166117651370659494817695620407452489394658888194,
N_max < 2^250 < 2*N_max.
```

Thus no pair-feasible row prime divides a residual norm.
