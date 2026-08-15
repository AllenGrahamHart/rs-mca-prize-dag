# Rank-stratified isolated-incidence cap

- **status:** PROVED
- **correction dimension:** `10`
- **tuple size:** `11`
- **isolated records per tuple:** at most `1`

Retain the normalized rank-eleven dense-locator setup.  For every residual
coordinate `x`, write its equation as

```text
a_x+Z b_x+q(Z) ev_x(R)=0,       R in V',              (SI1)
```

where `dim V'=10`, `deg q=18`, and every retained record slope avoids the
roots of `q`.

For one fixed eleven-set `T`, at most one retained record point is isolated
in the intersection of the equations `(SI1)` for `x in T`.  Hence, if `N`
records have exact support size `m'` in a residual domain of size `n'`, the
number of incidences lying on a positive-dimensional component is at least

```text
N C(m',11)-C(n',11).                                  (SI2)
```

This replaces the generic `198 C(n',11)` isolated-incidence allowance by
`C(n',11)` for actual retained record points.

## Falsifier

Two distinct retained slopes isolated on the same eleven-set; an evaluation-
rank-at-most-nine record point without a kernel line through it; a rank-ten
system whose residual equation has slope degree above one after eliminating
`R`; or use of the result at a root of `q`.
