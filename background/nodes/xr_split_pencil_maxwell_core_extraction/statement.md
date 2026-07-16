# XR split-pencil Maxwell-core extraction

- **status:** see `dag.json` (single source of truth)
- **consumers:** `xr_highcore_collision_count`, `xr_lowcore_spread_heart`
- **dependency:** `xr_grs_split_pencil_rank_certificate`

Let `F` be a genuine coherent `GRS_4` split-pencil family on an `N`-point
domain. Every block `A_i` has size `m=4+c`, where `c>=1`, and supplies `c`
independent cubic parity rows. Suppose

```text
c |F| >= 2N-8.                                         (MC1)
```

Then `F` contains an inclusion-minimal nonempty subfamily `G` such that,
writing

```text
L=|G|,       V=union_(A in G) A,       v=|V|,
e=cL-(2v-8),
```

one has

```text
0 <= e <= c-1,
c|J| <= 2|union J|-9             for every proper J subset G,
L <= floor((2N+c-9)/c).                            (MC2)
```

If `u_A` is the number of coordinates occurring only in a block `A` inside
`G`, then

```text
e+2u_A <= c-1.                                      (MC3)
```

Let `M_G` be the stacked matrix `[H_i|-gamma_i H_i]`, restricted to `V`.
The genuine split pencil gives

```text
rank M_G <= 2v-9,
dim leftker(M_G) >= e+1.                            (MC4)
```

Only `e` left-kernel dimensions are forced by ordinary row overdetermination
relative to the eight-dimensional cubic-pair kernel. Thus `G` has at least
one anomalous dependence. It is a bounded, proper-subfamily-sparse circuit
target for the split-pencil census.

At the three P-A RowC base branches, `(N,m,c)=(772,9,5),(900,9,5),
(964,7,3)`, so `L<=308,359,640`, and every block has at most `2,2,1`
private coordinates. At the P-B one-loop branches,
`(N,m,c)=(772,10,6),(900,10,6),(964,8,4)`, so
`L<=256,299,480`, with the same private-coordinate caps `2,2,1`.

This extraction does not classify the anomalous circuits and does not
promote either consumer.
