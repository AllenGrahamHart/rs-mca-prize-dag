# Budget-three antipodal pencil degree floor

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:** `rate_half_list_budget_three_antipodal_mobius_weld`,
  `rate_half_list_budget_three_maximal_field_degree_collapse`

Retain the antipodal quotient descent with `d=4s`, `r=s-1`, four distinct
nonzero scalars `a_i`, and four pairwise-coprime monic degree-`r` factors
`G_i` spanning a two-dimensional base-field pencil. In particular,

```text
product_i(Y-a_i^2) product_i G_i(Y)=Y^d-1.             (APD0)
```

Let `V` span the kernel of the leading-coefficient map on that pencil and put

```text
v=deg V <=r-1.
```

Equivalently, for one monic `U` and four distinct constants `c_i`,

```text
G_i=U+c_iV.                                             (APD1)
```

If the base-field characteristic is zero or exceeds `d`, then

```text
v >=ceil((r-4)/2).                                      (APD2)
```

Writing `e_j` for the elementary symmetric functions of the centered
parameters, the intermediate stratum has the stronger bound

```text
e_2=0       ==>       v>=ceil((2r-4)/3).                (APD2')
```

On the maximal official budget-three row,

```text
d=2^39,       r=2^37-1,       v>=2^36-2.               (APD3)
e_2=0         ==>              v>=(2^38-4)/3.           (APD3')
```

Thus the antipodal residual has no constant or low-degree translation
direction. Both independent pencil directions must carry degree on the
official scale. This theorem does not exclude pencils meeting `(APD2)`.
