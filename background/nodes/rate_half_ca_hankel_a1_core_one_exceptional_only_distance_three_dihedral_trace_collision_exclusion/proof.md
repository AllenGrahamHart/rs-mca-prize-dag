# Proof

Let `Gamma` be the `3e` roots of the squarefree external-slope locator
`P_Z`. Let `mathcal U` index all nonexceptional two-active-row orbits used
by the pair-complement trace. The trace count gives

```text
N=|mathcal U|>=3e-3.                                 (1)
```

For `u in mathcal U`, put `c_u=a_u/chi(u)`. Since an external slope is not
an internal slope, `I(gamma)!=0`. Formula `(PCT3)` therefore gives

```text
K_u(gamma)=0 iff q_gamma(u)=c_u.                    (2)
```

Every `K_u` is a squarefree degree-`e` divisor of `P_Z`, so exactly `e` of
the `3e` quadratics in `(TCX1)` take the common value `c_u` at `u`.

Partition `Gamma` by

```text
gamma~delta iff q_gamma=q_delta as polynomials.     (3)
```

Each equivalence class is selected all at once in `(2)`. If a class has
size `m`, then `m<=e`. Indeed, equality of the `U^2` coefficient fixes

```text
-M_0(gamma)/I(gamma)=theta.
```

All members of the class are roots of `M_0+theta I`. This is a nonzero
polynomial of degree at most `e`: for `theta!=0` its leading coefficient is
`theta`, while for `theta=0` it is the nonzero interpolation polynomial
`M_0`, whose values at the internal slopes are the nonzero `mu_i`.

We next lower-bound how often every class is selected. Fix
`gamma in Gamma` and inspect its external block `G_gamma`. That block has
`r=2e+1` rows. It can meet at most `r` of the `N` nonexceptional row pairs.
For every pair it does not meet, `(PCT1)` puts `gamma` in the corresponding
complement. Thus

```text
w_gamma=#{u:K_u(gamma)=0}>=N-r>=e-4.                (4)
```

All roots in one class have the same selection count; call it `w`.

Fix a class of size `m`. Whenever it is selected, the same complement
selects exactly `e-m` roots outside the class. Hence there are
`w(e-m)` incidences between such a complement and an outside root. Two
distinct quadratic classes can be selected together at no more than two
values of `u`, because the difference of their quadratics is nonzero and
has degree at most two. Summing over the `3e-m` outside roots gives

```text
(e-4)(e-m)<=w(e-m)<=2(3e-m).                        (5)
```

Write `d=e-m`. Equation `(5)` becomes

```text
(e-6)d<=4e.                                         (6)
```

For `e>=31`, `(6)` forces the integer `d<=4`, so every class has size at
least `e-4`. There are at most three classes because
`4(e-4)>3e`. There are at least three because every class has size at most
`e` and their sizes sum to `3e`. Therefore there are exactly three classes,
and all three have size exactly `e`.

By `(2)`, the root set of every `K_u` is a union of complete classes. Since
it has size `e`, it must be one of those three classes. This gives at most
three projective complement divisors. But the pair-complement trace proves
that the `N>=3e-3>3` orbit coordinates give distinct projective divisors.
This contradiction excludes both dihedral branches. QED.
