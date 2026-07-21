# Proof

For an indeterminate `t`, put `X=t+t^(-1)`. The Dickson recursion gives

```text
C_j(X)=t^j+t^(-j).                                 (1)
```

Consequently

```text
C_m(X)-2=(t^(m/2)-t^(-m/2))^2
          =(X^2-4)U_(m/2-1)(X/2)^2,               (2)
```

where `U_r` is the Chebyshev polynomial of the second kind. Therefore

```text
Q_m(X)=U_(m/2-1)(X/2).                             (3)
```

It is monic of degree `m/2-1`. Its roots are the traces of the nontrivial
inverse pairs in `mu_m`. Indeed `(1)--(2)` give every such root, and equality
of two traces implies

```text
(x-y)(xy-1)=0.
```

There are `(m-2)/2` inverse pairs, equal to the degree in `(3)`, so there are
no other roots. They are distinct because `p` does not divide `m`. This proves
`(KTG1)--(KTG2)` and squarefreeness.

The dependency says that every retained endpoint trace `tau` satisfies

```text
A(tau)^q=1.                                        (4)
```

It also says that if `q` is odd, the endpoint ratio lies in `mu_(m/2)`;
hence its trace is a root of `Q_(m/2)`. If `q` is even, it is a root of
`Q_m`. Thus in both cases the complete allowed trace set before `(4)` is the
root set of `Q_M` from `(KTG3)`.

The polynomial `Q_M` splits into distinct linear factors over `F_p`.
Therefore its common roots with `A^q-1` are exactly the roots of their monic
gcd, and each contributes degree one. This proves `(KTG4)`. Modular
exponentiation computes `A^q mod Q_M` by repeated squaring, so no polynomial
of degree `q` needs to be materialized.

Every allowed trace comes from exactly the two ordered ratios `x,x^(-1)`;
the excluded fixed points are `+/-1`. Hence the ordered ratio count is twice
the gcd degree. Factoring the split squarefree gcd recovers the trace list.
The three nonempty controls are exact evaluations of this identity and rule
out the stronger universal-emptiness statement. QED.
