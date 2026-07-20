# Proof - L1 marked constant-shift multistrip exclusion

Put

```text
F'=JF,       W'=JW,       D=d+v.
```

As in the first marked strip, `J=V_iJ_i` and `(MT1)` imply

```text
P-a_i | W'-c_iF'                                  (1)
```

for every `i`. Exact saturation gives

```text
gcd(F',W')=J,       deg gcd(F',W')=v.              (2)
```

The strip inequalities in `(MT2)` give

```text
m ell<D<(m+1)ell.
```

There are therefore unique `P`-adic block decompositions

```text
F'=sum_(j=0)^m P^jF_j,       W'=sum_(j=0)^m P^jW_j,
deg F_j,deg W_j<ell.                                  (3)
```

For each coefficient position `0<=r<ell`, the corresponding vector in the
`2(m+1)` block coefficients lies in the kernel of the matrix with rows

```text
(-c_i,-c_i a_i,...,-c_i a_i^m,1,a_i,...,a_i^m).       (4)
```

## 1. The row rank is at most `2m`

If the row rank were at least `2m+1`, its kernel would have dimension at most
one. It cannot be zero because `F'` is nonzero. Hence every coefficient
vector in `(3)` would be a scalar multiple of one vector, giving

```text
F'=H A(P),       W'=H B(P),       deg A,deg B<=m.       (5)
```

Since `deg F'=D>m ell`, one has `deg A=m` and

```text
deg H=D-m ell=d+v-m ell>v.                              (6)
```

This contradicts `(2)`. The row rank is therefore at most `2m`, so its
kernel has dimension at least two.

## 2. Every kernel pair has one primitive direction

Represent a kernel vector by a pair `(A(Z),B(Z))` of polynomials of degree at
most `m`. Equation `(4)` says

```text
B(a_i)=c_iA(a_i)                                        (7)
```

for all `i`. For any two kernel pairs `(A_j,B_j)` and `(A_k,B_k)`, the
polynomial

```text
A_jB_k-A_kB_j
```

has degree at most `2m` and vanishes at the `t>=2m+1` distinct labels.
It is therefore zero.

Fix one nonzero pair and divide it by the gcd of its two entries, obtaining a
primitive pair `(A,B)`. The preceding cross-product identity and
`gcd(A,B)=1` imply that every kernel pair is

```text
(h_jA,h_jB)                                             (8)
```

for some polynomial `h_j`. Put `e=max(deg A,deg B)`. Since the kernel has at
least two linearly independent pairs and every pair in `(8)` has degree at
most `m`, the multiplier space has dimension at least two. Hence

```text
e<=m-1.                                                 (9)
```

Here `A` is nonzero: if one kernel pair had first component zero, its second
component would vanish at all `t>m` labels by `(7)`, so the pair itself would
be zero. Thus the factorization of `F'` below is nonvacuous.

## 3. The primitive direction is a forbidden common factor

Expand every coefficient vector in `(3)` in a kernel basis and use `(8)`.
For polynomials `H_j(X)` of degree below `ell`, this gives

```text
F'=A(P) sum_j H_j h_j(P)=A(P)H,
W'=B(P) sum_j H_j h_j(P)=B(P)H.                         (10)
```

The first equality and `(9)` imply

```text
deg H
 =D-deg A(P)
 >=D-(m-1)ell
 =d+v-(m-1)ell
 >v.                                                     (11)
```

Thus `H` is a common divisor of `F'` and `W'` of degree larger than `v`,
contradicting `(2)`. This proves `(MT2)`.

For `(MT3)`, choose the selected dense common-pencil petals and take their
missing-set locators as the `V_i`. Their total degree satisfies `v<=p`, so
`d+p<(m+1)ell` implies the upper inequality in `(MT2)`.

For `(MT4)`, let `T` be the total number of dense petals. The sparse supports
have total size at most `p`, while each dense support has size at most `ell`.
Thus the total petal agreement satisfies

```text
h<=T ell+p.
```

The list threshold and strict background cap give

```text
d<=h+r-ell<=T ell+p-1,
```

which is equivalent to the lower bound in `(MT4)`. If `T>=2m+1`, choose any
`2m+1` dense petals. Their selected mark degree is at most `p`, so `(MT3)`
excludes the contributor. Hence `T<=2m`. Finally, `m ell<d` and `p<ell`
make the ceiling at least `m`; if `d>m ell+p-1`, it is at least `m+1`.
