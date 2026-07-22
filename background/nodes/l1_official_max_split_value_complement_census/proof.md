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

## 3. Polynomial abc dichotomy

Translate the inner polynomial by a constant and depress the outer
polynomial. Since `h<p`, there are a monic degree-`p` polynomial `R`, a
polynomial `J` of degree at most `h-2`, and
`nu=ord_0(R)` such that

```text
G(P)=R^h+J(R).
```

The domain identity becomes

```text
R^h C+(J(R)C+alpha)=Z^n.                                (2)
```

The first summand has exact valuation `h nu`. Since `h nu<=hp<n`, the
second has the same valuation. Divide `(2)` by `Z^(h nu)`. The three
resulting terms are pairwise coprime: any common nonzero root would divide
their monomial sum, and exact valuation removes zero.

If the reduced triple is not entirely in `F[Z^p]`, polynomial
Mason--Stothers gives

```text
n-h nu
 <= (p-nu+u)+((h-2)p+u-h nu)+1-1
 = (h-1)p+2u-(h+1)nu.                                  (3)
```

Here the first radical is bounded by the roots of `R/Z^nu` and `C`; the
second by its degree; and the monomial contributes one root. Substituting
`n=hp+u` into `(3)` gives

```text
p-u+nu<=0.                                              (4)
```

Thus the non-Frobenius branch gives `nu<=u-p`. In the other branch, the
reduced triple is Frobenius-degenerate. In particular

```text
(R/Z^nu)^h C in F[Z^p].                                 (5)
```

Let `c` be any root of `C` over the algebraic closure and set
`e_c=ord_c(R)`. The domain binomial is squarefree and `c!=0`, so `(5)` gives

```text
p divides h e_c+1.                                      (6)
```

Let `e_h in {1,...,p-1}` be the unique residue with `h e_h+1=0 mod p`.
Every nonnegative solution of `(6)` is congruent to `e_h` modulo `p`; since
`deg R=p`, necessarily `e_c=e_h`. Summing multiplicities over the `u`
distinct roots of `C` gives `u e_h<=p`, proving `(MSC5)`.

If `h<m`, then `u=n-hp>=p+s>p`, so `u e_h<=p` is impossible and `(MSC6)`
follows. If `h=m`, then `u=s<p`, so `nu<=s-p` is impossible; the Frobenius
arm is forced and gives `(MSC7)`.

The atlas verifier computes `e_0=-m^(-1) mod p` for each of the 16 exact
`m>=3` rows and checks `s e_0>p` in every case. No maximal-capacity record
exists on any such row, proving `(MSC8)`.
