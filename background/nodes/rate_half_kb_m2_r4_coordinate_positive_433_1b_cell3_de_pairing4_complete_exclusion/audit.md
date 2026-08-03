# Audit

- Matching 4 is pinned as `((0,2),(1,4),(3,5))`; the second quadratic is
  `paired(second_de,bf)`, not the pairing-3 `ef` cut.
- The missing relation follows from `d=u/f`, `e=de f/u`; its cleared
  quartic and degree-eight eliminant are pinned in source and verifier.
- The norm and first two paired cuts are target-lane independent.  Each
  computed source row explicitly declares and checks all four lanes.
- Every intermediate exceptional root is directly lifted through the
  original source equations.
- The eight source-level boundary records all have `f=0` and cover all
  target lanes.
- All 64 nonboundary lane evaluations make the third paired equation
  nonzero.  There is no hidden target-guard inference.
- The theorem counts 32 computed and 16 transported raw atlas cases; source
  points and eliminant roots are not recounted as raw cases.
