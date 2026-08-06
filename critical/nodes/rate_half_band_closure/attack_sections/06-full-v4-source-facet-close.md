
## 2026-07-29 KoalaBear full-V4 source-facet close

This section supersedes the earlier text naming `n=3` as the live full-V4
frontier. The PROVED
`rate_half_kb_q6_s6_common_five_outgoing_fiber_pin` imports Corollaries
9.25 and 9.27 of the pinned equality-wall source theorem. It gives
`K subset I` with `|K|=5` and, above both points of every complete source
fiber indexed by `k in K`,

```text
Root_T F_out(T,pi)=I^c.
```

For a residual cubic component, the PROVED source-star theorem identifies
the two component stars over that complete fiber with the four endpoints
`N_G(k)` in

```text
G=K_(2,2,2) disjoint_union K_(2,2,2).
```

This identification does not set the relative endpoint twist to one.
Before the facet constraint, the four endpoints are `U_k`, the complement
of one deck pair `P_k` in the relevant six-label component. Since
`k in I` and `U_k subset I^c`, one has `k notin U_k`; common-pole
membership then forces `k in P_k`, and only then `U_k=N_G(k)`.

Since the component divides `F_out`, `N_G(k) subset I^c` for every
`k in K`. Thus `K` would be independent, but `alpha(G)=2+2=4`. The PROVED
`rate_half_kb_m2_r2_dihedral_degree3_source_facet_exclusion` therefore
deletes `n=3` without ownership enumeration or field computation.

Combining this with the proved `n=2,5,6` exclusions and the exhaustive
factor-degree list closes the full-V4 type:

```text
(m,r,delta)=(2,2,4) is empty.
```

This is banked as
`rate_half_kb_m2_r2_dihedral_full_v4_exclusion`. The previous endpoint
cofactor/gain-flatness compiler remains a valid exact theorem and useful
upstream audit instrument, but universal gain nonflatness is no longer
required for this type.

The live `m=2` frontier is now exactly the order-two stabilizer type
`(r,delta)=(4,2)` and the trivial-stabilizer type `(8,1)`. No owner or
payment moves, so `rate_half_band_closure` remains TARGET.
