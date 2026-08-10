### 2026-08-10 general-t FPC5 Pade chart

The new PROVED node `l1_fpc5_tpetal_anchor_pade_chart` prints the exact
inverse of the arbitrary-`t` anchor coordinate. With
`I=W^(-1) mod F`, every coordinate `H` reconstructs as

```text
G_H=F+rem_F(-Lambda H I),
B_H=(G_H W+Lambda H)/F.
```

The theorem also gives the exact root-local primitive guard, including the
derivative condition at roots common to `F` and `G_H`. This aligns every
surviving large-source fixed cell with the primitive determinant/remainder
language already available in the rate-half `t=3` LS6 branch.

No critical status changes. The fixed-cell obstruction is now sharply one
split-remainder maximum with printed primitive guards; a dimension-uniform
bound and chronology-valid aggregation remain open.

The identical primitive remainder theorem is exported in upstream PR #1151
at pinned head `bae58ad1ac057e4857947dc7a0c0caff4113ccf4`; the PR remains an open
mergeable draft.
