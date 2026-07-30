# KoalaBear m2 r2 degree-three source-facet exclusion

- **status:** PROVED
- **scope:** sole residual full-V4 `n=3` dihedral component
- **dependencies:**
  `rate_half_kb_q6_s6_common_five_outgoing_fiber_pin`,
  `rate_half_kb_m2_r2_dihedral_residual_star_graph_rigidity`
- **consumer:** `rate_half_band_closure`

The residual cubic source-star graph is

```text
G=K_(2,2,2) disjoint_union K_(2,2,2).               (KB3F-1)
```

For every source label `k`, the two stars over the complete coordinate
fiber `psi^(-1)(alpha_k)` together equal the graph neighborhood `N_G(k)`.
The common-five outgoing-fiber pin supplies `K subset I`, `|K|=5`, and
forces

```text
N_G(k) subset I^c       for every k in K.            (KB3F-2)
```

Thus `K` would be an independent five-set in `G`. But each
`K_(2,2,2)` has independence number two, so `alpha(G)=4`. This
contradiction proves that the `n=3` actual component is impossible.

This deletes the last residual factor degree inside the full-V4 row. The
aggregate full-V4 close is a separate synthesis node. No owner or payment is
constructed, and no endpoint, KoalaBear, or Prize row is closed here.

## Falsifier

A cubic source fiber whose two stars do not form `N_G(k)`, failure of the
common-five horizontal fiber identity, or an independent five-set in two
disjoint copies of `K_(2,2,2)`.
