# Cycle 106: quadratic gap-four incidence-center spread (2026-08-11)

## Cycle pins

```text
our start:       453cd35d8
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
compute:         none
critical open:   28
```

## Joint incidence/coding bridge

The `u=4` double-root packet has an exact locator block design:

```text
blocks:              rho+4, each of size rho;
fixed core:          one point of degree rho+4;
light rows:          3rho+5 points of degree e;
double heavy row:    one point of degree e-6;
inactive heavy rows: rho-7 points of degree zero.
```

RS minimum distance `2rho+1` makes each radius-`rho` center unique. The
`e-6` deficient slopes have actual error weight `rho-1`; all others have
weight `rho`. Column-farness therefore bounds a center line containing `r`
deficient slopes by `rho+1-r` assigned centers. A pair of locator blocks has
at least three, four, or five third blocks whose triple union has size at
least `2rho+1`, according as the pair contains zero, one, or two deficient
slopes.

## Burn-down

```text
result:                  COUPLED exact design to column-far center spread
DAG delta:               +1 PROVED leaf, +2 req edges, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next test whether the printed degree sequence can satisfy the uniform
three-expander condition, or sharpen the line cap by charging specialized
rank-loss deficits to the actual error weights.
