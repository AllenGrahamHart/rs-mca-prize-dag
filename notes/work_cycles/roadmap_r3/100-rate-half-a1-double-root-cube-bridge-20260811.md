# Cycle 100: double-root radical cube bridge (2026-08-11)

## Cycle pins

```text
our start:       3f7dc4b21
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
compute:         none
critical open:   28
```

## Global bridge

Radical division converts the cancelled scalar ambient identity into

```text
(rad(R_a)/s_F)^3=(rad(R_a)^3/R_a)(G_L/H).
```

The retained cubic and quadratic double-root branches are therefore exact
function-field cube problems. Their canonical bounded Picard sections are
the cube roots themselves, so section uniqueness cannot exclude them.

The existing strict-endpoint separated-pullback theorem does not apply: its
scope is the `A=3` endpoint and an equality `f(X)=g(z)`, while the present
cube root is a mixed rational function on `C`. In characteristic three the
identity is not an etale Kummer cover.

## Burn-down

```text
result:                  REDUCED double-root arms to global non-cube target
DAG delta:               +1 PROVED leaf, +3 req edges, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next prove a non-cube theorem using the Hankel/apolar origin of `C`, or find
a countermodel showing that even this global condition is realizable.
