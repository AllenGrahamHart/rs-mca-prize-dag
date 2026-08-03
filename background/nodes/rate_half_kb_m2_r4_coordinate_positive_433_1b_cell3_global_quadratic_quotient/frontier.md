# Frontier

The six-basis norm route, nested-quadratic cut, finite direct solvers, and
parallel-edge transport have now proved all `432` cases with
`xi in {0,1,2}` and `pairing in {0,1,2,3,4,5,6,7,8}`.  The next route decision is
between `pairing=9` for the parallel-`DE` missing block and
`xi=3,pairing=0` in the localized quadratic algebra

```text
b^2 = -(B_epsilon/A_epsilon)b - 1,
c = -C_epsilon/D_epsilon.
```

Retain every element in the basis `{1,t,t^2,b,bt,bt^2}`.  The successful
pairing-3 through pairing-8 routes used FLINT-backed rational functions, direct
and tower norm cross-checks, and direct lifts of every norm and intermediate
exceptional root.  Pairing 5 established that the target-label exchange
maps cell 3 to cell 6; do not use it as a within-cell transport.

The direct `xi=3,pairing=0` colored/missing-sum quartic resultant already
exceeded the 300-second cap in both Sylvester and Euclidean forms, so that
branch still needs a lower elimination degree or shared-`f` structure.

Do not return to the monolithic six-variable SymPy expansion or Singular at
the deployed characteristic.  Do not call a quadratic relation a
parametrization, and do not infer complete cell-3 closure from the nine paid
parallel-`DE` matching indices.
