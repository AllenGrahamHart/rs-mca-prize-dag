# Cycle 122: quadratic oriented-gcd coupling (2026-08-11)

## Cycle pins

```text
our start:       6b6ae27f7
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
compute:         two local tiny integer verifiers
critical open:   28
```

## Every minimum pair has a large gcd

The source slope is outside every oriented row-root set, sharpening the
single-orientation capacity by one. More importantly, at zero endpoint
deficit the forward and reverse gcds exchange `alpha,beta` and share all
other roots. A forward residual root cannot also be a reverse residual root:
that would put the slope on the endpoint center pencil, where it must contain
all forward and reverse difference points. Therefore six residual root sets
are disjoint and

```text
g+1+6(e-g)<=3e+3,       5g>=3e-2.
```

Together with the positive-deficit capacity bounds, every `rho+3` pair has
a center-owned common divisor of degree at least about `0.6e`, `e/3`, or
`e/2` according as its maximum endpoint deficit is zero, one, or two.

## Burn-down

```text
result:                  FORCED a linear gcd in every rho+3 pair case
DAG delta:               +1 PROVED leaf, +2 req edges, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next compare this center-owned gcd with the heavy-row factors
`g_*S_B^3` or `G_i^2S_i^3`, and with the reverse-oriented coefficient
pencil. A large gcd is structural progress but not itself a contradiction.
