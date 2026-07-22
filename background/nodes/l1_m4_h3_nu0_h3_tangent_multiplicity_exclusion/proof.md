# Proof - L1 m=4, h=3, nu=0 cubic-tangent multiplicity exclusion

The tangent supplier gives

```text
g(y_0)=b Delta/(8a^3)!=0,
kappa=4alpha y_0/g(y_0).                              (1)
```

Define the rational function

```text
phi(Y)=4alpha Y/g(Y).
```

At the tangent value,

```text
g(Y)-Yg'(Y)=b-2Y^3,
b-2y_0^3=-b Delta/(4a^3),
phi'(y_0)=-alpha b Delta/(a^3 g(y_0)^2)!=0.           (2)
```

Divide the exact Euler quotient factorization by `g(R)` and subtract
`kappa=phi(y_0)`:

```text
H-kappa=phi(R)-phi(y_0)+D T X R'/g(R).                (3)
```

Let `x` be a tangent root and put `e=ord_x(T)`. Since the preceding theorem
gives at least two distinct tangent roots, `e<=p-1`; hence the
characteristic does not divide `e`. Therefore

```text
ord_x(R-y_0)=e,       ord_x(R')=e-1.                  (4)
```

Write `d=ord_x(D)` and `epsilon=ord_x(X)`. The complement is squarefree, so
`d` is zero or one, while `epsilon` is zero or one. Because `g(R)` is a unit
at `x`, the correction term in (3) has order

```text
ord_x(D T X R'/g(R))=2e+d+epsilon-1.                 (5)
```

Equation (2) shows that the first term in (3) has exact order `e`. If
`e>=2`, then the order in (5) is strictly larger than `e`, so cancellation
at the leading local order is impossible. This proves `(TME2)`.

Now `H-kappa` is a nonzero polynomial of degree three. Every repeated
tangent multiplicity is consequently at most three, and every simple
multiplicity is already one. The `r` distinct multiplicities sum to
`deg T=p`, while `(TME3)` gives `r<=3`. Hence `p<=9`, contradicting every
official characteristic. This proves the exclusion.
