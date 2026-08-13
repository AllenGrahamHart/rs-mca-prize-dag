# Proof

## Forced polynomial-pair cores

Fix `e=130237` and cutoff `b=65521`.  In the high-core branch the preceding
absorption theorem pays the original family.  Assume the complementary
branch, so every selected line has actual total core at most 64796.

Every bank slot belongs to an exact layer `h>=b+1=65522` and has at least
two members.  The exact-layer incidence theorem gives its inside common core
size at least

```text
2*65522-130237 = 807.                              (IF1)
```

Indeed, for `h<e` the lower bound
`h-(e-h)/(lambda-1)` is nondecreasing in both `h` and `lambda`, so the
minimum occurs at the printed layer and size two.

Write the selected affine explanation line as

```text
c_gamma=a_i+gamma*b_i,       a_i,b_i in C.
```

Its inside common core is exactly the set of coordinates on which
`(r_0,r_1)=(a_i,b_i)`.  Peeling removes the entire line, so all selected
pairs `(a_i,b_i)` are distinct.

After 2,704 removed lines, use lower bound 807 and cap 64796 in the capped
convex envelope.  Exact arithmetic gives

```text
core budget = 18416037,
full caps   = 253,
remainder   = 44692,
charge      = 132203,
target      = 16645012.
```

The bank has `base=13961576` and `groups=1933560`, so its strict
pigeonhole threshold is still

```text
ceil((16645012-13961576+1)/1933560)=2.             (IF2)
```

The charge is monotone through earlier stages.  Thus an unsafe family forces
a 2,705th distinct line unless an earlier prefix, absorption, or packing
branch already proves safety.

## Weighted interpolation kernel

Let `E` be the gauged support, `|E|=e`, and give `(X,Y,Z)` weights `(1,5,5)`.
Let `V_264` consist of

```text
Q(X,Y,Z)=sum_(j,k) q_(j,k)(X)Y^j Z^k,
deg q_(j,k)<=264-5(j+k).
```

For `s=j+k`, there are `s+1` pairs `(j,k)` and `264-5s+1` possible
`X`-powers.  Hence

```text
dim V_264
 = sum_(s=0)^52 (s+1)(264-5s+1)
 = 131175.                                        (IF3)
```

Evaluation at the `e` received points defines a linear map

```text
V_264 -> F^E,
Q |-> (Q(x,r_0(x),r_1(x)))_(x in E).
```

Its kernel `I_264` therefore has dimension at least 938.

For a selected pair `(a_i,b_i)` and any `Q in I_264`, substitution gives a
univariate polynomial `Q(X,a_i(X),b_i(X))` of degree at most 264, because
`deg a_i,deg b_i<=5`.  It vanishes at every coordinate in the line's inside
core.  By `(IF1)` it has at least 807 distinct roots, so it is identically
zero.  Thus every selected pair is a common `F(X)`-rational zero of the
whole interpolation kernel.

## Coprime branch

Work over the algebraic closure of `F(X)`.  Suppose the nonzero members of
`I_264` have no common factor of positive `(Y,Z)` degree.  Pick one nonzero
member.  For each of its finitely many irreducible factors, some kernel
member is not divisible by that factor.  A generic constant linear
combination avoids their finite union, producing two coprime kernel members.

As polynomials in `(Y,Z)`, both have total degree at most

```text
floor(264/5)=52.
```

Affine Bezout therefore bounds their common zero set by `52^2=2704`, counted
with multiplicity.  The 2,705 distinct selected pairs forced by `(IF2)` are
distinct common zeros, a contradiction.

Hence every unsafe family forces a common interpolation factor of positive
`(Y,Z)` degree.  This proves the router but does not classify that factor.
