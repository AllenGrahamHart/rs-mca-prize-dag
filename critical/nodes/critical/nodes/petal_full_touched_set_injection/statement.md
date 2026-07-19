# Full-petal touched-set injection

- **status:** PROVED
- **consumer:** `petal_k4_primitive_bound`

Fix one G1 sunflower chart with missed-core locator `L_D`, retained locator
`L_R`, `m` pairwise disjoint petals of size `ell`, labels `c_i`, degree bound
`d`, retained size `r`, and auxiliary agreement threshold

```text
a=ell+d-r.
```

Restrict to the actual full-petal chart image: `G|R=0`, and on each petal the
agreement set is either the whole petal or empty. Then the map sending a listed
polynomial to its touched-petal index set is injective. Consequently the
complete full-petal list, before the stabilizer-primitive filter, has size at
most

```text
sum_(t=ceil(a/ell))^m C(m,t).
```

The downstream `petal_top_band_tail_collapse` theorem bounds this tail by
`m+1`, proving K4. The remaining aggregate obligation is G1's paid weighted
atlas census `sum_chi(m_chi+1)<=(121/128)n^6`.
