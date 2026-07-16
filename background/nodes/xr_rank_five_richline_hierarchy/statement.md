# XR rank-five rich-line hierarchy

- **status:** see `dag.json` (single source of truth)
- **consumer:** `xr_highcore_collision_count`
- **dependency:** `xr_rank_five_reuse_core`

Use the P-A `u=v=0` notation

```text
m=4+h,       N=R+4,       b=C(m,4),
T=C(N,4),    B=8n^3.
```

For every integer line threshold `r>=2`, put

```text
d_r=b-floor((r-1)T/(B+1)).                         (RH)
```

If `d_r>0`, every selected family of more than `B` slopes contains a
nonempty subfamily in which each member lies on at least `d_r` distinct
kernel-basis collision lines, each containing at least `r` members of that
subfamily.

The exact RowC hierarchy includes:

| rate | `d_2` | `d_3` | `d_4` | `d_8` | `d_16` | `d_32` | last positive `r:d_r` |
|---|---:|---:|---:|---:|---:|---:|---:|
| `1/4` | 125 | 123 | 121 | 115 | 101 | 74 | `74:2` |
| `1/8` | 123 | 120 | 117 | 104 | 79 | 28 | `40:3` |
| `1/16` | 31 | 27 | 23 | 6 | 0 | 0 | `9:2` |

Thus the reuse core cannot consist only of two-point lines.  In particular,
one may pass to a nonempty core of minimum 3-rich-line degree
`123,120,27` on the three rows.

This is a hierarchy of necessary structures, not a count of any one core.
It does not promote the P-A consumer.
