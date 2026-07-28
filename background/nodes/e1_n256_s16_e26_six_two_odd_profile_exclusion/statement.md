# E1 N=256 E=26 six two-odd profile exclusion

- **status:** PROVED
- **closure:** complete actual-vector censuses and exact norms

At `N=256`, folded profile `(3,4,0)`, and autocorrelation variance `V=52`,
none of the six two-odd profiles

```text
(2,6), (1,4,1), (0,2,2), (2,2,0,1), (1,0,1,1), (1,0,0,0,1)
```

can occur in a pair-feasible collision.

Folded-chord and direct-negacyclic engines agree row by row after
`1,726,770,432` signed vectors per engine. They find 27,380 vectors in the six
profiles and 17,624 above the exact cubic cutoff `M_3=228`. Of these, 8,060
have full conductor. The proper-conductor theorem excludes the other 9,564.

FLINT and PARI agree entry by entry on all 8,060 primitive norms. Their maximum
is

```text
902560312161452055740126650872074695232473707768299835426377069738129096704
```

and satisfies

```text
2*N_max < 2^250 < 3*N_max.
```

Thus every primitive exception also misses every pair-feasible row prime.
