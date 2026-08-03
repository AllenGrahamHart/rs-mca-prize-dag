# Frontier

The six-basis norm route, nested-quadratic cut, finite direct solvers, and
parallel-edge transport have now proved all `720` cases with
`xi in {0,1,2}` and
`pairing in {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14}`. No parallel-`DE`
matching remains. The `xi=3,pairing in {0,1,2}` routes are now proved by
the three-branch reciprocal-square and reciprocal-linear theorems, raising
the paid cell-3 ledger to 768 cases. The next route decision is to classify
the residual matching orbits at `xi=3,pairing in {3,...,14}` and
`xi in {4,5,6}`.

```text
b^2 = -(B_epsilon/A_epsilon)b - 1,
c = -C_epsilon/D_epsilon.
```

Retain every element in the basis `{1,t,t^2,b,bt,bt^2}`.  The successful
pairing-3 through pairing-14 routes used FLINT-backed rational functions, direct
and tower norm cross-checks, and direct lifts of every norm and intermediate
exceptional root.  Pairing 5 established that the target-label exchange
maps cell 3 to cell 6; do not use it as a within-cell transport.

At `xi=3,pairing=0`, factoring `paired(q,q)` and setting `y=1/d^2`
replaced the timed-out colored/missing-sum quartic resultant by two
quadratics. Pairings 1 and 2 reused the three `q` branches and reduced their
even quartic in `z=1/d` modulo the remaining quadratic paired cut. Both
routes are now exact proved exclusions.

Do not return to the monolithic six-variable SymPy expansion or Singular at
the deployed characteristic.  Do not call a quadratic relation a
parametrization, and do not infer complete cell-3 closure from the fully paid
parallel-`DE` matching block or the three paid `xi=3` matchings.
