# KoalaBear m4 outer A6/S6 route cut

- **status:** PROVED
- **scope:** residual actual KoalaBear `Q=6,s=6,u=2` decomposition branch
- **dependencies:** `rate_half_kb_source_pencil_rank_transverse_compiler`,
  `rate_half_kb_m12_secondary_degree5_decomposition_exclusion`
- **consumer:** `rate_half_band_closure`

For an inner-degree-four transverse terminal, the outer map has degree 15
and the possible outer-correspondence types are

```text
(r,delta)=(1,16),(2,8),(4,4),(8,2).
```

The complete primitive degree-15 catalogue has nontrivial subdegrees `14`,
except for `A6,S6` on the 15 two-subsets of six points, whose subdegrees are
`6,8`. Thus `r=1,2,4` force the outer map to decompose. Its proper right
factor has degree 3 or 5, giving a decomposition of the endpoint map with
inner degree 12 or 20. Degree 12 is proved empty and degree 20 is excluded
by the exhaustive source-fiber profile theorem.

Only `(r,delta)=(8,2)` survives, and only with primitive outer monodromy
`A6` or `S6` in the two-subset action. The global independent transverse
frontier has nine types: the three `m=2` types, five `m=3` types, and this
one `m=4` type.

## Falsifier

A primitive degree-15 group with subdegree 1, 2, or 4; a proper factor of
degree 15 other than 3 or 5; or a valid inner-degree-12 or inner-degree-20
source profile.
