# Proof

The vector space of polynomials of degree less than `k` has dimension `k`.
Evaluation on the `r` distinct points of `R` has rank `r`: arbitrary values on
`R` are attained by interpolation with a polynomial of degree less than `r`.
Thus the fiber over `U|_R` is a nonempty affine space of dimension `k-r` and
has exactly `q^(k-r)` elements.

Fix `x in L\R`. On the kernel of evaluation on `R`, evaluation at `x` is a
nonzero functional. Indeed, the locator

```text
L_R(X) = product_(a in R) (X-a)
```

has degree `r<k`, vanishes on `R`, and is nonzero at `x`. Consequently the
additional equation `f(x)=U(x)` cuts the affine fiber in a hyperplane of
exactly `q^(k-r-1)` elements.

There are `n-r` possible extra agreement points. The union bound therefore
shows that at most `(n-r)q^(k-r-1)` members of the original fiber agree with
`U` somewhere outside `R`. Subtracting proves the stated lower bound for
polynomials whose exact agreement set is `R`.

When `k-r` grows, this count is not bounded by `n^b` for any fixed exponent in
the official large-field regime. Even when the deficit is bounded, it cannot
be absorbed into the petal ledger's constant-sized residual allowance without
additional constraints. Hence support canonicalization and interpolation
alone cannot discharge the sub-`k` clause of G3.

