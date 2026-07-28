# E1 N=256 E=25 nine-profile exclusion

- **status:** PROVED
- **closure:** complete actual-vector censuses and exact norms

At `N=256`, folded profile `(3,4,0)`, and autocorrelation variance `V=50`,
none of the nine exact profiles

```text
(5,5), (1,6), (4,3,1), (0,4,1), (3,1,2),
(5,1,0,1), (1,2,0,1), (0,0,1,1), (0,0,0,0,1)
```

can occur in a pair-feasible collision.

Folded-chord and direct-negacyclic engines agree row by row after
`2,203,120,896` signed vectors per engine. They find 31,686 vectors in the
nine profiles and 31,280 above the exact cubic cutoff `M_3=13`. Of these,
16,984 have full conductor. The proper-conductor theorem excludes the other
14,296.

FLINT and PARI agree entry by entry on all 16,984 primitive norms. Their
maximum is

```text
689346143769176281255733260656192958605975198224651023251426809106119000068
```

and satisfies

```text
2*N_max < 2^250 < 3*N_max.
```

Thus every primitive exception also misses every pair-feasible row prime.
