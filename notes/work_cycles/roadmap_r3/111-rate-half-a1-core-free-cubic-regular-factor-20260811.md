# Cycle 111: core-free cubic regular-factor pin (2026-08-11)

## Cycle pins

```text
our start:       312f2db39
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
compute:         none
critical open:   28
```

## Supported regular divisor

For every core-free cubic double-root `u=1` packet, let

```text
P_C=product_gamma L_gamma^c_gamma
```

be the complete supported excess-recurrence divisor. Local Smith form and
the exact packet degree give

```text
D_0=a P_C E_w,       deg E_w=w.
```

The four packet values are `w=1,0,0,0`. Thus three packets have completely
factored regular determinant, while the first has only one unlocated linear
factor. Every marked determinant is `a P_C E_w Q(x)`.

## Burn-down

```text
result:                  PINNED three regular determinants exactly, one up to a line
DAG delta:               +1 PROVED leaf, +3 req edges, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next compare the completely supported determinants with the source-minor
and resultant formulas. Separately locate the first packet's linear factor;
do not identify it with the Picard correction without proof.
