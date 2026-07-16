# XR rank-five ratio/minor dictionary

- **status:** see `dag.json` (single source of truth)
- **consumer:** `xr_highcore_collision_count`
- **dependency:** `xr_rank_five_richline_hierarchy`

Work in the P-A `u=v=0` rank-five branch. After coordinate scaling, write

```text
K_E=ev_E(F[X]_<4),       C_E=K_E+<q>,
```

and let `U` be the received word. Fix a selected codeword `c`, put `z=U-c`,
and choose an `m=4+h` subset `A` of its agreement set. For every four-set
`T subset A`, let `I_T q` be the cubic interpolant to `q` on `T` and put

```text
r_T=q-I_T q.
```

Then:

1. the codewords in `C_E` agreeing with `U` on `T` form exactly the affine
   line `c+lambda r_T`;
2. every other selected member on this line supplies a distinct value
   `lambda` for which the ratio `z(x)/r_T(x)` has a fiber of size at least
   `h` on `E\A`; and
3. for distinct `x,y` outside `A`, equality of those ratios is equivalent to
   a vanishing maximal minor of the global lift matrix with columns

   ```text
   (1,x,x^2,x^3,q(x),U(x)).
   ```

Consequently, if the rich-line core is taken at threshold `r`, every member
has at least

```text
d_r (r-1) C(h,2)
```

distinct external vanishing-minor records `(T,{x,y})`. Optimizing over the
proved hierarchy gives:

| rate | `r` | `d_r` | external vanishing minors per member |
|---|---:|---:|---:|
| `1/4` | 39 | 62 | 23,560 |
| `1/8` | 22 | 60 | 12,600 |
| `1/16` | 5 | 19 | 228 |

This is an exact algebraic reduction of the representability gap. It does not
bound the number of members and does not promote P-A.
