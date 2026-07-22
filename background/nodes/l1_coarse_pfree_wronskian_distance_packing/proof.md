# Proof - L1 coarse p-free Wronskian distance packing

## 1. P-free equality gives all moments through depth d

Every positive integer `j` has a unique form `j=p^v u` with `p` not dividing
`u`. In characteristic `p`,

```text
S_j(A)=S_u(A)^(p^v).                                  (1)
```

Since `u<=j<=d`, equality of the p-free coordinates implies
`S_j(A)=S_j(B)` for every `1<=j<=d`. Removing the common set `C` gives

```text
S_j(X)=S_j(Y),       1<=j<=d.                         (2)
```

## 2. Logarithmic-derivative Wronskian

Let

```text
F_X(Z)=product_(x in X)(Z-x),
F_Y(Z)=product_(y in Y)(Z-y).
```

They are coprime squarefree monic polynomials of degree `t`. At infinity,

```text
F_X'/F_X=t/Z+sum_(j>=1) S_j(X)/Z^(j+1),
F_Y'/F_Y=t/Z+sum_(j>=1) S_j(Y)/Z^(j+1).
```

By `(2)`, their difference is `O(Z^(-d-2))`. Hence the polynomial

```text
W=F_X'F_Y-F_XF_Y'                                    (3)
```

satisfies

```text
deg W<=2t-d-2                                         (4)
```

whenever it is nonzero.

If `W=0`, then `(F_X/F_Y)'=0`. A finite field is perfect, so a rational
function with zero derivative lies in `F(Z^p)` and every zero and pole over
an algebraic closure has valuation divisible by `p`. But `F_X/F_Y` has
simple zeros at `X` and simple poles at `Y`. Thus `W=0` forces `t=0` and
`A=B`. For distinct sets, `W` is nonzero; `(4)` then forces

```text
2t-d-2>=0,
```

which proves `(PWD2)`.

## 3. Constant-weight packing

Distinct members of one fiber intersect in at most `a-tau` points. With
`s=a-tau+1`, no `s`-subset of `H` can occur in two fiber members. Counting
pairs consisting of a fiber member and one of its `s`-subsets gives

```text
|Phi_free^(-1)(z)| binom(a,s)<=binom(n,s),
```

proving `(PWD4)`.

Finally set `d=a-k`. If `d=2u`, then `tau=u+1` and
`s=a-u=(a+k)/2`. If `d=2u+1`, then `tau=u+2` and
`s=a-u-1=(a+k-1)/2`. This proves `(PWD5)`.

## 4. Official-cap route diagnosis

Write `r=n-a`. Cancelling factorials gives

```text
binom(n,s)/binom(a,s)
 =product_(i=0)^(r-1) (n-i)/(n-s-i).                 (5)
```

The denominators are positive because `s<=a`. If `s>=n/2`, every factor in
`(5)` is at least two: this is equivalent to `n-i>=2(n-s-i)`, and its
right-minus-left slack is `2s-n+i>=0`. Hence the ratio is at least `2^r`,
and so is its integer floor. The official strict cap `q<2^256` gives

```text
floor(q/2^128)<2^128.
```

Thus the packing upper bound itself is above the finite payment whenever
`r>=128`, proving `(PWD6)--(PWD7)`. This compares two upper bounds and makes
no assertion that a fiber of that size exists.

For comparison, equality of all first `d` elementary locator coefficients
would make `F_A-F_B` have degree at most `a-d-1=k-1`. Its common-root
locator divides this nonzero difference, so `|A intersect B|<=k-1` and
`t>=d+1`. Coarse p-free equality does not imply those elementary checkpoint
equalities in characteristic `p`; the `F_4` fixture attains `t=2<3=d+1`.
