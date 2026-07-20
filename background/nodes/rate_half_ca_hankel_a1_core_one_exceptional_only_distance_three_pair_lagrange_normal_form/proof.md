# Proof

The MDS-escape router gives exactly `3e` external slopes. At every one of
them its external locator `G_z` satisfies

```text
G_z(t)/A(t)=constant       for t in T.                (1)
```

Multiplying by the nonzero leading coefficient of the clean fiber shows
that, for any `t,u in T`, the parameter form

```text
A(u)Q(z;t)-A(t)Q(z;u)                                (2)
```

vanishes at all `3e` external slopes. Its degree is at most `e`, so `(2)`
vanishes identically. All supported slopes are finite in the official
normalization.

Set

```text
phi(z)=Q(z;t)/A(t)
```

for any `t in T`. Equation `(2)` makes this independent of `t`. The global
normalization gives `phi(0)=1`. Every internal locator contains all three
points of `T`, so `phi` vanishes at `xi_1,...,xi_e`. These are `e` distinct
nonzero points and `deg phi<=e`; hence `phi=Phi` from `(PLN3)`.

It follows that

```text
Q(z;X)-Phi(z)A(X)                                    (3)
```

vanishes at every root of the squarefree cubic `B`. Therefore `(3)` is
divisible by `B` in `F[z,X]`. Write

```text
Q(z;X)=Phi(z)A(X)+B(X)L(z;X).                        (4)
```

The degree bounds are

```text
deg_z L<=e,       deg_X L<=r-3=2e-2.                 (5)
```

At `z=0`, equation `(4)` and `Q(0)=A=Phi(0)A` give `L(0;X)=0`, so

```text
L(z;X)=z M(z;X),       deg_z M<=e-1.                 (6)
```

The internal support formula from the dependency gives `(PLN2)`. Evaluating
`(4)--(6)` at `xi_i` therefore yields

```text
M(xi_i;X)=(lambda_i/xi_i)A(X)/D_i(X).                (7)
```

There are exactly `e` interpolation points and `M` has parameter degree at
most `e-1`. Coefficientwise Lagrange interpolation of `(7)` gives `(PLN4)`.

At a triple point the second term of `(PLN4)` vanishes, proving the first
identity in `(PLN5)`. If `a` belongs to the pair indexed by `i`, then
`A(a)=0`; every quotient `A/D_j` with `j!=i` still contains the factor
`X-a`, while `A/D_i` does not vanish at `a`. Substitution proves the second
identity, with

```text
c_a=B(a)(lambda_i/xi_i)(A/D_i)(a)!=0.                (8)
```

This also proves the printed parameter-root pattern.

For independence of the `X`-side family, evaluate a putative relation at a
root in the pair indexed by `i`. Only `B A/D_i` survives, so its coefficient
is zero. This holds for every `i`, after which the coefficient of `A` is
zero. On the parameter side, `Phi(0)=1` while every `zL_i` vanishes at zero;
the remaining `L_i` form the Lagrange basis through the `e` internal slopes.
Thus both families in `(PLN6)` are independent and `(PLN4)` has separation
rank exactly `e+1`. QED.
