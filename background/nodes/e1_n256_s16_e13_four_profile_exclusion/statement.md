# E1 N=256 E=13 four-profile exclusion

- **status:** PROVED
- **closure:** exact finite computation plus proved conductor and prime-field reductions

At `N=256`, folded profile `(3,4,0)`, and variance `V=26`, all four routed
profiles are impossible collision profiles. Independent folded-chord and
direct-negacyclic engines each exhaust 2,203,120,896 vectors and agree:

```text
profile       actual   full conductor   proper conductor
(5,2)            418              112                306
(1,3)            252                0                252
(4,0,1)          104               16                 88
(0,1,1)           46                8                 38
total             820              136                684
```

The conductor theorem excludes all 684 proper-conductor representatives.
FLINT and PARI/GP agree on all 136 full-conductor norms, with 36 distinct
values. The whole-norm maximum is

```text
4937981356753691307652038461254907642619144628263052811320856547919621259264,
```

and 112 whole norms reach `2^250`. After stripping exact powers of two, the
maximum odd part is

```text
2099233185140600860850973089797376067771315496789913419840767568645748406017.
```

Four vectors, comprising two distinct odd parts, lie in `[2^250,2^251)`.
Exact PARI and FLINT primality tests agree that both are composite. Hence no
prime `p>2^250` divides any residual norm.
