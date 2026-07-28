# E1 N=256 E=16 four-profile exclusion

- **status:** PROVED
- **closure:** exact finite computation plus proved conductor reduction

At `N=256`, folded profile `(3,4,0)`, and variance `V=32`, all four routed
profiles are impossible collision profiles. Independent folded-chord and
direct-negacyclic engines each exhaust 3,056,582,144 vectors and agree exactly:

```text
profile       actual   full conductor   proper conductor
(4,3)            530              162                368
(0,4)              0                0                  0
(3,1,1)          158               16                142
(0,0,0,1)          0                0                  0
total             688              178                510
```

The conductor theorem excludes all 510 proper-conductor representatives.
FLINT and PARI/GP agree on all 178 full-conductor norms, with 78 distinct
values. The whole-norm maximum is

```text
3310692535087337739109785704249356622971820103039851493935549506897278325762,
```

and ten whole norms reach `2^250`. After stripping exact powers of two, the
maximum odd part is

```text
1655346267543668869554892852124678311485910051519925746967774753448639162881,
```

with `odd_max<2^250<2*odd_max`. Thus no odd pair-feasible row prime divides a
residual norm.
