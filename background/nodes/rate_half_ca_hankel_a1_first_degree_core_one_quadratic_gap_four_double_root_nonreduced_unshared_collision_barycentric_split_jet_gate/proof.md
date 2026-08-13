# Proof

The collision dictionary gives `Lambda(tau)!=0`, so `tau` is not one of
the assigned centers. At the collision `Q(tau,x_*)=F_0(tau)=0`; the Pade
syzygy and `Lambda(tau)!=0` therefore give `G(tau,x_*)=0`. Suppose `tau`
were an off-line supported slope. The all-excess vertical-fiber theorem
would then put
`x_*` in the complete fiber gcd

```text
gcd_X(Q(tau,X),G(tau,X))=A_tau(X)R_tau(X).          (1)
```

The roots of `A_tau` lie in `U_0`, whereas `x_*` does not. Hence `x_*`
would be padded-heavy at `tau`, making `g_*(tau)=0`. This contradicts
unsharedness. Therefore `tau` is not supported. Since the roots of every
`P_x` are off-line supported slopes, `(BSJ2)` follows.

The scalar-weld theorem and its connected-rank refinement show that the
actual paired biform supplies one full-support `lambda`, unique up to
scale, satisfying `(BSJ1)` and the coefficient-MDS equations.

For each parameter coefficient, `G(t,Y)` has `Y`-degree at most `n` and
`|X|>n`. Lagrange interpolation on all of `X` therefore gives

```text
G(t,Y)=sum_(x in X)
 lambda_xP_x(t)L_X(Y)/[(Y-x)L_X'(x)].              (2)
```

Evaluation at `Y=x_*` gives the first formula in `(BSJ4)`. Differentiating
the Lagrange basis gives

```text
d/dY [L_X(Y)/(Y-x)]_(Y=x_*)
 =[L_X(x_*)/(x_*-x)]
  [L_X'(x_*)/L_X(x_*)-1/(x_*-x)].                 (3)
```

Equations `(2)--(3)` prove the second formula in `(BSJ4)` and the Hasse
coefficient formulas `(BSJ5)`.

It remains to record the exact collision orders. At `x_*`, the Pade
syzygy is

```text
Q(t,x_*)B(t,x_*)-Lambda(t)G(t,x_*)
 =L_U0(x_*)F_0(t).                                 (4)
```

Here `ord_tau Q(t,x_*)=6`, `ord_tau F_0=2`, and
`Lambda(tau)L_U0(x_*)!=0`. The first term of `(4)` has order at least six,
so

```text
ord_tau G(t,x_*)=2.                                (5)
```

Equations `(BSJ4)--(BSJ5)` turn `(5)` into `(BSJ6)`. Finally the proved
Pade/split-jet dictionary identifies its routing coefficients with
nonzero scalar multiples of `J_0` and, after `J_0=0`, of `J_1`.
Its Smith trichotomy is exactly `(BSJ7)`. QED.
