# Proof

Let `a_j` be the elementary symmetric functions of the nine roots in
`(QDD1)`. Newton's identity at an odd index `m<=7` is

```text
m a_m=sum_(i=1)^m (-1)^(i-1)a_(m-i)p_i.               (1)
```

If `i` is odd, its power sum vanishes by `(QDD2)`. If `i` is even, `m-i` is
an earlier odd index. Induction in `(1)` therefore gives

```text
a_1=a_3=a_5=a_7=0.                                    (2)
```

All roots lie in `mu_2048`, so their product `a_9` does too. The map
`z -> z^9` is an automorphism of this group because

```text
9*1593=1 mod 2048.                                    (3)
```

Thus `(QDD3)` is the unique dilation making the product one. Multiplying all
roots by `lambda` multiplies `p_j` by `lambda^j`, so it preserves every
vanishing and reducedness.

Apply `(2)` to the normalized monic locator. Its constant term is minus the
root product, hence minus one, and it has exactly the form

```text
F(X)=X^9+a_2X^7+a_4X^5+a_6X^3+a_8X-1
    =X A(X^2)-1.                                      (4)
```

This proves `(QDD4)--(QDD5)`. Direct multiplication gives the key descent

```text
-F(X)F(-X)=X^2A(X^2)^2-1=G(X^2).                      (5)
```

The original signed support is reduced. Hence its roots are distinct and no
two are antipodal, so their squares are nine distinct elements of
`mu_1024`. Equation `(5)` shows that these are all roots of the monic
degree-nine polynomial `G`, proving `(QDD7)`.

Conversely suppose `G` divides `Y^1024-1`. The latter polynomial is
separable under the characteristic hypothesis, so `G` has nine distinct
roots in `mu_1024`. At any root `y`, equation `(QDD6)` gives

```text
yA(y)^2=1.                                             (6)
```

In particular `A(y)` is nonzero. Define `rho=A(y)^(-1)`. Then `(6)` gives
`rho^2=y`, so `rho` lies in `mu_2048`. Distinct `y` give distinct,
nonantipodal `rho`. Moreover

```text
rho A(rho^2)-1=0,                                      (7)
```

so the nine reconstructed roots are exactly the roots of `F=XA(X^2)-1`.
Its constant term makes their product one. The coefficients of `F` have the
four odd elementary gaps in `(2)`, and Newton's identities in the reverse
direction give `p_1=p_3=p_5=p_7=0`. Writing each element of `mu_2048`
uniquely as `s omega^e`, with `s` in `{+1,-1}` and `0<=e<1024`, the distinct
squares make the base exponents distinct. Thus the reconstructed relation is
reduced. This proves the converse and the bijection.

Because `G` is monic, Euclidean division proves that every coefficient in
`(QDD9)` is integral in the four displayed variables. Suppose the ideal
`I` were proper over `Q`. It would have a point over an algebraic closure of
`Q`, and hence, after embedding its finite coordinate field in `C`, would
give a complex quartic satisfying `(QDD7)`.

The converse would then give a reduced signed relation at a primitive
`2048`th root `zeta`. Equivalently, a nonzero polynomial

```text
sum_i s_i Z^e_i,       deg<1024,                       (8)
```

would vanish at `zeta`. This is impossible because the minimal polynomial
of `zeta` is `Z^1024+1`. Therefore `I` is the unit ideal over `Q`. A rational
Nullstellensatz identity for one can be cleared of denominators, yielding
`(QDD11)` with `Delta!=0`.

Finally, reducing `(QDD11)` in a field carrying a solution makes its right
side zero. Its characteristic must therefore divide `Delta`. QED.
