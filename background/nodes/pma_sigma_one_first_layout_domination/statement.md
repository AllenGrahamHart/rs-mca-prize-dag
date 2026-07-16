# PMA sigma-one first-layout domination

- **status:** PROVED
- **consumer:** `pma_wide_residual`, `petal_mixed_amplification`
- **role:** eliminates the finite paired-core chart multiplier

## Statement

Fix an official finite `sigma=1` word `U` after global profile ownership. Let

```text
C_1 < C_2 < ... < C_A
```

be its ordered paired cores, and let `Anch(C_j)` be the `M=(n-k)/2` planted
listed codewords in the unique maximal source layout over `C_j`. Let `E_Cj`
be the Post codewords whose first non-planted carried layout has core `C_j`,
as in `pma_sigma_one_paired_core_normalization`.

If `A=0`, then `Post(U)` is empty. If `A>0`, then

```text
disjoint_union_(j>=2) E_Cj subset Anch(C_1),

#Post(U) <= #E_C1 + M.                                  (FL1)
```

Indeed, the core-defect reduction applies to every listed codeword which is
not planted in a fixed source layout. Thus a Post codeword not planted in the
first layout is already carried there and cannot first appear later.

Let

```text
B_paid=B_low+B_31+B_30^full
```

be the exact sum of the proved `d<=2`, `(d,r)=(3,1)`, and full-petal
`(d,r)=(3,0)` source payments, evaluated only in the first layout. Let
`R_first(U)` be the remaining unowned Post-compatible non-planted extras in
that layout. Then

```text
#Post(U) <= B_paid(n,k)+M+#R_first(U),                    (FL2)

B_paid(n,k)+M < n^6/1023                                (FL3)
```

on every official row. This removed the paired-core composition obligation
from the former finite target and reduced that target to the one-layout
inequality

```text
#R_first(U) <= B_post-B_paid-M.                          (FL4)
```

The defect-four generic-source obstruction later proves `(FL4)` false. Thus
`(FL1)`--`(FL3)` remain proved structural reductions, while `(FL4)` is a
retired proposed endpoint rather than part of this theorem. The corrected
consumer is the direct polynomial/profile target
`petal_mixed_amplification`.

## Scope

This theorem uses universal non-planted carriage, not merely existence of a
layout-specific auxiliary injection. It does not bound `R_first`, change the
separate asymptotic `GROW union RES` obligation, or turn planted anchors into
primitive Post mass. The `M` term is a safe overcount after global ownership.
