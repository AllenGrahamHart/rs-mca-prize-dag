# Cycle 95: core-free cubic root router (2026-08-11)

## Cycle pins

```text
our start:       87217be41
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
compute:         none
critical open:   28
```

## Low-gap cubic dichotomy

The core-free scalar residual `a=3` has `u+v=e+1`. Exact new-root capacity
shows that `r` simple heavy residual roots require

```text
(3-r)e<=3u+2I_0<=5u,
```

while a triple root requires `2u>=e`. Hence for every integer

```text
0<=u<=36650387592,       5u<e,
```

the residual is either squarefree with all three roots heavy or
double-plus-simple with both roots heavy. No residual root is hidden outside
the heavy set, and the triple-root branch is empty.

## Burn-down

```text
result:                  ROUTED first fifth of cubic gap to 2 patterns
DAG delta:               +1 PROVED leaf, +2 req edges, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next attack the squarefree and double-root vertical ledgers separately.
The simple row has `t_x<=c_x+epsilon_x`; the double row has the opposite
large-new-root pressure and should be handled without importing the simple
congruence.
