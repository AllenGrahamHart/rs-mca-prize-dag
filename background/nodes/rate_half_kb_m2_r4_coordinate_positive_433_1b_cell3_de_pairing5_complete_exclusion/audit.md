# Audit

- Matching 5 is pinned as `((0,2),(1,5),(3,4))`; its second quadratic is
  `paired(second_de,sigma_c c f)` and its final pair is
  `paired(sigma_o e f,b f)`.
- The missing relation follows from `d=u/f`, `e=de f/u`; its cleared
  quartic and degree-eight eliminant are pinned in source and verifier.
- The norm depends on `sigma_c` but not `sigma_o`.  Each computed source
  row fixes the former and explicitly checks both latter lanes.
- Every intermediate exceptional root is directly lifted through the
  original source equations.
- The sixteen source-level boundary records all have `f=0` and each covers
  both `sigma_o` lanes at its fixed `sigma_c`.
- All 96 nonboundary lane evaluations make the third paired equation
  nonzero.  There is no hidden target-guard inference.
- The theorem counts 32 computed and 16 transported raw atlas cases; source
  points and eliminant roots are not recounted as raw cases.
- The tempting `b<->c` shortcut is not used: it exchanges common roles
  `AB,AC` and sends role cell 3 to duplicate cell 6 rather than stabilizing
  cell 3.
