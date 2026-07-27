# E1 N=256 E=27 six-profile joint exclusion

- **status:** PROVED
- **closure:** complete actual-vector censuses and exact norms

At `N=256`, folded profile `(3,4,0)`, and autocorrelation variance `V=54`,
none of the six profiles

```text
(3,6), (2,4,1), (1,2,2),
(3,2,0,1), (0,0,3), (2,0,1,1)
```

can occur in a pair-feasible collision.

Folded-chord and direct-negacyclic engines agree row by row after
`158,783,488` signed vectors per engine. They find 4,124 vectors in the six
profiles and 2,000 above the exact cubic cutoff `M_3=443`. Of these, 404 have
full conductor. The proper-conductor theorem excludes the other 1,596.

FLINT and PARI agree entry by entry on all 404 primitive norms. Their maximum
is

```text
172876856486553232403068097247779856553359362267270754177943490636016856066
```

and satisfies

```text
10*N_max < 2^250 < 11*N_max.
```

Thus every primitive exception also misses every pair-feasible row prime.
