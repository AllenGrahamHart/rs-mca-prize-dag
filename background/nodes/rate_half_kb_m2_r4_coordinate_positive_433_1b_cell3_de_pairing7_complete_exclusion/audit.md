# Audit

- Matching 7 is pinned as `((0,3),(1,4),(2,5))`: its first cuts are
  `paired(de,sigma_o e f)` and `paired(second_de,b f)`, and its final
  cut is `paired(d f,sigma_c c f)`.
- The missing-sum eliminant is derived with `u=ef`; direct replay recovers
  `e=u/f` and then `d=de/e`.
- The norm depends on `sigma_o` but not `sigma_c`. Each computed source
  row fixes the former and explicitly checks both latter lanes.
- Direct six-by-six and quadratic-over-cubic tower norms agree in all 16
  rows.
- All norm roots, denominator roots, inverse-guard roots, and the base-cubic
  leading-coefficient roots enter the direct lift.
- The sixteen source-level boundary records all have `f=0` and each covers
  both `sigma_c` lanes at fixed `sigma_o`.
- All 64 nonboundary lane evaluations make the third paired equation
  nonzero.
- The theorem counts 32 computed and 16 transported raw atlas cases; source
  rows are not confused with raw cases.
- No target-label exchange is used as a within-cell symmetry.
