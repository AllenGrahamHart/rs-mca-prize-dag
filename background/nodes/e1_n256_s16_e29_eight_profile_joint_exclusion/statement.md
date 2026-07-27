# E1 N=256 E=29 eight-profile joint exclusion

- **status:** PROVED
- **closure:** complete actual-vector censuses and exact norms

At `N=256`, folded profile `(3,4,0)`, and autocorrelation variance `V=58`,
none of the eight profiles

```text
(5,6), (1,7), (4,4,1), (0,5,1),
(3,2,2), (5,2,0,1), (2,0,3), (1,3,0,1)
```

can occur in a pair-feasible collision.

Folded-chord and direct-negacyclic engines agree row by row after
`2,203,120,896` signed vectors per engine. They find 61,408 vectors in the
eight profiles and 4,812 above the exact cubic cutoff `M_3=872`. Of these,
820 have full conductor. The proper-conductor theorem excludes the other
3,992 vectors.

FLINT and PARI agree entry by entry on all 820 primitive norms. Their maximum
is

```text
186828941137106397532470537651505306486275228904728704307636700572095315972
```

and satisfies

```text
9*N_max < 2^250 < 10*N_max.
```

Thus every primitive exception also misses every pair-feasible row prime.
