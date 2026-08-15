# Rank-eleven rank-eight codimension-one circuit-shadow census

- **status:** PROVED
- **residual row:** `K'=11`
- **scope:** one fixed rank-eight nine-coordinate affine-owner chart

Let `V'` be the ten-dimensional residual correction space inside
`RS_{<11}`, and let `B` be a nine-set with

```text
rank(ev_B|V')=8.
```

There is one fixed circuit `C_B subset B`, independent of every
eleven-set extending `B`, with

```text
2<=c:=|C_B|<=9.
```

For every pair of coordinates `x,y` outside `B`, put
`T=B union {x,y}`. Evaluation on `T` has rank ten. Among its 55
nine-subsets, exactly

```text
C(11-c,2)
```

have rank eight; the other `55-C(11-c,2)` have rank nine. A nine-shadow
has rank eight exactly when the omitted pair is disjoint from `C_B`.
Exactly `c` of the eleven ten-subsets of `T` are rank-ten bases.

The circuit also forces the locator ideal

```text
L_(C_B) * RS_{<11-c} <= V',       dimension 11-c.
```

All circuit sizes `c=2,...,9` occur for ten-dimensional hyperplanes with no
evaluation loop, hence satisfy the local linear-algebra assumptions.
Therefore no circuit size can be discarded without retaining additional
global component or chronology information.

## Exact table

```text
c                 2   3   4   5   6   7   8   9
rank-eight        36  28  21  15  10   6   3   1
rank-nine         19  27  34  40  45  49  52  54
rank-ten bases     2   3   4   5   6   7   8   9
locator ideal dim  9   8   7   6   5   4   3   2
```

## Nonclaim

The census does not bound the aggregate number of records, coalesce owner
pairs, assign first-match chronology, pay `K'=11`, move an active-v4 atom,
or close either prize problem.
