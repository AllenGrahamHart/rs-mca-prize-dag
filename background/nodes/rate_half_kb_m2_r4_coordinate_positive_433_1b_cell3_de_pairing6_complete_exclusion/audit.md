# Audit

- Matching 6 is pinned as `((0,3),(1,2),(4,5))`; its first cuts are
  `paired(de,sigma_o ef)` and `paired(second_de,df)`.
- The compiler uses `u=ef`, `v=df`, so direct recovery is `d=v/f`,
  `e=u/f`.  The replay checks those assignments against the original cuts.
- The quartic nested cut is only necessary.  Every finite survivor is
  replayed against the omitted colored pair and all target guards.
- Every intermediate exceptional root is directly lifted through the
  original source equations; no algebra singularity is silently discarded.
- All 32 terminal boundary records have `f=0` and only the `nonzero_5`
  failure.  The other finite lifts give 32 explicitly nonzero colored-pair
  evaluations.
- The theorem counts 32 computed and 16 transported raw atlas cases; source
  points and eliminant roots are not recounted as raw cases.
