# Proof - L1 m=4, h=3 colored cyclic-code equivalence

The exact atlas lists four `m=4` Mersenne rows. Their characteristics are
Mersenne primes `2^r-1` with odd `r`, so `p=1 mod 3`. Hence `F_p` contains
the two primitive cube roots of unity.

Suppose first that `X_0,X_1,X_2` are three complete fibers of one normalized
degree-`p` pencil. Their monic locators differ only in their constants, so
Newton identities give one common power sum

```text
s_a=sum_(x in X_j) x^a,       0<=a<=p-1,              (1)
```

where `a=0` uses the common size `p`. Color the three exponent supports by
`1,omega,omega^2` and call the resulting word `b`. For every initial
frequency,

```text
B(zeta^a)=(1+omega+omega^2)s_a=0,
B^[2](zeta^a)=(1+omega^2+omega)s_a=0.                 (2)
```

Both words have coefficients in `F_p`, so Frobenius propagates their zeros
to the full closure `S`. This proves `(CC3-2)`.

Conversely, let a word satisfy `(CC3-2)`, and let `X_0,X_1,X_2` be its three
color classes. At an initial frequency `a`, write their power sums as
`s_0,s_1,s_2`. Membership of `b` and `b^[2]` in `C_M` gives

```text
s_0+omega s_1+omega^2 s_2=0,
s_0+omega^2 s_1+omega s_2=0.                          (3)
```

The two rows are independent and their common nullspace is spanned by
`(1,1,1)`. Hence `s_0=s_1=s_2` for every `0<=a<=p-1`. Newton identities for
`1<=a<=p-1` show that the three monic degree-`p` locators have identical
nonconstant coefficients. They therefore differ only by constants. Their
supports are disjoint and nonempty, so the constants are distinct. After
normalizing the common constant-free polynomial, the three sets are complete
split fibers of one pencil.

This gives at least three split values. On an `m=4` row, the maximal-value
theorem excludes four, so the value degree is exactly three. This proves the
equivalence.

Finally each nonzero color is a cube root of one, while zero stays zero, so
coefficientwise cubing gives the union indicator. Its zero count is

```text
4(p+1)-3p=p+4=N+3,
```

proving `(CC3-3)`.
