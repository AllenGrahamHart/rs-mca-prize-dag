# RS flat-nullity basis charge

- **status:** see `dag.json` (single source of truth)
- **consumers:** `xr_highcore_collision_count`, `xr_lowcore_spread_heart`
- **dependency:** `xr_rs_common_root_basis_charge`

Use the notation and hypotheses of the RS common-root weighted basis charge.
Put

```text
g=|G|,       p=|P_0|,
u=k-a-g,     v=g-p,
L=floor((n-kappa)/(k+h-kappa)).
```

Thus `u,v>=0` and `u+v<=k-a`. For a selected error `e`, delete the global
loop coordinates from the coordinate matroid of `K|Z_e`, and let `m_e` be
the remaining ground-set size. Every proper flat `F` of rank `j<a` satisfies

```text
|F| <= j+u.                                             (FN1)
```

Consequently, if `b_e` is the number of kernel-coordinate bases in `Z_e`,

```text
a b_e >= m_e C(m_e-u-1,a-1).                           (FN2)
```

Define

```text
W_u(m)=m C(m-u-1,a-1),
m_0=a+h+u+v,       m_*=a+h+u.
```

Then the selected slope count obeys

```text
|P| <= max{
  v,
  floor(
    (a L C(R+a+u,a) + v(W_u(m_0)-W_u(m_*))) / W_u(m_0)
  )
}.                                                       (FN3)
```

There is also an independent persistent-root packing bound. Put

```text
t=kappa-p+1.
```

Then

```text
|P| C(k+h-p,t) <= C(n-p,t).                             (FN4)
```

At selector rank five on the three RowC rows, combining `(FN3)` and `(FN4)`
leaves only the following integer parameter pairs capable of exceeding the
`8n^3` allocation:

| row | all `(u,v)` | P-A residual | P-B residual | max `u` P-A/P-B | max `v` P-A/P-B |
| --- | ---: | ---: | ---: | ---: | ---: |
| rate `1/4` | 32,131 | 14 | 8 | `10 / 7` | `1 / 1` |
| rate `1/8` | 7,875 | 70 | 49 | `38 / 29` | `3 / 2` |
| rate `1/16` | 1,891 | 323 | 274 | `60 / 60` | `7 / 6` |

This is a proved structural reduction, not a rank payment. In particular it
does not close either XR target or change the first open selector ranks.
