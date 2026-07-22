# Proof - L1 exact-shell prefix/Hankel bridge

## 1. Exact-shell bijection

The vector in `(EH1)` is zero exactly when `deg I_A(U)<k`. Thus every
`A in E_a(U)` maps to a degree-below-`k` polynomial whose exact agreement set
is `A`.

Conversely, let `P` have degree below `k` and exact agreement set `A` of size
`a`. Since `P` and `I_A(U)` agree on the `a>k` points of `A` and both have
degree below `a`, interpolation uniqueness gives `I_A(U)=P`. Hence
`Phi_(U,a)(A)=0`, and exactness puts `A` in `E_a(U)`. The two constructions
are inverse. Partitioning the list by its exact agreement size proves
`(EH3)`.

## 2. Local factorization

Fix `A`, `D`, and `X` as in the statement. The polynomial `I_A(U)-Q`
vanishes on `C\D`, so there is a unique polynomial `J` with

```text
I_A(U)-Q=L_(C\D)J.                                     (1)
```

The degree of the left side is below `a=k+w`, while
`deg L_(C\D)=k-1-d`; hence `deg J<d+w+1=|X|`. On `X`, equations `(EH4)` and
`L_C=L_(C\D)F` give

```text
L_(C\D)(x)J(x)=alpha(x)L_(C\D)(x)F(x).
```

The core locator is nonzero outside `C`, so cancellation gives
`J(x)=alpha(x)F(x)` on `X`. By degree and interpolation uniqueness,
`J=I_X(alpha F)`, proving `(EH5)`.

## 3. Unitriangular prefix transport

Write

```text
L_(C\D)=X^(k-1-d)+lower terms,
J=sum_(i=0)^(d+w) j_i X^i.
```

Terms `j_i` with `i<=d` contribute only through degree
`d+(k-1-d)=k-1`, so they do not affect the prefix coordinates in degrees
`k,...,k+w-1`. In descending degree order, multiplication by the monic core
locator sends

```text
(j_(d+w),...,j_(d+1))
```

to the coefficients of `L_(C\D)J` in degrees `k+w-1,...,k` by a triangular
matrix with every diagonal entry one. The term `Q` has degree below `k` and
does not affect those coordinates. This proves `(EH6)` and therefore the
equivalence `(EH7)`.

## 4. Exactness guards and converse

For `z in D`, equation `(1)` and `U(z)=Q(z)` show that `z` would be an extra
core agreement exactly when `J(z)=0`. For `y outside C union X`, cancellation
as above shows that `y` would be an extra noncore agreement exactly when
`J(y)=alpha(y)F(y)`. Thus `(EH8)` is equivalent to exact agreement set `A`.
Since `F` is squarefree with root set `D`, the first guard also gives
`gcd(F,J)=1`.

Conversely, start from `D,X`, put `F=L_D`, interpolate `J=I_X(alpha F)`, and
assume `(EH7)--(EH8)`. Define

```text
P=Q+L_(C\D)J.
```

Equation `(EH7)` gives `deg J<=d`, so `deg P<k`. It agrees with `U` on
`(C\D) union X`, while `(EH8)` excludes every other point. Thus its exact
agreement set is `A=(C\D) union X`, and the first part puts `A in E_a(U)`.

Finally, with `s=k+sigma`, `a=s+lambda`, and `ell=sigma+1`, direct subtraction
gives `(EH9)`.
