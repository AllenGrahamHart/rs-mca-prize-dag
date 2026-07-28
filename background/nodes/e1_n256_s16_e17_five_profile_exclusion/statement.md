# E1 N=256 E=17 five-profile exclusion

- **status:** PROVED
- **closure:** exact finite computation plus proved conductor reduction

At `N=256`, folded profile `(3,4,0)`, and variance `V=34`, all five routed
profiles are impossible collision profiles. Independent folded-chord and
direct-negacyclic engines each exhaust 2,203,120,896 vectors and agree exactly:

```text
profile       actual   full conductor   proper conductor
(5,3)            608              196                412
(1,4)          1,152              272                880
(4,1,1)          188               20                168
(0,2,1)           92                0                 92
(1,0,0,1)         10                0                 10
total           2,050              488              1,562
```

The conductor theorem excludes all 1,562 proper-conductor representatives.
FLINT and PARI/GP agree on all 488 full-conductor norms, with 108 distinct
values. The whole-norm maximum is

```text
2816861446662266258222239103326104068711609833031798890850684996153986296836,
```

and 16 whole norms reach `2^250`. After stripping exact powers of two, the
maximum odd part is

```text
744372174442013450465816409476894770650462784978029532566873973061928116737,
```

with `2*odd_max<2^250<3*odd_max`. Thus no odd pair-feasible row prime divides
a residual norm.
