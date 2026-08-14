# Cycle 319: MCA rank-11 rank-9 split-pencil cell ledger (2026-08-14)

The new PROVED node
`rate_half_mca_rank11_rank9_split_pencil_cell_ledger` classifies and pays the
incidence capacity of one fixed rank-nine ten-coordinate cell.

All pair owners agreeing with the received pair on the cell form an affine
plane. A record of slope `gamma` is a line of direction
`(-gamma*u,u)`. Distinct lines intersect once, so owner blocks satisfy

```text
sum_p C(t_p,2)=C(g,2).
```

On the kernel zero set all owner points coincide, producing one common core
`J_B`. Outside it, each coordinate determines one owner point, so owner
petals are pairwise disjoint. The component-star theorem supplies at least
45153 petal-extension incidences per record. A fixed owner carries at most
981105 slopes, and at most `2097152-10` petal coordinates exist. Hence

```text
45153*g<=981105*(2097152-10),
g<=floor(2057516501910/45153)=45567658.
```

The original cycle print used the valid but weaker ceiling `45567659`.
The upstream export audit caught the one-unit sharpening: the integer
record count is bounded by the floor.

This is a cell cap, not a cell census. A macroscopic rank-nine lane must
spread across many distinct cells.

Focused verification:

```text
RATE_HALF_MCA_RANK11_RANK9_SPLIT_PENCIL_CELL_LEDGER_PASS
  weighted=2057516501910 cell=45567658 controls=8/8
RATE_HALF_MCA_RANK11_RANK9_SPLIT_PENCIL_CELL_LEDGER_AUDIT_PASS
  weighted=2057516501910 cell=45567658 controls=6/6
```

No Modal computation was used.

```text
start:                   20eb40d59
DAG delta:               +1 PROVED fixed-cell split-pencil ledger,
                         +1 requirement edge, +1 evidence edge
critical status delta:   none
upstream terminal delta: exact base-field-normalized split-pencil ledger
                         and cap inside one rank-nine cell
delta-star movement:     none
compute:                 constant-size exact incidence arithmetic only
next route action:       bound or compress the number of rank-nine cells,
                         or aggregate the large-owner/kernel-plane lanes
```
