# Cycle 126: quadratic macroscopic pair floor (2026-08-11)

## Cycle pins

```text
our start:       f783ad46f
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
upstream PR:     #1161 open draft
compute:         two local tiny integer verifiers
critical open:   28
```

## The pair floor jumps macroscopically

For a pair union `rho+j`, exact global degree-`e` incidence on the union can
be split between centers on the endpoint codeword line and centers off it.
Linearity gives `jh+d_A<=rho+j-1`; minimum distance bounds every off-line
intersection. Eliminating `h` produces one concave quadratic `F_e(j)`.

It is positive at both endpoints of

```text
4<=j<=rho/2-2,
```

and therefore positive throughout. The complete interval is impossible:

```text
|S_alpha union S_beta|>=3rho/2-1.
```

The official floor is `824633720831`. Every assigned-center line contains
at most three supported slopes; a three-center line has total deficit at
most one. Every pair therefore has at least `rho+1` expanding thirds.

## Burn-down

```text
result:                  REMOVED a macroscopic pair-union band
DAG delta:               +1 PROVED leaf, +1 req edge, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: stronger theorem available for PR #1161 update
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

The next route decision is whether the at-most-three-center geometry and
exact support moments exclude the quadratic packet outright.
