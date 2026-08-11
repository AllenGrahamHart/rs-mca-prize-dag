# Cycle 98: core-one quadratic gap-four normal forms (2026-08-11)

## Cycle pins

```text
our start:       164fbeafd
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
upstream PRs:    39 open; no new scalar-contact result
compute:         none
critical open:   28
```

## Minimum-gap classification

The core-one scalar quadratic satisfies `u+v=e+2`, hence begins at `u=4`.
At that gap omission is zero, so the excess factor is squarefree and
disjoint from the minimal locator. Ordinary incidences and excess roots away
from the residual-root rows are impossible by the unit-residual cube law.

Exactly two patterns remain:

```text
DOUBLE: deficit 6, effective degree-two class B, h^0(B)=1;
SPLIT:  deficits (e+3)/2,(e+9)/2, corrections 3,9.
```

The split contact complement has degree `e+2`; the double class has only its
canonical reduced-root quotient section. Thus neither is excluded, but the
complete minimum-gap chamber is now explicit.

## Burn-down

```text
result:                  CLASSIFIED core-one quadratic u=4
DAG delta:               +1 PROVED leaf, +2 req edges, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next seek a global ambient/recurrence constraint on the canonical double
class, or extend the omission-sensitive root router to `u>=5`.
