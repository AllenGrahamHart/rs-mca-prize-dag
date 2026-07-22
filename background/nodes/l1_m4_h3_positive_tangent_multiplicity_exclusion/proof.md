# Proof - L1 m=4, h=3 positive tangent multiplicity exclusion

The supplier proves that only `(nu,eta)=(1,2),(2,1)` survive. In both
cases, `nu+eta=3`, so

```text
P=X^nu H-kappa
```

is a nonzero cubic: its constant term is `-kappa!=0` and its leading term is
the leading term of `X^nu H`.

As in the zero-valuation tangent argument, put

```text
phi(Y)=4alpha Y/g(Y).
```

The identities

```text
g(y_0)=b Delta/(8a^3)!=0,
phi'(y_0)=-alpha b Delta/(a^3 g(y_0)^2)!=0             (1)
```

hold because positive valuation forces `b!=0`, while the outer cubic is
squarefree.

Multiply the Euler quotient factorization

```text
D T V=H g(R)-4alpha U
```

by `X^nu/g(R)` and subtract `kappa=phi(y_0)`. Since `R=X^nu U`, this gives

```text
P=phi(R)-phi(y_0)+X^nu D T V/g(R).                    (2)
```

Let `x` be a tangent root and `e=ord_x(T)`. Positive valuation gives
`T(0)=3b!=0`, so `x!=0`. The tangent-radical theorem gives at least two
distinct roots, and consequently `e<=p-1`. From

```text
T'=2aX^(nu-1)V
```

we obtain `ord_x(V)=e-1`. If `d=ord_x(D)` is zero or one, then the correction
term in (2) has order

```text
ord_x(X^nu D T V/g(R))=2e+d-1.                        (3)
```

By (1), `phi(R)-phi(y_0)` has exact order `e`. For `e>=2`, the order in (3)
is larger, so no leading cancellation is possible and `ord_x(P)=e`.

The cubic `P` therefore bounds every repeated multiplicity by three; simple
roots are already bounded by one. Since `r<=3`, the degree-`p` tangent fiber
would have `p<=9`, contradicting the official rows. Both positive strata are
empty.
