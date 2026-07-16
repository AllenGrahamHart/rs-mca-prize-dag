# XR low-core one-loop GRS defect reduction

- **status:** see `dag.json` (single source of truth)
- **consumer:** `xr_lowcore_spread_heart`
- **dependency:** `xr_rank_five_extension_list_reduction`

Consider the P-B rank-five deficiency pair `(u,v)=(0,1)` at a RowC row, and
put `B=8n^3`. If its selected slope count exceeds `B`, then after deleting
the unique loop coordinate and at most one exceptional selected member there
remain at least `B` codewords in distinct quotient classes of a
one-dimensional extension of `GRS_4`. Their chosen agreement sets have

```text
N=R+4,        m=5+h,        pairwise intersection at most 4.   (D1)
```

For every line threshold `r>=2`, put

```text
d_r=C(m,4)-floor((r-1)C(N,4)/B).                       (D2)
```

Whenever `d_r>0`, this regular family contains a nonempty subfamily in which
every member lies on at least `d_r` collision lines containing at least `r`
retained members. In particular, the `r=2` degrees on the three rates are

```text
209,207,66
```

out of `210,210,70` possible four-sets.

Normalize the kernel as `F[X]_<4`. For every retained member, all fifth
divided differences `[S]q` on its chosen agreement set are nonzero, and

```text
Phi(S)=[S]U/[S]q
```

is constant there with value equal to the member's slope. The collision
directions form a simple four-dimensional star configuration. No nonzero
direction polynomial through degrees

```text
5,5,3
```

vanishes on all `r=2` reused directions.

Optimizing the ratio/minor count over (D2) forces at least

```text
97,650; 52,530; 1,782
```

external vanishing-minor records per retained member. This is an exact
reduction of the `(0,1)` deficiency pair to the coherent split-pencil census.
It does not count that census and does not promote P-B.
