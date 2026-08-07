# Independent proof

Fix `c|n` and let `H_c` be the subgroup of `H` of order `c`.  The fiber of
`x -> x^c` through `x in D` is exactly `xH_c`: if `y^c=x^c`, then
`y/x in H` is a `c`-th root of unity, and cyclicity plus `c|n` identifies
these roots with `H_c`.

If `S` is a union of these fibers, each fiber has locator `X^c-x^c`.
Multiplying over the distinct quotient images gives a unique monic split
polynomial `L_bar` with

```text
L_S(X)=L_bar(X^c).                                  (1)
```

Equation `(1)` forces `c|e` and forces every nonzero sub-leading coefficient
index to be divisible by `c`.  Conversely, those coefficient conditions let
one collect the powers of `X` uniquely into a polynomial in `X^c`.  Every
root of that polynomial over `D_c` lifts to its complete `c`-point fiber in
`D`; squarefreeness follows from `char(F)` being coprime to `n`.  This proves
the three-way equivalence.  Its valid divisors are exactly the divisors of
`gcd(n,e,{j:lambda_j!=0})`, proving maximality of `s(S)`.

For the pair, let `c=gcd(s(P),s(Q))`.  The equivalence supplies unique
locators `A_c,B_c` of degree `e_c=e/c` with

```text
A=A_c(X^c),  B=B_c(X^c).                            (2)
```

The pair is nontrivial, so `A_c-B_c` is nonzero.  Substitution in `(2)` gives

```text
deg(A-B)=c deg(A_c-B_c).                             (3)
```

The depth-`t` condition and `(3)` imply

```text
deg(A_c-B_c)
 <= floor((e-t-1)/c)
  = e_c-ceil((t+1)/c),
```

which is exactly depth `t_c=ceil((t+1)/c)-1`.  Equation `(3)` also proves
`c|d` and hence `(QS-1)`.

If the quotient pair retained a common scale `b>1`, applying the first part
again would write both original locators as polynomials in `X^(cb)`,
contradicting maximality of `c`.  Hence the maximal quotient is
coefficient-primitive.

Conversely, pull back a coefficient-primitive depth-`t_c` pair by `X^c`.
Then

```text
c deg(A_c-B_c)
 <= ce_c-c ceil((t+1)/c)
 <= e-t-1,
```

so the pullback has depth `t`.  Any common scale strictly larger than `c`
would descend to a nontrivial common scale of the quotient pair, impossible.
Thus its maximal common scale is exactly `c`.  QED.
