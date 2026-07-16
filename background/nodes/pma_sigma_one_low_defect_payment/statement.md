# PMA sigma-one source-pinned low-defect payment

- **status:** PROVED
- **consumer:** `pma_wide_residual`
- **dependencies:** `pma_aux_list_reduction`, `pma_source_paving_bridge`,
  `pma_sigma_one_b11_scope`

## Statement

On an official `sigma=1` maximal-sunflower source, put

```text
L=n-k, M=L/2, b=1.
```

After summing over every missed-core set `D`, both possible exact background
agreement sets, and all source-admissible auxiliary polynomials with core
defect `d<=2`, the number of non-planted extras is at most

```text
B_low(n,k)
 = (k-1) [ M + floor(binom(L,2)/3) ]
   + binom(k-1,2)
       [ floor(binom(L,2)/3) + floor(binom(L,3)/4) ].       (L1)
```

For every official row `n=2^s`, `13<=s<=44`, at all four clean rates,

```text
B_low(n,k) < n^5/1024.                                    (L2)
```

The bound is independent of the generated-field size and the petal scalars.
It includes exact-periodic members, so it remains valid after the global
exact-periodic first-match owner removes them.

## Consequence

The finite `sigma=1` branch no longer needs the failed ambient
`11 binom(M,2)q^4` certificate for its realized `d<=2` cells. Per maximal
sunflower, those cells have a field-independent source payment below
`n^5/1024`. The remaining finite source residual is `GROW={d>=3}`. Global chart
composition and the exact unborrowed mixed-branch allowance remain open.

## Scope

This is a per-maximal-sunflower source theorem. It does not bound the number
of sunflower charts needed for an arbitrary received word, pay `d>=3`, or
replace the general B11 router at growing reserve.
