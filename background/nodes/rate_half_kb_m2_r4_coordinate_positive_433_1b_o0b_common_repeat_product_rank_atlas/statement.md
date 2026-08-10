# KoalaBear `433-1b/O0b` repeated-BC product-rank atlas

- **status:** PROVED
- **scope:** five-product-row blocks in all fifteen role cells and two BC signs

For each row, form the `5 x 6` product matrix in coefficient order
`(d_0,d_1,d_2,e_0,e_1,e_2)`. The six signed maximal minors are also its
cofactor kernel. Exact compilation over `F_2130706433` completes all thirty
cell/sign rows in raw and guard-stripped form.

In cells 3 and 6, for both BC signs, maximal-minor columns 1 and 4 become
nonzero constants after division only by source-label differences and the
printed target-open-set guards. Therefore the raw minors are nonzero on the
admissible open set, and the product matrix has rank exactly five there.

No other cell has a guard-only maximal minor. This is not a claim that rank
drop occurs there; their nonconstant rank-drop loci remain to be classified.
No common-rank, outside-row, route, K3, or Prize closure is claimed.

## Falsifier

A missing cell/sign row, incorrect cofactor sign, invalid guard division, or
a guarded rank drop in cell 3 or 6.
