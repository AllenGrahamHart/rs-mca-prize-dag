# Maximum prefix fiber equals one plus maximum local shift-pair degree

- **status:** PROVED
- **closure:** proof

Let `R` be any support-wise first-match residual family of `A`-subsets, and
partition it by the depth-`t` elementary locator-prefix map. Join two distinct
members when they have equal prefix. Then

```text
max_z |R_z| = 1 + max_(S in R) deg_R(S),               (SP-1)
```

with both sides zero by convention if `R` is empty.

If `S,T` are distinct same-prefix supports and

```text
e=|S\T|=|T\S|,
```

then `e>=t+1`. Factoring their common-core locator gives a pair of disjoint
degree-`e` locators whose difference has the required degree drop. At the top
stratum `e=t+1`, that residual locator difference is a nonzero constant.

Consequently the official target

```text
max_z |R_z| <= N^3
```

is equivalent to the uniform local primitive shift-pair bound

```text
deg_R(S) <= N^3-1  for every residual support S.        (SP-2)
```

This is the exact adapter to upstream's primitive shift-pair input. The global
second moment is the sum of these local degrees plus the diagonal; it controls
an average, not `(SP-2)`.
