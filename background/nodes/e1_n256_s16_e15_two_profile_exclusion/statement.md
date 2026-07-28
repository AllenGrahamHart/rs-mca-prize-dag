# E1 N=256 E=15 two-profile exclusion

- **status:** PROVED
- **closure:** exact finite computation plus proved conductor reduction

At `N=256`, folded profile `(3,4,0)`, and variance `V=30`, both routed
profiles are impossible collision profiles. Independent folded-chord and
direct-negacyclic engines each exhaust 158,783,488 vectors and agree exactly:

```text
profile       actual   full conductor   proper conductor
(3,3)            258               64                194
(2,1,1)           36                0                 36
total             294               64                230
```

The conductor theorem excludes all 230 proper-conductor representatives.
FLINT and PARI/GP agree on all 64 full-conductor norms, with 28 distinct
values. The whole-norm maximum is

```text
3003171528471974836716922425205211633163258783488230570091067301168069285892,
```

and 32 whole norms reach `2^250`. After stripping exact powers of two, the
maximum odd part is

```text
1263041506267492322130816623667822529962454800313964008196082776100356004097,
```

with `odd_max<2^250<2*odd_max`. Thus no odd pair-feasible row prime divides a
residual norm.
