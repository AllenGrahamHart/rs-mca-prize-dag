# Proof of the conditional implication

The width pin partitions the established F-4 minimal-record ledger into
disjoint width strata from 2 through
`H_max=min(k+t,floor(n/2))`.  Add the harmless width-1 term supplied by
`f3_h1_singleton_injectivity`.

The proved h=2 theorem gives `R_2^min<n^3`.  The h=3 conditional close gives
`R_3^min<n^3` under its named premise.  The h>=4 aggregate theorem gives

```text
sum_(h=4)^H_max R_h^min <= 14n^3
```

under its named norm-gate premise.  Therefore

```text
R_min < 0+n^3+n^3+14n^3 = 16n^3.
```

At least the h=2 and h=3 inequalities are strict, so the final inequality is
strict.  No step identifies a general order-`t` record with an F-4 minimal
record; that is outside this implication.
