# Proof

Work over the algebraic closure of `F` and write the primitive linear factor
as

```text
P=A(X)Y+B(X)Z+C(X),      gcd(A,B,C)=1.              (LS1)
```

The mass router supplies at least 4,982 distinct pairs `(a_i,b_i)` in
`F[X]_<6^2` satisfying `P(X,a_i,b_i)=0` identically.

## Polynomial-section parameter

Let `g=gcd(A,B)`, `A=gA_0`, and `B=gB_0`, with `gcd(A_0,B_0)=1`.  Subtract
the equations for two distinct captured pairs.  Their difference satisfies

```text
A_0(a_i-a_j)+B_0(b_i-b_j)=0.
```

Coprimality gives a nonzero polynomial `t` such that

```text
a_i-a_j=B_0 t,       b_i-b_j=-A_0 t.               (LS2)
```

Since both differences have degree at most five,
`deg A_0,deg B_0<=5`.  One captured equation gives

```text
C=-g(A_0 a_i+B_0 b_i),
```

so `g` divides `C`.  Primitivity in `(LS1)` makes `g` a unit.  Normalize it
away.  Thus `A,B` are coprime and both have degree at most five.

Fix one captured pair `(a_0,b_0)`.  Every captured pair has the unique form

```text
(a_i,b_i)=(a_0+B t_i,b_0-A t_i),                  (LS3)
```

where

```text
deg t_i <= s:=5-max(deg A,deg B).                  (LS4)
```

The `t_i` are distinct.

## Johnson exclusion

Because `A` and `B` are coprime, they do not vanish simultaneously at any
evaluation coordinate.  Define an extension-field received word `tau` on
the inside support by

```text
tau(x)=(r_0(x)-a_0(x))/B(x)       if B(x)!=0,
tau(x)=-(r_1(x)-b_0(x))/A(x)      otherwise.
```

On the inside core of captured pair `i`, equation `(LS3)` gives
`tau(x)=t_i(x)`.  Thus at least 4,982 distinct degree-at-most-`s`
polynomials agree with `tau` on at least `u=807` of `e=130237` points.

The ordinary constant-block Johnson bound is

```text
J_s=floor(e(u-s)/(u^2-es)).                         (LS5)
```

For `0<=s<=4`, exact values are

```text
s       0    1    2    3    4
J_s   161  201  268  401  802.
```

If either `A` or `B` is nonconstant, then `s<=4`, contradicting
`4982>J_s`.  Hence `A,B` are constants.  The captured equation then gives
`deg C<=5`.

## Projective star

The factor is defined only a priori over the algebraic closure, but its
projective center is `F`-rational.  If `A!=0`, two distinct captured
`F`-rational pairs have different `b` components and

```text
B/A=-(a_i-a_j)/(b_i-b_j) in F.
```

Then `-C/A=a_i+(B/A)b_i` lies in `F[X]_<6`.  Every captured line
`c_gamma=a_i+gamma*b_i` passes through this codeword at the common slope
`gamma_*=B/A`.

If `A=0`, primitivity gives nonzero constant `B`, and every captured pair
has the same direction codeword `b_i=-C/B in F[X]_<6`; this is the common
projective center at slope infinity.  The degree-one branch is therefore an
`F`-rational projective star.
