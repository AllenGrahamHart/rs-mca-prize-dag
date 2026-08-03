# Frontier

The six-basis norm route, nested-quadratic cut, finite direct solvers, and
parallel-edge transport have now proved all `192` cases with
`xi in {0,1,2}` and `pairing in {0,1,2,3}`.  The next route decision is
between `pairing=4` for the parallel-`DE` missing block and
`xi=3,pairing=0` in the localized quadratic algebra

```text
b^2 = -(B_epsilon/A_epsilon)b - 1,
c = -C_epsilon/D_epsilon.
```

Retain every element in the basis `{1,t,t^2,b,bt,bt^2}`.  The successful
pairing-3 route used FLINT-backed rational functions, a quadratic resultant,
the direct/tower norm cross-check, and a direct lift of every norm and
intermediate exceptional root.  Reuse that backend for pairing 4 if its
residual equations admit a comparable low-degree cut.

The direct `xi=3,pairing=0` colored/missing-sum quartic resultant already
exceeded the 300-second cap in both Sylvester and Euclidean forms, so that
branch still needs a lower elimination degree or shared-`f` structure.

Do not return to the monolithic six-variable SymPy expansion or Singular at
the deployed characteristic.  Do not call a quadratic relation a
parametrization, and do not infer a remaining outside exclusion from the
three proved `DE` cases.
