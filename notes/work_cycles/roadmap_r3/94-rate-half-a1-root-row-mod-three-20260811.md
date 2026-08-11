# Cycle 94: scalar root-row correction law (2026-08-11)

## Cycle pins

```text
our start:       c3c00af09
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
compute:         none
critical open:   28
```

## Row-summed cube congruence

At every heavy residual-root row, summing the local cube identity over the
complete vertical fibre gives

```text
c_x+epsilon_x-t_x=0 mod 3.
```

Here `c_x` is the row deficit, `t_x` counts distinguished excess roots that
are new relative to the minimal locator, and `epsilon_x` counts extra excess
copies beyond the incidence baseline. Full-overlap deficits `0,1,2 mod 3`
therefore require `0,2,1` correction copies. The result recovers the local
cost behind the closed degree-two packet and exports it to scalar residual
degrees `3,4,5`.

## Burn-down

```text
result:                  STRENGTHENED all scalar root-row rank budgets
DAG delta:               +1 PROVED leaf, +1 req edge, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next combine the correction costs with the residual-root multiplicity and
omission budgets for `a=3,4,5`; do not return to Picard section counting,
whose six-packet information is now exhausted.
