# Cycle 105: core-one source-weight surjectivity fence (2026-08-11)

## Cycle pins

```text
our start:       d9b60b26f
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
compute:         none
critical open:   28
```

## Route fence

Tracing the fixed-core contraction through the RS moment formula gives

```text
omega_x=(x-s_0)v_xa_x,       x in D\{s_0}.
```

This is an invertible diagonal change of arbitrary word values. The
residual domain has `4rho-1` points, while the middle Hankel pair uses only
`2rho-1` moments, so its Vandermonde moment map is onto. Consequently every
endpoint Hankel pair has an RS source representation.

The Cycle-104 subset sum remains useful as an interface, but smooth-domain
source weights alone cannot supply a noncancellation theorem. Closure must
couple it to column-farness, simultaneous supported splitting, the primitive
minimal-index profile, or Forney contact.

## Burn-down

```text
result:                  FENCED source-only noncancellation route
DAG delta:               +1 PROVED leaf, +2 req edges, +1 ev edge
critical status delta:   corrected attack, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next attack the joint condition rather than the source representation:
combine the `e-6` supported roots of `Q(-;x_*)`, the two triple residual
roots, and column-farness of the endpoint pair.
