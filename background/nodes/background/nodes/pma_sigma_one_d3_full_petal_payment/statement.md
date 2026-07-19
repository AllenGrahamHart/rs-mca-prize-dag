# PMA sigma-one defect-three full-petal payment

- **status:** PROVED
- **consumer:** `pma_wide_residual`
- **dependencies:** `pma_source_paving_bridge`,
  `pma_sigma_one_low_defect_payment`,
  `pma_sigma_one_d3_background_payment`

## Statement

On an official `sigma=1` maximal sunflower, put `L=n-k` and `M=L/2`.
The complete source class with

```text
(d,r)=(3,0)
```

and at least one full two-point petal has cardinality at most

```text
B_30^full(n,k)
 = binom(k-1,3) M binom(L-2,2)
 < n^6/1536.                                           (D30F)
```

Together with the previous finite source payments, the complete per-sunflower
class

```text
d<=2;
or (d,r)=(3,1);
or (d,r)=(3,0) with a full petal
```

is strictly smaller than `n^6/1024` on every official row.

## Consequence

The exact defect-three finite remainder is the diffuse class

```text
(d,r)=(3,0),
at most one agreement in each petal,
at least five touched petals.
```

All defects `d>=4` remain open. This node does not remove first-match chart
composition; `pma_sigma_one_first_layout_domination` does so later.

## Scope

The theorem is per maximal sunflower. It neither pays the diffuse class nor
proves that the diffuse ambient `n^7` charge is attained on an official row.
