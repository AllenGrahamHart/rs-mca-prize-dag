# Claim Contract

- **Claim ID:** `(KBP1B3-DE-P8-1)`
- **Source cell:** coordinate-positive `433-1b`, outside role cell 3
- **Missing records:** the three parallel `DE` copies, `xi=0,1,2`
- **Matching:** canonical index `8 = ((0,3),(1,5),(2,4))`
- **Sign coverage:** four source-sign pairs and four target-sign lanes
- **Raw cases excluded:** `48`
- **Computed rows/raw cases:** `32`, one for each source sign, target lane,
  and `xi in {0,2}`
- **Transported raw cases:** `16` at `xi=1`
- **Algebra:** quadratic over cubic, basis `1,t,t^2,b,bt,bt^2`
- **Elimination:** quadratic `P_u`, quadratic `P_f`, degree-eight
  missing-sum eliminant, linear remainder, quadratic resultant, six-basis
  norm
- **Terminal boundary ledger:** 32 records, all exactly `f=0`
- **Not claimed:** another matching or missing role, complete cell 3,
  complete `433-1b`, K3, band closure, or a prize theorem
