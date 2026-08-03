# Audit

- Matching 8 is pinned as `((0,3),(1,5),(2,4))`: its first cuts are
  `paired(de,sigma_o e f)` and `paired(second_de,sigma_c c f)`, and its
  final cut is `paired(d f,b f)`.
- The missing-sum eliminant is derived with `u=ef`; direct replay recovers
  `e=u/f` and then `d=de/e`.
- Both target signs enter the nested cut. Each computed row covers exactly
  its printed target lane.
- Direct six-by-six and quadratic-over-cubic tower norms agree in all 32
  rows.
- All norm roots, denominator roots, inverse-guard roots, and the base-cubic
  leading-coefficient roots enter the direct lift.
- The 32 boundary records all have `f=0`.
- All 96 nonboundary final-pair evaluations are nonzero.
- The theorem counts 32 computed and 16 transported raw atlas cases; source
  rows are not confused with raw cases.
- No target-label exchange is used as a within-cell symmetry.
