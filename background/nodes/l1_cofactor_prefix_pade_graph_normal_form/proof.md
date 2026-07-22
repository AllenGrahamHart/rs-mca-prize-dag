# Proof - L1 cofactor-prefix Pade graph normal form

## 1. Product reversal

Write the monic locator as

```text
L=Z^a+l_1 Z^(a-1)+...+l_a
```

and the degree-`e` cofactor as

```text
Q=q_e Z^e+q_(e-1)Z^(e-1)+...+q_0,     q_e=lc(U)=c.
```

The coefficient of `Z^(h-t)` in `QL` is the coefficient of `T^t` in
`Qhat Lhat`.  Since `d=h-k`, requiring `deg(U-QL)<k` is exactly equality of
these coefficients for `0<=t<=d`.  This proves `(PG1)`.

## 2. Graph and inverse

The constant term of `Qhat` is nonzero, so it is a unit in
`F[T]/(T^(d+1))`.  Therefore `(PG2)` has one solution for every choice of
its `e` nonconstant coefficients.  There are `q^e` choices.

Conversely, the first `e` coefficients of any unit series `Lhat` determine

```text
Qhat=Uhat/Lhat mod T^(e+1).
```

Its constant term is `c`, and substituting it into `(PG2)` reproduces the
chosen first `e` coefficients by uniqueness of truncated division.  Hence
projection of the solution set to `(l_1,...,l_e)` is both injective and
surjective.  Recursive series division expresses every later `l_t` as a
polynomial in the first `e` coefficients, with powers of the fixed nonzero
constant `c` in the denominators.  This proves claims 1--3 and `(PG4)`.

For a depth-`d` unit series `Lhat`, its quotient `Uhat/Lhat` satisfies
`(PG1)` for a degree-at-most-`e` `Qhat` exactly when the quotient
coefficients in degrees `e+1,...,d=e+w` vanish.  This is `(PG3)` and proves
claim 4.

## 3. Exact-shell bijection

An exact-shell member has `U-P=LQ` with `deg P<k`; Step 1 puts its locator
prefix in `G_(U,a)`, and `(PG4)` recovers the same `Q`.  If a domain point
outside the roots of `L` were an additional agreement, then
`L(x)Q(x)=0` with `L(x)!=0`, so `Q(x)=0`.  Exactness is therefore equivalent
to `gcd(Q,Omega/L)=1`.

Conversely, let `L|Omega` have prefix in the graph and recover `Q` by
`(PG4)`.  Equation `(PG1)` cancels all coefficients of `U-QL` from degree
`h` through degree `k`, so `P=U-QL` has degree below `k`.  It agrees with
`U` on every root of `L`; the gcd guard excludes agreement at every other
domain point.  This constructs the inverse in `(PG5)`.

## 4. Ambient scale

The graph has `q^e` points in an ambient depth-`d` space of size `q^d`.
Since `d=e+w`, its density is exactly `q^(-w)`.  Multiplying by the
`binom(n,a)` split locators gives the displayed natural scale.  This is an
accounting identity only; no uniformity of the divisor-prefix image is used.
