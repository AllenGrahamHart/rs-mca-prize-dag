# E1 N=256 E=30 two-odd profile exclusion

- **status:** PROVED
- **closure:** complete computation plus proved conductor split

At `N=256`, folded profile `(3,4,0)`, and autocorrelation variance `V=60`,
neither two-odd magnitude profile `(2,7)` nor `(1,5,1)` can occur in a
pair-feasible collision.

Folded-chord and independent direct-negacyclic engines each census all 87
two-odd light templates and

```text
87*binom(124,3)*64 = 1,726,770,432 representative signed vectors.
```

They agree on

```text
profile    count    full conductor   max M_3   full-conductor max M_3
(2,7)      44,302       28,114         1320              1320
(1,5,1)     7,722        3,572         1344              1068
```

The exact cubic cutoff `M_3=1087` excludes the full-conductor `(1,5,1)`
branch. Two further independent exact-resultant engines enumerate all 28,114
full-conductor `(2,7)` vectors and agree that none reaches `2^250`. Their
global maximum is

```text
N_max = 255193811126065252065353356643030254729479452452701245894186298519499407392,
7*N_max < 2^250 < 8*N_max.
```

The proved proper-conductor theorem excludes both complementary branches.
