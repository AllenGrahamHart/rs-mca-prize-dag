# XR prize P-A cells have an effective-core floor

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependencies:** `xr_rs_flat_nullity_basis_charge`,
  `xr_rs_common_root_basis_charge`, `xr_target_budget_audit`

Use a prize-row P-A flat-nullity cell with affine kernel rank `a` and
parameters `u,v`. Put

```text
kappa=a+u+v,       N=R+kappa,
L=floor((2R+h-1)/h).                                (EF1)
```

After deleting the persistent common-root set `P_0`, every selected zero set
has at least `kappa+h` points and two selected zero sets intersect in at most
`kappa` points. If the cell contains more than `8n^3` slopes, then

```text
kappa>=K_eff(h,L):=ceil((h+1)/(2(L-2))).             (EF2)
```

The exact prize values are:

| rate | `h` | `L` | necessary effective core `kappa=a+u+v` |
|---|---:|---:|---:|
| `1/4` | `2^33+1` | `384` | `11,243,370` |
| `1/8` | `2^33+1` | `448` | `9,629,972` |
| `1/16` | `2^32+1` | `960` | `2,241,633` |

At the first open selector ranks, respectively `a=16,16,14`, every surviving
P-A cell therefore satisfies

```text
u+v>=11,243,354;       9,629,956;       2,241,619.  (EF3)
```

This theorem includes the uniform-cell exclusion as the special case
`u=v=0`, but its main content is nonuniform: bounded-flat-nullity prize cells
cannot be P-A counterexamples at any low selector rank.

The theorem does not count cells above the effective-core floor, control
P-B, pay cross-cell aggregation, or prove P-A. The boundary values are
necessary conditions, not existence claims.
