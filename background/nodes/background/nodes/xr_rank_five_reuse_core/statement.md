# XR rank-five collision-line reuse core

- **status:** see `dag.json` (single source of truth)
- **consumers:** `xr_highcore_collision_count`, `xr_lowcore_spread_heart`
- **dependency:** `xr_rank_five_extension_list_reduction`

Consider the `u=v=0` branch of a RowC rank-five extension list.  From each
selected codeword choose exactly

```text
m=4+h
```

agreement coordinates.  Put

```text
N=R+4,       b=C(m,4),       T=C(N,4),       B=8n^3,
c=b-floor(T/(B+1)).
```

In the high-core application P-A, if the selected slope count exceeds `B`,
then it contains a nonempty subfamily in which every member has at least `c`
distinct four-subsets that occur in another member of the subfamily.  Every
such reused four-subset is an exact size-`k` collision core after restoring
`G`, and the corresponding members lie on one kernel-basis collision line.
The lines through a fixed member are distinct, and each line has the proved
post-strip population cap `floor(R/h)`.

At the three RowC rows this gives:

| rate | `N` | `m` | `b` | `c` | line cap |
|---|---:|---:|---:|---:|---:|
| `1/4` | 772 | 9 | 126 | 125 | 153 |
| `1/8` | 900 | 9 | 126 | 123 | 179 |
| `1/16` | 964 | 7 | 35 | 31 | 320 |

In the low-core application P-B, no four-subset can be reused, so the same
base branch obeys

```text
|P| <= floor(T/b) = 116548571, 215520801, 1021697885,
```

respectively, all strictly below `B=8589934592`.

This pays the P-B `u=v=0` branch and turns the P-A base obstruction into a
near-saturated collision-line core.  It does not bound that core and does not
promote either critical consumer.
