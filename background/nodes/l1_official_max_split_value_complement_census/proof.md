# Proof - L1 official maximal split-value complement census

## 1. Complement and leading gap

Distinct complete fibers of `P` are disjoint. If there are `h` of them, they
occupy `hp` points of `H`, so their product has the monic complement `C` of
degree `u=n-hp`, proving `(MSC1)`.

First suppose `Q=0`. The map `x -> x^p` is a permutation of `H`, because
`p` is coprime to `n`; it has no `p`-point fiber. Thus `Q!=0` whenever
`h>=2`.

Put `r=deg Q`, `j=p-r`, and `q=lc(Q)`. Because `G` is monic of degree `h`,
the first term below the leader of `G(P)` is

```text
h q Z^(hp-j).
```

Indeed it comes from `P^h`; terms containing two copies of `Q` have gap at
least `2j`, and the next outer term has gap at least `p`. Here `h<=m<p`, so
`hq!=0`. In the product with monic `C`, every coefficient below the leader
must vanish until the constant term of `Z^n-alpha`. If `j>u`, this would
force `C(0)=0`. Hence `j<=u`; comparison through gap `j` gives exactly the
zero string and coefficient in `(MSC2)`.

The first-checkpoint reduction supplies `r<=2p-d-1`, so

```text
j=p-r>=d-p+1.
```

This proves the zero string in `(MSC3)` and emptiness when `ell_h<=0`.

## 2. The complement determines the pencil

Let `B_beta` be any complete fiber. For every `1<=a<=p-1`, all fiber
locators `P-beta` have the same nonconstant coefficients, so Newton's
identities give one common power sum

```text
S_a(B_beta)=sum_(x in B_beta) x^a.
```

The sum of `x^a` over the multiplicative coset `H` is zero because `a<n`.
The `h` fibers and the complement partition `H`, whence

```text
h S_a(B_beta)=-S_a(C).                                  (1)
```

Both `h` and every `a<p` are invertible in the field. Equation `(1)` and
Newton's identities therefore recover all coefficients of `P` except its
constant from `C`. The normalization `P(0)=0` recovers the last coefficient.
Thus `C` determines `P`; if a composition exists, the quotient in `(MSC1)`
then determines `G` uniquely.

At depth `d`, write `ell_h=u-d+p`. The forced zero string leaves precisely
the coefficients `c_0,...,c_(ell_h-1)` unknown in `C`. For any `ell_h`
distinct roots `x_1,...,x_(ell_h)` of `C`, their equations are

```text
sum_(i=0)^(ell_h-1) c_i x_a^i=-x_a^u       (1<=a<=ell_h).
```

The coefficient matrix is Vandermonde and invertible. Hence each `ell_h`-set
of domain roots belongs to at most one candidate complement. Every valid
squarefree degree-`u` complement contributes exactly `binom(u,ell_h)` such
subsets, and these families are disjoint between complements. Therefore
there are at most

```text
floor(binom(n,ell_h)/binom(u,ell_h))
```

complements. Each gives at most one normalized pencil, and each pencil has
`binom(h,2)` unordered value pairs. This proves `(MSC4)`.

## 3. Exact terminal exclusion

Now specialize to maximal capacity `h=m`, so `u=s`. At `d=p+s-1`, the gap
is `j=s`, so `C=Z^s-b` with `b!=0`. Reduce `Z^n`
modulo this binomial. Divisibility of `Z^s-b` into `Z^n-alpha` forces
`s|n`; because `n=mp+s` and `gcd(s,p)=1`, it follows that `s|m`.

The atlas itself now removes the seven rows with `s>m`. On each of the nine
remaining rows, `s=m`. We prove that a terminal decomposition in this case
requires `p=1 mod m`.

Put `Y=Z^m`. Since `C=Z^m-b` divides the domain binomial,

```text
D(Z)=(Z^(m(p+1))-b^(p+1))/(Z^m-b)
    =A(Y),
A(Y)=Y^p+bY^(p-1)+...+b^p.                              (2)
```

In characteristic `p`, direct differentiation gives

```text
D'(Z)=-mb Z^(m-1)(Z^m-b)^(p-2).                         (3)
```

On the other hand `D=G(P)` and the terminal gap gives
`deg P'=p-m-1`. For a root `gamma` of `G'`, the degree-`p` polynomial
`P-gamma` divides `D'`. It has at least

```text
p-deg(P')=m+1
```

distinct roots over the algebraic closure. Equation `(3)` has exactly the
`m+1` distinct roots consisting of zero and the roots of `Z^m-b`.
Different `gamma` give disjoint fibers, so `G'` has only one distinct root.
As `m<p`, this means

```text
G(T)=(T-gamma)^m+delta.                                  (4)
```

Set `R=P-gamma`. Equations `(2)--(4)` give `D-delta=R^m`. For every
`m`-th root of unity `zeta`, invariance of `D` under `Z -> zeta Z` and the
integral-domain factorization of two `m`-th powers imply

```text
R(zeta Z)=zeta^p R(Z).
```

Thus every exponent in `R` is congruent to `p` modulo `m`. If
`u in {1,...,m-1}` is the residue of `p`, then

```text
R(Z)=Z^u S(Z^m).                                        (5)
```

Since `R(0)=0`, equation `(2)` forces `delta=b^p`. As a polynomial in `Y`,
`A(Y)-b^p` has exact order one at zero, whereas `(5)` has order
`u mod m` after taking the `m`-th power. Therefore

```text
1=u+m ord_0(S),
```

so `u=1`, proving `p=1 mod m`. Every one of the nine official `s=m` rows
has instead `p=-1 mod m` and `m>=4`. This proves `(MSC5)`.
