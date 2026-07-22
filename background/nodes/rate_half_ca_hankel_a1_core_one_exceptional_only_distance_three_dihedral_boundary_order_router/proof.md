# Proof

For every matched pair `{a,b}`, the matching-free boundary theorem gives

```text
K_A(b)^e=-K_A(a)^e,                                  (1)
K_A(x)=P_X'(x)/(B(x)^4 A'(x)^4).
```

All values below are nonzero on the official support packet.

## 1. Antipodal pairs

Here `A` is even, so `A'(-a)=-A'(a)`. Using

```text
P_X'(x)=N x^(-1)/((x-s)(x-x_0))
```

in `(1)` gives

```text
R_-(a)^e=-1,
R_-(X)=-F(X)/F(-X).                                  (2)
```

The rational function `R_-` has degree at most 14 and is nonconstant. If it
were constant, `R_-(-X)=R_-(X)^(-1)` and `R_-(0)=-1` would force `F` to be
even. Its zero divisor would then be stable under negation. Multiplicities
force the three-element root set of `B` to be stable under negation, which
is impossible in odd characteristic because a negation-stable odd set of
nonzero elements has a fixed point.

Choose one representative from each of the `e` antipodal pairs. Equation
`(2)` gives `e` distinct preimages under a nonconstant degree-at-most-14 map
of the set

```text
{y in F_p^*:y^e=-1},
```

which has exactly `g=gcd(e,p-1)` elements when nonempty. Hence

```text
e<=14g.                                              (3)
```

Since `g|e` and the only divisors of `e` whose cofactor is at most 14 have
cofactor one or three, `(3)` gives `(DBO2)`.

## 2. Constant-product pairs

Now `b=c/a` and

```text
X^(2e) A(c/X)=c^e A(X).
```

Differentiating at a root `a` gives

```text
A'(c/a)=-c^(e-1)a^(-(2e-2))A'(a).                   (4)
```

Substitute `(4)` and the formula for `P_X'` into `(1)`. Since
`N=8e+8` and `a^N=1`, all powers of `a` cancel, leaving

```text
R_c(a)^e=-1,
R_c(X)=c^(3-4e) F(X)/F_c(X),
F_c(X)=X^14F(c/X).                                   (5)
```

If `R_c` is nonconstant, the same degree and fiber count as in `(3)` proves
`(DBO2)`. If it is constant, `F_c` is proportional to `F`. Equality of their
zero divisors says that the zero multiset of `F` is invariant under
`x |-> c/x`. The roots `s,x_0` have multiplicity one and the three roots of
`B` have multiplicity four, so the two multiplicity classes are invariant
separately. This is exactly `(DBO4)`.

An inversion-stable three-element set contains exactly one fixed point and
one two-cycle: the involution has at most two fixed points, and using both
would leave the third point without its mate. Hence `c` is a square and
`T={u,t,c/t}` with `u^2=c` and `t^2!=c`. The invariant two-element set
`{s,x_0}` is either one two-cycle or the complete fixed-point set. The latter
would consume both fixed points, leaving no fixed point for the disjoint
triple `T`. Therefore `s` and `x_0` form a two-cycle, so `c=sx_0`. This is
`(DBO5)`.

It remains to apply the triple part of the same matching-free boundary
theorem. Write `v=c/t` for the nonfixed mate in `T`. Reciprocal symmetry of
`A` gives

```text
A(v)=c^e t^(-2e)A(t).                                (6)
```

Using `c=sx_0` in the derivative formula for `P_X` gives

```text
P_X'(v)/P_X'(t)=t^4/c^2.                             (7)
```

For `B=(X-u)(X-t)(X-v)`, with `u^2=c`, direct differentiation gives

```text
B'(t)/B'(v)=t/u.                                     (8)
```

Combining `(6)--(8)` in
`K_B(x)=P_X'(x)/(A(x)^4B'(x))`, then using
`t^N=1`, `c=u^2`, and `N=8e+8`, yields

```text
K_B(v)/K_B(t)
 =t^(8e+5)c^(-4e-2)u^(-1)
 =(u/t)^3.                                           (9)
```

The triple gate says `K_B(v)^e=K_B(t)^e`, so `(9)` gives `(DBO6)`.
Both `u/t` and `t/u` lie in `mu_N`, while `gcd(3e,N)=1` because `N` is a
power of two and `e` is odd. Hence `(DBO6)` forces `u/t=1`, contradicting
the distinct triple roots. The constant-map alternative is empty, and
`(DBO2)` holds on both dihedral branches. QED.
