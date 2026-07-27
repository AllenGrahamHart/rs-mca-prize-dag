# E1 N=256 E=31 three-profile joint exclusion

- **status:** PROVED
- **closure:** complete computation plus proved conductor split

At `N=256`, folded profile `(3,4,0)`, and autocorrelation variance
`V=62`, none of the three residual magnitude profiles

```text
(3,7), (2,5,1), (1,3,2)
```

can occur in a pair-feasible collision.

Two independent exact engines census all eight light-support templates, all
`binom(124,3)` heavy supports per template, and all 64 relative sign vectors:

```text
8*binom(124,3)*64 = 158,783,488 representative signed vectors.
```

They agree on the following complete ledger:

```text
profile    count   full conductor   max M_3   full-conductor max M_3
(3,7)       7204       3856           1380              1206
(2,5,1)     1590        472           1068              1062
(1,3,2)      388         84           1122               714
```

The exact cubic cutoff is `M_3=1302`. Thus `(2,5,1)` and `(1,3,2)` are
excluded without a conductor split, while the full-conductor part of `(3,7)`
is also excluded. The proved proper-conductor theorem excludes its complement.
