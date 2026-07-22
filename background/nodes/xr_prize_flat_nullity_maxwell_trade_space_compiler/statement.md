# XR prize flat-nullity Maxwell trade-space compiler

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependencies:** `xr_rs_common_root_basis_charge`,
  `xr_rs_flat_nullity_basis_charge`,
  `xr_prize_flat_nullity_effective_core_floor`,
  `xr_prize_flat_nullity_nonpersistent_root_cap`,
  `xr_prize_u0_loop_defect_maxwell_rank_one_compiler`

Fix any prize P-A flat-nullity cell with affine kernel rank `a` and parameters
`u,v`. Delete the at-most-`v` slopes exceptional at a nonpersistent global
kernel root. After puncturing all global roots, the retained family has a
rank-`a` polynomial kernel

```text
W subset F[X]_{<a+u}
```

with no common evaluation root, on blocks of the exact normalized size and
pair cap

```text
N=R+a+u,       m=a+h+u+v,       kappa=a+u+v.         (GC1)
```

Every over-budget official cell contains a minimal dense core `G`, with
`t=|G|>=3`, union `V`, and

```text
h t=2|V|-2kappa+e,       0<=e<=h-1.                  (GC2)
```

The stacked two-syndrome parity matrix has at least

```text
(u+v)(t-2)+e+1                                          (GC3)
```

independent trades. Every active coordinate of every trade is incident to at
least three active block rows.

Rank-one trades have an exact matroid owner. Their active rows are
`lambda_i=alpha_i lambda`, where the common nonzero dual vector `lambda` is
supported inside every active block and

```text
sum_i alpha_i=sum_i gamma_i alpha_i=0.                (GC4)
```

Choose the lexicographically first circuit `C` in `supp(lambda)` of the
coordinate matroid of `W`. Then

```text
2<=|C|<=a+1,       b|C in W|C,       q|C in W|C.      (GC5)
```

Thus every rank-one trade has a canonical shared local-tangent circuit on
which both received directions already have `W` explanations. If `u=0`, the
matroid is uniform, `|C|=a+1`, and the stronger common-support polynomial
normal form of `xr_prize_u0_loop_defect_maxwell_rank_one_compiler` applies.

This theorem covers the interior and both endpoint chambers of the surviving
flat-nullity wedge. It does not count circuit owners, pay trade rank at least
two, or prove P-A.
