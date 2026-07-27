# E1 N=256 E=26 four six-odd profile exclusion

- **status:** PROVED
- **closure:** complete actual-vector censuses and exact norms

At `N=256`, folded profile `(3,4,0)`, and autocorrelation variance `V=52`,
none of the four six-odd profiles

```text
(6,5), (5,3,1), (4,1,2), (6,1,0,1)
```

can occur in a pair-feasible collision.

Folded-chord and direct-negacyclic engines agree row by row after
`24,492,353,024` signed vectors per engine. They find 78,848 vectors in the
four profiles and 74,614 above the exact cubic cutoff `M_3=228`. Of these,
45,408 have full conductor. The proper-conductor theorem excludes the other
29,206.

FLINT and PARI agree entry by entry on all 45,408 primitive norms. Their
maximum is

```text
1139098407599461804511111865916270680930143333943822578584573946997885235216
```

and satisfies

```text
N_max < 2^250 < 2*N_max.
```

Thus every primitive exception also misses every pair-feasible row prime.
