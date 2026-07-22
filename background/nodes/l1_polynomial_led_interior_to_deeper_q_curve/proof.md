# Proof - L1 polynomial-led interior cells are deeper-Q curves

## 1. Product-prefix recursion

For a degree-below-`k` codeword `P` with at least `m` agreements, write its
agreement locator `L_T` and cofactor `R` as

```text
U-P=L_T R.
```

Since `U` is monic of degree `m+e` and `L_T` is monic of degree `m`, `R` is
monic of degree `e`.  The condition `deg P<k` says that the top

```text
(m+e)-k=w+e
```

nonleading coefficients of `L_T R` equal those of `U`.  If
`R=X^e+r_1X^(e-1)+...+r_e`, the coefficient at depth `j` is

```text
sum_(l=0)^min(j,e) r_l a_(j-l).                     (1)
```

For `1<=j<=e`, equation `(1)=z_j` solves triangularly for `r_j`, giving the
first recurrence in `(DQ2)`.  Because `e<=k`, one has `e+w<=m`; for
`e<j<=e+w`, the coefficient of `a_j` is `r_0=1`, so the same equation solves
recursively for `a_j`, giving the second recurrence.  Therefore the product
condition is equivalent to

```text
(a_1,...,a_(e+w))=theta_z(s),       R=R_s.           (2)
```

Conversely `(2)` makes all `w+e` top coefficients cancel, so
`P=U-L_TR_s` has degree below `k`.  This proves the unguarded bijection.

## 2. Exactness guard

At a domain point outside `T`, the locator `L_T` is nonzero.  Equation
`U-P=L_TR_s` gives an additional agreement exactly when `R_s` vanishes there.
The complement locator `Omega/L_T` has precisely those outside points as
roots.  Hence the complete agreement set is exactly `T` if and only if

```text
gcd(R_s,Omega/L_T)=1.                                (3)
```

Imposing `(3)` on the unguarded bijection proves `(DQ3)` and `(DQ4)`.  A
fixed support of size at least `k` has only one explaining codeword, so no
member is duplicated.  Different `s` have different first `e` locator
coefficients, making the sum disjoint.

## 3. Q bound accounting

Dropping `(3)` and then bounding every one of the `|B|^e` distinct fibers by
the maximum proves `(DQ5)`.  Substitution of the displayed discrete Q bound
and the identity

```text
|B|^e binom(n,m)|B|^(-(w+e))=binom(n,m)|B|^(-w)
```

gives `(DQ6)`.  The same calculation shows why ambient means cancel the
depth cost while additive one-per-slice errors do not.
