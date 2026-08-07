# f_scale_recursion proof

This proof covers the multiplicative `M`-pullback statement in the node. It
does not claim the separate reciprocal/Chebyshev analogue mentioned in the
ledger notes.

Assume `M | n` and `M | j`. Let `pi : H -> H'` be the quotient map
`x -> x^M`, so `|H'| = n/M`. A locator in the multiplicative periodic stratum
has the form

```text
ell(X) = g(X^M).
```

The coefficient map

```text
g(Y) -> g(X^M)
```

is linear and injective: it places the coefficients of `g` in the exponents
divisible by `M` and zeroes all other coefficients.

For `x in H`,

```text
ell(x) = 0  iff  g(x^M) = 0.
```

Each point of `H'` has exactly `M` preimages in `H`, so `ell` has exact
support size `j` on `H` exactly when `g` has exact support size `j/M` on
`H'`.

Let `P` be a linear flat of locators at scale `n`. Intersect `P` with the
linear subspace of `M`-pullback locators and apply the inverse coefficient map
above. The image is a linear flat `P'` at scale `n/M`, with dimension at most
`dim P`, and the construction gives a bijection

```text
P cap D_j^per(M)  <->  P' cap D'_(j/M).
```

Thus periodic points in `F(n)` are quotient-instance points at scale `n/M`.
Splitting a plane section into its primitive part plus the periodic branches
gives

```text
F(n) <= F_primitive(n) + sum_{M | gcd(n,j), M > 1} F(n/M),
```

with recursion terminating at smaller scales.
