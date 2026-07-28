# E1 low-square-mass Plotkin coloring compiler

- **status:** PROVED
- **closure:** proof plus exact integer ledger
- **dependencies:** `acl_count`, `e1_clean_anchor_exact_collision_allowance`,
  `e1_collision_square_mass_reparametrization`
- **open consumer:** `e1_official_low_square_mass_collision_coloring`

Fix one pair-feasible prime-field E1 row with class set `X_ell`. For classes
`x,y in X_ell`, put

```text
S(x,y)=sum_i (x_i-y_i)^2.
```

Define the low-square-mass collision graph `G_p(ell)` on `X_ell`: distinct
vertices are adjacent exactly when they have the same reduced E1 value and
`S(x,y)<=2ell`.

If `G_p(ell)` is properly colorable with `c` colors, every reduced E1 fiber
has size at most

```text
R_max <= c(ell+1).
```

Consequently its reduced E1 image has size at least

```text
L >= ceil(K/(c(ell+1))),       K=|X_ell|.
```

For each named envelope, define the largest admissible color count

```text
c_max=floor((K-1)/(B*(ell+1))).
```

The exact ledger is:

| row | `ell` | `c_max` | fiber cap `c_max(ell+1)` | certified image floor |
|---|---:|---:|---:|---:|
| RowC `1/4` | 65 | 3268165922105543787 | 215698950858965889942 | 5316911983139663491945071196031276118 |
| RowC `1/8` | 33 | 210 | 7140 | 5322314010682671613516194952413711990 |
| RowC `1/16` | 33 | 18885148505476 | 642095049186184 | 5316911983139880370678024748494484621 |
| prize `1/4` | 65 | 54730211038721500 | 3612193928555619000 | 317494674775468776604028242834763517703 |
| prize `1/8` | 33 | 3 | 102 | 372561980747787012946133646668959839245 |
| prize `1/16` | 33 | 316259390691 | 10752819283494 | 317494674775514892450411471699202449213 |

Every printed image floor is strictly greater than that row's `B*`. Thus the
row-specific coloring bounds `chi(G_p(ell))<=c_max` suffice for a direct E1
unsafe payload, without proving injectivity or the stronger collision-pair
allowance. The binding new premise is the prize rate-`1/8` bound
`chi(G_p(33))<=3`. This node proves the compiler, not those coloring bounds.
