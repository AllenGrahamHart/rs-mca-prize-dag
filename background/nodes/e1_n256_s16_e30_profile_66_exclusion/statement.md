# E1 N=256 E=30 profile-(6,6) exclusion

- **status:** PROVED
- **closure:** proof assembly over three exact certificate nodes

At `N=256`, folded profile `(3,4,0)`, and autocorrelation variance `V=60`,
the magnitude profile `(6,6)` cannot occur in a pair-feasible collision.

Two independent odd-difference engines agree on all `1,234` masks and
`44,779,702,968` assignments. They leave `33,737` cubic exceptions on `1,191`
light masks. Two independent actual-vector engines then agree after
`23,638,891,776` vectors per engine, leaving `6,244` exceptions, of which
`1,232` have full conductor. The proper-conductor theorem excludes the other
`5,012`. FLINT and PARI agree on all `1,232` primitive norms. Their maximum is

```text
384340001363476246612319029755636117549080229904040014178244445877664108548
```

and satisfies

```text
4*N_max < 2^250 < 5*N_max.
```

Thus every primitive exception also misses every pair-feasible row prime.
