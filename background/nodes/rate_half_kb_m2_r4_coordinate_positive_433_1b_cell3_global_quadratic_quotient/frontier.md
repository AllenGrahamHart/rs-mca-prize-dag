# Frontier

The six-basis norm route, nested-quadratic cut, finite direct solvers, and
parallel-edge transport have now proved all `720` cases with
`xi in {0,1,2}` and
`pairing in {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14}`. No parallel-`DE`
matching remains. The `xi=3,pairing in {0,1,2}` routes are now proved by
the three-branch reciprocal-square and reciprocal-linear theorems, raising
the paid cell-3 ledger to 768 cases. The opposite-DE parity theorem pays
`xi=3,pairing in {3,6}`, and the two fully mixed theorems pay
`xi=3,pairing in {7,8,10,11,13,14}`, raising the ledger to 896 cases. The
remaining `xi=3` pairings form two two-element transport orbits, `{4,9}` and
`{5,12}`; every pairing at `xi in {4,5,6}` remains.

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
routes are now exact proved exclusions. The opposite-sign equation is an
even quartic in `q`; parity descent closes pairings 3 and 6. Fully mixed
pairings 11 and 14 use a linear-`z` compatibility cut; pairings 7, 8, 10, and
13 use a quadratic-`q` resultant reduced modulo the monic missing-`f`
quartic. The analogous pairing-4/5 compiler still exceeds the 300-second row
cap and must be re-factored before reuse.

Do not return to the monolithic six-variable SymPy expansion or Singular at
the deployed characteristic.  Do not call a quadratic relation a
parametrization, and do not infer complete cell-3 closure from the fully paid
parallel-`DE` matching block or the eleven paid `xi=3` matchings.
