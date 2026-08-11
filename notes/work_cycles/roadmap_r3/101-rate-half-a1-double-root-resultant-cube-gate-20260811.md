# Cycle 101: double-root resultant cube gate (2026-08-11)

## Cycle pins

```text
our start:       d582111fd
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
compute:         none
critical open:   28
```

## Exact norm test

The global cube bridge has the necessary univariate consequence

```text
Res_X(Q,P)/(q_d^deg(P) H^d)=Norm(W)^3 in F(z).
```

The norm is taken from the finite reduced total-quotient algebra, so no
irreducibility of `C` is assumed. In characteristic different from three,
the quotient is tested by factor valuations and its constant cube class. In
characteristic three, it is a cube exactly when its derivative vanishes.

This is a branch-killing test once an actual or symbolic candidate `Q` is
available. Passing the norm test is not sufficient for recurrence
realization or for the cube root to exist componentwise.

## Burn-down

```text
result:                  REDUCED global cube to exact resultant falsifier
DAG delta:               +1 PROVED leaf, +1 req edge, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next derive the resultant quotient from the bounded residual and light-row
factorizations, or use a small exact recurrence model to test whether the
gate can fail.
