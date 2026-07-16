# Proof

Condition (RC1) is exactly

```text
H_i(U-gamma_i q)=0.
```

Stacking these equations proves `(U,q) in ker M_F`. Every vector in `K` is
annihilated by every `H_i`, so `K x K` is an eight-dimensional subspace of
the kernel. Since `q notin K`, the pair `(U,q)` does not belong to that
subspace. Hence the kernel has dimension at least nine, proving (RC3) by
rank-nullity. The exclusion criterion is its contrapositive.

For the six-face law, let `F_X` be the unique degree-at-most-five interpolant
to a function `f` on `X`, and write its top terms as

```text
F_X(T)=c_5 T^5+c_4 T^4+lower terms.
```

The degree-at-most-four interpolant on `X\{x_i}` is

```text
F_X(T)-c_5 product_(j!=i)(T-x_j).
```

The coefficient of `T^4` in the product is
`-sum_(j!=i)x_j`. Therefore

```text
[X\{x_i}]f
 = c_4+c_5(sum_j x_j-x_i),
```

which has the form (RC4). Taking the quotient for `f=U` and `f=q` gives
(RC5).

A nonconstant fractional-linear map is injective wherever its denominator is
nonzero. Thus if two defined facet colors agree, the map in (RC5) must be
constant, and all defined colors agree. If it is nonconstant, all defined
colors are distinct. This proves the stated dichotomy and completes the
certificate interface.
