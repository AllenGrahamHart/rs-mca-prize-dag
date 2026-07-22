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
