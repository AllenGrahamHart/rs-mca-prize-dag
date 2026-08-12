# `A=1` quadratic truncated-source minimal-recurrence separation fence

- **status:** REFUTED
- **refuted claim:** roots of the compressed minimal recurrence must lie in
  the original fixed source
- **consumer:** nonreduced collision routing

The following implication is false:

```text
x_* notin U_0
  => P_tau(x_*)!=0,                                (TSF1)
```

where `P_tau` is the minimal recurrence polynomial of a truncated Hankel
moment sequence represented by nonzero weights on `U_0`.

An exact counterexample exists over `F_101` at the small core-one ratios

```text
e=5,       p=7,       d=13,       |U_0|=19.       (TSF2)
```

Take `U_0={1,...,19}`. There are all-nonzero weights on `U_0` whose first
`2d+1=27` moments equal those of all-nonzero weights on either of the
disjoint sets

```text
A_12={30,...,41},       A_11={30,...,40}.          (TSF3)
```

The resulting `14 x 14` Hankel matrices have ranks 12 and 11. Their
minimal recurrences are the squarefree locators `P_A`, although every root
of `P_A` lies outside `U_0`. Taking `x_*=30` gives `P_A(x_*)=0`.

Moreover, the degree-13 kernel polynomial can be chosen with `x_*` as an
exact double root in both regular-corank cases:

```text
corank 1:       Q=P_A(X-x_*),
corank 2:       Q=P_A(X-x_*)(X-90).                (TSF4)
```

Thus neither corank one nor higher corank provides automatic
original-source separation at a truncated moment fiber.

## Scope

The fixtures refute only `(TSF1)` and any proof step based solely on the
truncated Vandermonde representation. They do not realize the complete
global split-biform packet or refute the repaired conditional jet theorem.
