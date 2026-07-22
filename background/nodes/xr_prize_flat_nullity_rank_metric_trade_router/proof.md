# Proof

For a core on `t` distinct slopes, every trade matrix `T` satisfies the two
row equations

```text
1^T T=0,       gamma^T T=0.                           (1)
```

The two check vectors are independent. Their common kernel `U` has dimension
`m=t-2`. Choose any full-column-rank matrix `J:F^m->U`. Every trade has a
unique compression

```text
T=J Tbar,       Tbar in Mat_(m x M)(F),                (2)
```

and `rank(T)=rank(Tbar)`. The compressed trade space has the same dimension
as the original one, hence dimension at least `D` by the general compiler.

We use the elementary rank-metric Singleton bound. If a linear subspace
`L subset Mat_(m x M)(F)` has no nonzero matrix of rank at most `r`, delete
any fixed `r` rows. The deletion map is injective on `L`: an element in its
kernel is supported on at most `r` rows and therefore has rank at most `r`.
Consequently

```text
dim L<=(m-r)M.                                        (3)
```

Taking the contrapositive of `(3)` with `m=t-2` proves `(RM2)`.

Put `q=ceil(D/M)`. Then `D>(q-1)M`. Applying `(RM2)` with

```text
r=m-q+1=t-1-q
```

proves `(RM3)`. The actual trade-space dimension is at most `mM`, so
`1<=q<=m` and this rank bound is well-defined.

If no rank-one trade exists, `(3)` with `r=1` gives

```text
s(t-2)+e+1<=(t-3)[a+s+(h t-e)/2].                    (4)
```

Multiplying by two and cancelling `2s(t-3)` gives `(RM4)`. If no rank-at-
most-two trade exists, the same calculation with `r=2` gives `(RM5)`.
For `t=3` and `t=4`, the compressed matrix has respectively one and two rows,
so the stated automatic conclusions also follow directly.

At `s=k-a`, use `e=0` in the strict reversals of `(RM4)` and `(RM5)`:

```text
2s+2>(t-3)(2a+h t),
4s+2>(t-4)(2a+h t).                                  (5)
```

Exact substitution of the first-open prize parameters gives last true
arities `12,9,9` and `18,13,13`. Since the left sides of the exact strict
reversals gain `(t-1)e` or `(t-2)e`, any positive excess only strengthens
the forcing. QED.
