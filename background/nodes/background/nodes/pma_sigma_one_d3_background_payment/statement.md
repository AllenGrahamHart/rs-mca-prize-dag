# PMA sigma-one defect-three background payment

- **status:** PROVED
- **consumer:** `pma_wide_residual`
- **dependencies:** `pma_source_paving_bridge`,
  `pma_sigma_one_low_defect_payment`

## Statement

On an official `sigma=1` maximal sunflower, let `R` be its unique background
point and put `L=n-k`. The complete source class with

```text
d=3, R_P=R
```

has cardinality at most

```text
B_31(n,k)=binom(k-1,3) floor(binom(L,3)/4) < n^6/9216.    (D31)
```

Together with `pma_sigma_one_low_defect_payment`, the complete per-sunflower
class

```text
d<=2, or (d,r)=(3,1)
```

is strictly smaller than `n^6/8192` on every official row.

The bound is field-independent and may be applied after the global periodic
owner by subset.

## Consequence

The first unpaid finite source cell is now `(d,r)=(3,0)`. All higher defects
also remain open, as does first-match composition over maximal-sunflower
charts.

## Scope

This theorem does not pay defect three without the retained background point,
does not give a chart census, and does not address growing reserve.
