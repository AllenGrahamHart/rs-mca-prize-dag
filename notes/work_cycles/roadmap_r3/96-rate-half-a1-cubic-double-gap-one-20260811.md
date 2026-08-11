# Cycle 96: gap-one cubic double-root packets (2026-08-11)

## Cycle pins

```text
our start:       1e0dbdc55
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
compute:         none
critical open:   28
```

## Exact packet ledger

At `u=1`, the double-plus-simple cubic branch has four and only four
rank/contact packets. Three have no ordinary incidence and satisfy

```text
O_C(rho+3,-e-1)=O_C(A),       h^0=1.
```

The fourth has one ordinary triple incidence and satisfies

```text
O_C(rho+3,-e-1)=O_C(A+B-R_0), h^0=0.
```

The proof fixes both row deficits, every extra excess copy, the determinant
gap, all new-root counts, and the complete vertical/contact divisors. It
uses no numerical computation and does not exclude the packets.

## Burn-down

```text
result:                  CLASSIFIED u=1 double-root cubic branch
DAG delta:               +1 PROVED leaf, +2 req edges, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next determine whether the unique ambient scalar form can realize these
degree-one classes, and run the analogous exact ledger for the squarefree
cubic branch.
