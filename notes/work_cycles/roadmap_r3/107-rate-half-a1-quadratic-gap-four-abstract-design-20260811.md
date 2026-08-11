# Cycle 107: quadratic gap-four abstract incidence design (2026-08-11)

## Cycle pins

```text
our start:       8c55f916d
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
compute:         local tiny, bounded toy set systems only
critical open:   28
```

## Support-only route fence

A balanced seven-mark word on `3e+3` cyclic starts gives an explicit
abstract realization of the exact Cycle-106 degree sequence for every
`e>=7`. Three light rows begin at every start except the seven marked ones,
where two begin; each row occupies `e` consecutive blocks. Every block has
`3e-2` or `3e-3` light points, and exactly `e-6` have the smaller size.
Adding `x_*` to those blocks and the core point to all blocks completes the
design.

The exact degree sequence is therefore consistent. A bounded probe for
`7<=e<=30` also found that every pair satisfies the Cycle-106 support spread,
with minimum `e+3` expanders. That spread observation remains numerical, not
a theorem or an RS realization.

## Burn-down

```text
result:                  FENCED degree-only contradiction route
DAG delta:               +1 PROVED leaf, +1 req edge, +1 ev edge
critical status delta:   corrected attack, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next use field-valued nearest-error/center consistency, the Hankel cube gate,
or Forney weights. Further support-degree counting is not a closing route.
