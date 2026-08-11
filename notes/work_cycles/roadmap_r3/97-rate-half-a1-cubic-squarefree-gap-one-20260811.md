# Cycle 97: gap-one cubic squarefree correction row (2026-08-11)

## Cycle pins

```text
our start:       254bac85f
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
compute:         none
critical open:   28
```

## Route decision

The degree-one section in each no-ordinary double-root packet is exactly the
reduced two-root divisor divided by the contact section. It is compatible
with ambient uniqueness rather than independent of it. The ordinary packet
gives the same rational quotient with its predicted pole at `R_0`. Thus
section uniqueness alone cannot exclude those four packets.

## Squarefree normal form

In the squarefree `u=1` branch, the three simple-row correction quantities
are nonnegative multiples of three whose sum is three. Exactly one root row
is therefore corrected. Its complete vertical/contact divisor belongs to
one of three printed forms, according as the sole augmented incidence is
absent, new, or overlapping.

The resulting Picard class has degree `e+1`. This prevents accidental reuse
of the bounded-degree double-root argument and leaves a clear next target:
a global constraint linking the unique corrected row to the scalar ambient
cubic.

## Burn-down

```text
result:                  CLASSIFIED squarefree u=1 correction row
DAG delta:               +1 PROVED leaf, +2 req edges, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```
