# E1 prize N=256 square-mass-18 cofactor-514 exclusion

- **status:** PROVED
- **closure:** dual exhaustive census plus dual exact resultants
- **scope:** prize-envelope `N=256`, profile `(a,b,c)=(4,2,0)`
- **dependency:** `e1_prize_n256_s18_variance_cofactor_windows`

No pair-feasible prize-envelope collision in folded profile `(4,2,0)` has
norm cofactor

```text
m=514=2*257.
```

The variance/cofactor theorem restricts this class to

```text
V in {10,18,26,34,42,50}.
```

After normalizing the two singleton positions to `0,1`, two independent
complete engines exhaust all `320292000` signed vectors. Their exact counts
are:

| `V` | vectors | vectors with `257|Norm` |
|---:|---:|---:|
| 10 | 0 | 0 |
| 18 | 16 | 4 |
| 26 | 8 | 4 |
| 34 | 88 | 48 |
| 42 | 88 | 40 |
| 50 | 232 | 88 |

FLINT and PARI independently agree on all 184 divisor-surviving resultants,
which comprise 46 distinct whole norms. Every quotient `Norm/514` is below
the exact prize lower endpoint. The largest is

```text
66082262884856162162140234757894655654959953149381163882659090799481192796929
```

whereas the prize lower endpoint is

```text
108037839417390090843359763492907651257884484313348964300411102808750191280128.
```

Thus cofactor `514` is impossible. This leaves the four prize cofactors
`{2,4,16,256}` in the leading profile; their residual vectors remain open.
