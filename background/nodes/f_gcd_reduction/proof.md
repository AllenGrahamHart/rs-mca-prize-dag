# f_gcd_reduction proof

Let `g` be the common divisor of every locator in `P cap D_j`, with
`deg(g) = w`. The set of polynomials divisible by `g` is a linear subspace.
Therefore the members of `P` that lie in `D_j` and share this common divisor
can be written uniquely as

```text
ell = g * ell'
```

with `deg ell' = j - w`.

Division by `g` is linear on this subspace, so the image is contained in a
linear flat `P'` with `dim P' <= dim P`. It is injective on `P cap D_j`,
because multiplication by `g` recovers the original locator.

After dividing by the maximal common divisor, the image has trivial common gcd.
Thus the general F problem reduces to the gcd-trivial case plus the paid
tangent/common-divisor branch represented by `g`.
