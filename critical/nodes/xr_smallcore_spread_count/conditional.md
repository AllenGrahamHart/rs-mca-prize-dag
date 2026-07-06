# Conditional proof: small-core spread count

Status: CONDITIONAL on the routed spread-count inputs.

The close-look decomposition splits the post-cascade spread remainder into the
following legs.

- Same-slope leg: `xr_sameslope_list_crossover` proves that this is exactly the
  worst-word list object at radius `j`.
- Partial-forcing band: `xr_partial_tangent_band` covers the cores
  `r in [k+1, A-2]` by the graded tangent ledger.
- Far-spread core: `xr_fresh_codim_dichotomy` covers the 2c residual after the
  alpha/beta/gamma split.
- Exact-list staircase and primitive pullback inputs:
  `x4_exactlist_staircase_split` and `u1_pullback_dichotomy` are the routed
  terminal inputs for the list/pullback contribution in this residual.

Therefore the small-core spread count is not an independent target once these
predicate nodes are admitted.  It remains conditional because several of those
predicate nodes are themselves conditional/open on the critical path.
