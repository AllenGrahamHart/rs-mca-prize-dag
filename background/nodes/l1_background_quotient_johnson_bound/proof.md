# Proof - L1 background-quotient Johnson bound

Let `I_X` be the unique degree-`<h` polynomial interpolating the received
word on `X`. For every compatible codeword `P`,

```text
L_X | P-I_X.
```

Define

```text
G_P=(P-I_X)/L_X.                                        (1)
```

Since `deg P<=N` and `deg I_X<h`, one has `deg G_P<=N-h=c`. The map
`P |-> G_P` is injective.

For `x in B`, define the derived received word

```text
V(x)=(U(x)-I_X(x))/L_X(x).                              (2)
```

The denominator is nonzero because the background and petal support are
disjoint. Whenever `P` agrees with `U` at `x`, equations `(1)--(2)` give
`G_P(x)=V(x)`. The list threshold gives at least

```text
r_bg>=d+ell-h=ell-s=u                                  (3)
```

such background agreements.

Choose canonically `u` agreement positions for every `G_P`. Two distinct
degree-at-most-`c` polynomials agree in at most `c` field points, so these
`u`-subsets of the `b`-point background have pairwise intersection at most
`c`. The constant-weight Johnson second-moment argument gives

```text
|Z|<=b(u-c)/(u^2-bc)                                   (4)
```

when the denominator is positive. Positivity and `u<=b` imply `u>c`, so the
numerator is nonnegative. The denominator is a positive integer and the
numerator is at most `n^2`, proving the final claim in `(BQ3)`.

At `p<=P`, the number of exact petal support patterns is at most
`2^M(P+1)n^P`, and there are at most `n` defect degrees. Multiplication by
the `n^2` cell bound and `2^M<=n^(1/c_0)` proves `(BQ4)`.

Finally `u=ell-s=ell-a+c` and `b=ell-g`, so failure of `(BQ2)` is exactly
`(BQ5)`. Intersecting it with the already-proved balanced strip gives
`(BQ5)--(BQ6)`. The equality fixture has two contributors at zero
denominator, proving strictness.
