# E1 N=256 E=28 eight-profile joint exclusion

- **status:** PROVED
- **closure:** complete actual-vector censuses and exact norms

At `N=256`, folded profile `(3,4,0)`, and autocorrelation variance `V=56`,
none of the eight profiles

```text
(4,6), (0,7), (3,4,1), (2,2,2),
(4,2,0,1), (1,0,3), (0,3,0,1), (3,0,1,1)
```

can occur in a pair-feasible collision.

Folded-chord and direct-negacyclic engines agree row by row after
`3,056,582,144` signed vectors per engine. They find 48,716 vectors in the
eight profiles and 12,638 above the exact cubic cutoff `M_3=658`. Of these,
4,372 have full conductor. The proper-conductor theorem excludes the other
8,266 vectors.

FLINT and PARI agree entry by entry on all 4,372 primitive norms. Their
maximum is

```text
296015175952529502165108365809577184284217843110959136601469787066321741314
```

and satisfies

```text
6*N_max < 2^250 < 7*N_max.
```

Thus every primitive exception also misses every pair-feasible row prime.
