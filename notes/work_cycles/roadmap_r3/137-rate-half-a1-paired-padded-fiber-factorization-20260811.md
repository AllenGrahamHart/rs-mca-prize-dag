# Cycle 137: rate-half `A=1` paired padded-fiber factorization (2026-08-11)

## Cycle pins

```text
starting source:  66360d01f
canonical prize:  6b337c6d17c63b557b2dd4c489aa938434033c3d
upstream main:    93fba1be3f3299b0ba4708d88715377bbb656e45
compute:          exact integer replay only
critical open:    28
```

## Full zero-excess fibers

For every zero-excess slope, restore the padded-heavy factor instead of
discarding the slope when its deficit is positive. The minimum-word circuit
and the specialized homogeneous locator give the exact identity

```text
G(delta,X)=zeta_delta A_delta(X)R_delta(X).
```

Here `A_delta` is the actual inside-support locator and `R_delta` is the
padded-heavy factor. Their roots are disjoint, and their degrees add to the
full domain degree of the biform. Consequently:

```text
extremal (e-2,p-3): at least 2e full-degree split fibers;
strict   (e-1,p-2): at least p+2 full-degree split fibers.
```

At the official row the counts are `366503875926` and `274877906946`.
The strict padded Forney identity is proved directly from its own minimum RS
word rather than imported by analogy.

## Burn-down

```text
result:                  PROVED paired padded-fiber factorization
DAG delta:               +1 PROVED
critical status delta:   none
terminal delta:          all zero-excess fibers are now usable
delta-star movement:     none
new assumptions:         none
compute requests:        none
```
