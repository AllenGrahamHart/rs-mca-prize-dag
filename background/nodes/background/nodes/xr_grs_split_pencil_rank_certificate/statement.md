# XR GRS split-pencil rank certificate

- **status:** see `dag.json` (single source of truth)
- **consumers:** `xr_highcore_collision_count`, `xr_lowcore_spread_heart`
- **dependencies:** `xr_rank_five_divided_difference_clique_bridge`,
  `xr_lowcore_u0_v1_grs_defect_reduction`

Let `E` be an `N`-point evaluation set with `N>=4`, let
`K=ev_E(F[X]_<4)`, and
`C=K+<q>` with `q notin K`. Consider a family of distinct colors `gamma_i`
and agreement sets `A_i` for one received word `U`, so that

```text
U-gamma_i q agrees with a cubic on A_i.                 (RC1)
```

For each `A_i`, let `H_i` be any full-row-rank parity-check matrix for cubic
evaluation on `A_i`, extended by zero columns to `E`. Form

```text
M_F = stack_i [ H_i | -gamma_i H_i ],                  (RC2)
```

with the first `N` columns acting on `U` and the last `N` on `q`.

Then

```text
K x K subset ker M_F,
(U,q) in ker M_F \ (K x K),
rank M_F <= 2N-9.                                      (RC3)
```

Consequently, a rank certificate `rank M_F=2N-8` excludes the proposed
support/color family. More exactly, the family requires a nonzero class in
`ker(M_F)/(K x K)` having a representative whose second component is outside
`K`. Classifying all matrices with an extra kernel direction is a sufficient,
possibly coarser route to the remaining coherent split-pencil aggregation.

The global divided-difference coloring also obeys a six-face law. On any
six-set `X={x_1,...,x_6}`, there are constants `a_f,b_f` such that

```text
[X\{x_i}]f=a_f+b_f x_i.                                (RC4)
```

Thus, wherever the denominators are nonzero,

```text
Phi(X\{x_i})=(a_U+b_U x_i)/(a_q+b_q x_i).              (RC5)
```

Among the facets on which the denominator is nonzero, the colors are
therefore either pairwise distinct or all equal. In particular, if all six
colors are defined, they are either pairwise distinct or all equal.
This is an exact rank/Plucker certificate interface. It does not prove the
required aggregate count and does not promote either consumer.
