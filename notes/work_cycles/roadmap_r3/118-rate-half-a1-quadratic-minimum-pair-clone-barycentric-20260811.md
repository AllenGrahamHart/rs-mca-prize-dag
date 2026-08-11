# Cycle 118: quadratic minimum-pair clone-barycentric gate (2026-08-11)

## Cycle pins

```text
our start:       7b3483fb6
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
upstream PRs:    refreshed through #1160; #1148/#1156 do not port
compute:         local tiny verifier only
critical open:   28
```

## Sharp boundary

At pair union `rho+2`, each one-sided support difference is a clone class of
size `r+2`. Its row forms share the same squarefree degree-`e` supported
slope divisor, and the endpoint error values are uniquely barycentric after
including the core contraction and RS dual multipliers.

This converts the extremal support case into a field-valued comparison with
the Forney numerator. It neither asserts that a sharp pair exists nor pays
larger pair unions.

## Burn-down

```text
result:                  EXPOSED exact clone/error boundary data
DAG delta:               +1 PROVED leaf, +2 req edges, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```
