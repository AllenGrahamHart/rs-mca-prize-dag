# HGE4 near-third dual-gap exclusion

- **status:** PROVED
- **consumer:** `f3_hge4_norm_gate_count`
- **dependency:** `f3_hge4_near_third_belyi_necklace_bound`

Let `m=3h+e` be dyadic, with `0<e<h`, and work in characteristic zero or
characteristic `p>4h+e`. If

```text
h>=2e+1,                                             (DGE1)
```

then there is no primitive ordered non-full exact-level shift pair. Thus

```text
E_h^prim(m,p)=0.                                    (DGE2)
```

Equivalently, every live exact-level width satisfies

```text
7h<=2m,
4<=h<=floor(2m/7).                                 (DGE3)
```

This is a zero-cost analytic exclusion. In particular it supersedes the
positive `e=1,2` boundary debits and excludes four of the five additional
necklace-paid cells. It does not apply when `e>=h` or in the remaining strip
`h<2e+1`.
