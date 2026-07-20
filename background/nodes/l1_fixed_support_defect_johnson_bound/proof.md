# Proof - L1 fixed-support defect Johnson bound

Take two members `(F_1,W_1),(F_2,W_2)` of `Z` and form

```text
Delta=W_1F_2-W_2F_1.                                    (1)
```

If `Delta=0`, primitivity gives equality of the pairs. Indeed,
`gcd(F_1,W_1)=1` implies `F_1|F_2`; the locators have the same degree and are
monic, so `F_1=F_2`, and then `W_1=W_2`. Thus `Delta` is nonzero for distinct
pairs.

Both pairs obey the same labelled equations on `X`, so `Delta` vanishes on
every point of `X` and

```text
L_X | Delta.                                             (2)
```

Put `I=D_1 intersect D_2`. Both terms in `(1)` are divisible by `L_I`, hence
`L_I|Delta`. The petal support and core are disjoint, so `L_X` and `L_I` are
coprime. Therefore

```text
L_X L_I | Delta.                                        (3)
```

Since `deg Delta<=2d`, nonvanishing and `(3)` give

```text
h+|I|<=2d,
|D_1 intersect D_2|<=2d-h=r_J.                          (4)
```

If `r_J<0`, no two distinct pairs exist. This proves the first two claims.

Now suppose `r_J>=0` and write `m=|Z|`. For `x in C`, let `a_x` be the
number of defect sets in the family that contain `x`. Counting incidences and
pairwise intersections gives

```text
sum_x a_x=md,
sum_x binom(a_x,2)<=binom(m,2)r_J.                       (5)
```

Cauchy-Schwarz gives `sum_x a_x^2>=m^2d^2/N`. Substituting this in `(5)`
yields

```text
m^2d^2/N-md<=m(m-1)r_J,
m(d^2-Nr_J)<=N(d-r_J).                                  (6)
```

Division by the positive denominator proves `(JB4)`.

For the aggregate, orient each of the `M` petals as sparse or dense and
record the at most `P` exceptional points. The number of exact petal-support
patterns is at most

```text
2^M(P+1)n^P.                                            (7)
```

On every positive-denominator cell, `(JB4)` is at most `n^2`: its denominator
is a positive integer and its numerator is at most `n^2`. There are at most
`n` defect degrees. Using `2^M<=n^(1/c_0)` in `(7)` proves `(JB5)`. No field
factor or missing-equation syndrome factor is present because the whole
exact support is fixed before the packing argument.

For `e>=1`, equation `(JB2)` says `r_J=e-1`; hence failure of the strict
Johnson condition is exactly `(JB6)`. The list threshold is
`h+r_bg>=d+ell`, where a word has at most `b` background agreements. Thus
`h>=d+ell-b=d+g`, which gives

```text
r_J=2d-h<=d-g.                                          (8)
```

Combining `(JB6)` and `(8)` proves `(JB7)`. The quadratic
`d^2-Nd+Ng` is nonpositive only if its discriminant
`N^2-4Ng` is nonnegative, equivalently `g<=N/4`, and then only between
its two real roots.
