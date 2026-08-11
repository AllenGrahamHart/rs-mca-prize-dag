# Cycle 89: core-free scalar residual degree two closes (2026-08-11)

## Cycle pins

```text
our start:       50b49d7e2
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
compute:         none
critical open:   28
```

## Full omission and cube congruence

Both packets have `O=Delta`, hence every excess degree produces omission
and every distinguished excess root overlaps `Q_min`. On a deficit-one row,
the ordinary local pattern has horizontal multiplicity two and vertical
multiplicity `1 mod 3`. The `e-1` supported roots and any unsupported roots
therefore give total degree `e-1 mod 3`, not the official `e=0 mod 3`.

The only possible repair in the packet with an unallocated determinant root
raises one horizontal multiplicity to three. Its vertical multiplicity is
then at least three, and the minimum total becomes `e+1`. The packet with an
ordinary triple incidence has no unallocated determinant root. Both are
empty.

The proved leaf is
`rate_half_ca_hankel_a1_first_degree_core_free_degree_two_packet_exclusion`.

## Burn-down

```text
result:                  CLOSED core-free scalar residual degree two
DAG delta:               +1 PROVED leaf, +2 req edges, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

The core-free scalar range is now `a in {3,4,5}`. Continue the six bounded
core-one degree-one packets and derive analogous structure for those three
core-free degrees.
