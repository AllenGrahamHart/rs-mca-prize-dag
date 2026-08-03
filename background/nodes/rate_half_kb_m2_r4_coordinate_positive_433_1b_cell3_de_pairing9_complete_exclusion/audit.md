# Audit

- Matching 9 is pinned as `((0,4),(1,2),(3,5))`: its first cuts are
  `paired(de,b f)` and `paired(second_de,d f)`, and its final cut is
  `paired(sigma_o e f,sigma_c c f)`.
- The missing-sum eliminant is derived with `u=df`; direct replay recovers
  `d=u/f` and then `e=de/d`.
- The norm is target-lane independent. Each computed source row explicitly
  checks all four target lanes.
- Direct six-by-six and quadratic-over-cubic tower norms agree in all eight
  rows.
- All norm roots, denominator roots, inverse-guard roots, and the base-cubic
  leading-coefficient roots enter the direct lift.
- The eight source-level boundary records all have `f=0` and each covers
  all four target lanes.
- All 128 nonboundary final-pair evaluations are nonzero.
- The theorem counts 32 computed and 16 transported raw atlas cases; source
  rows are not confused with raw cases.
- No target-label exchange is used as a within-cell symmetry.
