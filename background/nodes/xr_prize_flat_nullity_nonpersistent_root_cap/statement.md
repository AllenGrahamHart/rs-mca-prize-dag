# XR prize flat-nullity nonpersistent-root cap

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependencies:** `xr_rs_flat_nullity_basis_charge`,
  `xr_prize_flat_nullity_effective_core_floor`, `xr_target_budget_audit`

Use a prize-row P-A flat-nullity cell with affine kernel rank `a` and
parameters `u,v`, where `v=|G|-|P_0|` is the number of global kernel roots
that are not persistent on the affine family. Put

```text
R=n-k,       L=floor(R/h),       B=8n^3,       c=a+h.
```

For fixed `v`, the real envelope underlying `(FN3)` is convex in `u` on
`0<=u<=k-a-v`. Consequently its maximum occurs at one of

```text
u=0,       u=k-a-v.                                  (NC1)
```

At the first open affine ranks, every cell with more than `B` selected
slopes satisfies the following necessary bounds:

| rate | `a` | effective core `a+u+v` | nonpersistent roots `v` |
|---|---:|---:|---:|
| `1/4` | `16` | `>=11,243,370` | `<=1,526,176,110` |
| `1/8` | `16` | `>=9,629,972` | `<=2,902,067,939` |
| `1/16` | `14` | `>=2,241,633` | `<=1,962,285,106` |

Equivalently, `(u,v)` lies above the effective-core diagonal and below the
printed `v` ceiling. The ceiling is respectively about `0.278%`, `1.056%`,
and `1.428%` of `k`.

This is a parameter-space reduction, not a P-A close. It does not count the
remaining low-`v` cells, control P-B, or aggregate slopes across cells.
