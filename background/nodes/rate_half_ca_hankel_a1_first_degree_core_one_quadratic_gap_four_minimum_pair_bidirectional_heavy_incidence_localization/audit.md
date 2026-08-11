# Audit

1. The proof uses actual supports `S_gamma`, not padded locators `E_gamma`.
   This is what removes the old orientation restriction.
2. Every difference point is light because named heavy rows are absent from
   actual errors. Thus a row root at such a point is an actual support
   incidence, not padding.
3. The rank-one contradiction counts `e+1` line slopes against global light
   degree `e`; it does not assume positivity of any field weight.
4. A single residual root with `r_delta>=1` already has enough actual-support
   intersection with the endpoint union to trigger minimum distance.
5. Cross-orientation residual disjointness is proved only after residual
   deficits are shown to vanish.
6. `W` is the exact unused supported-slope set. Heavy correction roots that
   are not supported slopes are not inserted into `W` or the deficit sum.
7. The factor `2` in the two-simple slack payment is the maximum per-slope
   deficit, not a claim that both heavy rows occur at every slack slope.
