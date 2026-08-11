# Cycle 129: quadratic extremal dual split biform (2026-08-11)

## Cycle pins

```text
our start:       uncommitted Cycle-128 tree over 2a7b3c2a2
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
upstream PR:     #1161 open as draft at 09152eb
compute:         tiny arithmetic and F_101 dual-GRS audit
critical open:   28
```

## The minimum-word family has a lower-degree algebraic carrier

For each coordinate of the extremal fixed support, multiply its locator row
by its contracted source form and divide the three center-line roots. The
global Hankel kernel equation puts the resulting vector in a dual GRS code
on `U_0`. Dual interpolation therefore produces one biform

```text
G(t,X),       bidegree (e-2,p-3).
```

This biform splits densely in both directions:

```text
at least 3p-3+d_A domain rows:
    e-2 distinct roots among the 3e off-line supported slopes;

at least e+6+d_A parameter fibers:
    p-3 distinct roots in U_0.
```

At every clean parameter fiber, `G(delta,X)` is not merely split: it is an
explicit nonzero scalar multiple of the inside actual-support locator.

## Burn-down

```text
result:                  REDUCED the extremal branch to an exact
                         bidirectionally split biform census
DAG delta:               +1 PROVED leaf, +1 req edge, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: candidate Lane-T export after route assessment
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

The next decision is structural rather than computational: compare this
exact biform profile against the existing split-pencil/SPI classifiers. A
usable theorem must either exclude its dense two-directional split pattern
or classify it into a form incompatible with the original quadratic
Hankel packet.
