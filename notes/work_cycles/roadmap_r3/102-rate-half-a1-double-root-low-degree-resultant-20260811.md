# Cycle 102: double-root low-degree resultant factorization (2026-08-11)

## Cycle pins

```text
our start:       a73604a65
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
compute:         none
critical open:   28
```

## Bounded resultant target

The line-bundle norms of the classified cube roots sharpen the generic
rational-cube gate to exact factorizations:

```text
cubic, no ordinary: Res=c^3 H^rho times a linear cube;
cubic, ordinary:    Res=c^3 L_0^(rho-3)(H/L_0)^rho times a quadratic cube;
quadratic double:   Res=c^3 H^(rho-1) times a quadratic cube.
```

The leading `X` coefficient cancels because `deg P=3a` in each branch. The
linear and quadratic forms are parameter pushforwards of the already proved
contact-complement divisors, so they are outputs rather than new search
variables.

## Burn-down

```text
result:                  REDUCED resultant residual to degree 1 or 2
DAG delta:               +1 PROVED leaf, +3 req edges, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next compare these factorizations with a second resultant formula from the
Hankel recurrence or reconstruct the residual form from boundary data.
