# Proof - L1 split-pencil content is exact-shell excess

## 1. Content is intrinsic

Two bases of the free rank-two module `M_U` differ by a matrix in
`GL_2(F[X])`.  The old coordinates are polynomial linear combinations of the
new coordinates and conversely.  Therefore the two coordinates generate the
same ideal in `F[X]`.  Its monic generator `G` is basis independent.

Because `G` divides both `A` and `B`, equation `(CD1)` gives `G|W` and
`G|N`.  The locator `W` is a squarefree divisor of `Omega`, so `G` is also a
squarefree product of distinct factors `X-x` with `x in H`.

## 2. A content root is an extra agreement

Write

```text
A=GA_0,   B=GB_0,   W=GW_0,   N=GN_0.
```

Then `(W_0,N_0)=A_0g_1+B_0g_2` belongs to `M_U`, and `N_0=W_0c`.
For `x in Z_H(G)`, squarefreeness of `W` gives `W_0(x)!=0`.  Membership in
`M_U` therefore yields

```text
W_0(x)c(x)=N_0(x)=W_0(x)U(x),
```

so `U(x)=c(x)`.  Every point outside `Z_H(W)` is also an agreement directly
from `N(x)=W(x)U(x)` and `N=Wc`.

## 3. Every extra agreement is a content root

Let `x in Z_H(W)` and suppose `U(x)=c(x)`.  Since `W` is squarefree, put

```text
(W_x,N_x)=(W/(X-x),N/(X-x))=(W_x,W_x c).
```

For `y in H\{x}`, the module relation follows by dividing the relation for
`(W,N)` by `y-x`.  At `x`, it follows from `U(x)=c(x)` and `W_x(x)!=0`.
Hence `(W_x,N_x) in M_U`.  Write it uniquely as
`A_xg_1+B_xg_2`.  Multiplication by `X-x` and uniqueness of coordinates in
the basis give

```text
A=(X-x)A_x,       B=(X-x)B_x.
```

Thus `X-x|G`.  Combining this with the previous step proves `(CD3)`.  Since
`H\Z_H(W)` has `m` points and `G` has `r` distinct roots in `H`, the complete
agreement is `m+r`.  Exactness at level `m` is therefore equivalent to
`r=0`, or `G=1`.

## 4. Canonical descent

After dividing by the full content, `gcd(A_0,B_0)=1`.  Equation `(CD3)` says
that `W_0` has exactly the disagreement roots of `c`; it has degree
`omega-r=n-(m+r)`.  Thus `(W_0,N_0)` is the unique complete-support member
for `c` at level `m+r`.  Conversely, choosing an `m`-subset of an exact
`a`-point agreement set multiplies that primitive member by the locator of
the `a-m` omitted agreement points.  This produces every raw level-`m`
member and makes its coefficient content exactly that locator.  The claimed
first-match partition and binomial multiplicities follow.
