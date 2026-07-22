# Audit - L1 exact-shell complement Toeplitz normal form

## Checked axes

1. The domain locator is `Z^n-beta`, not only `Z^n-1`.
2. The derivative contributes `x/(n beta)`.
3. Extending the sum from `A` to `H` uses vanishing of the complement locator.
4. The exponent range is positive and strictly below `2n`.
5. The coset average contributes `beta`, which cancels the derivative factor.
6. The coefficient window is `n-w,...,n-1`, exactly `w` coordinates.
7. A degree-below-`k` shift times a degree-`r` complement stops below `n-w`.
8. Monicity makes the linear map affine on the divisor slice.
9. The exactness guard uses the cofactor `Q`, not the received word itself.
10. Toeplitz sections are not silently identified with locator-prefix fibers.

## Route effect

The moving-weight obstruction is normalized without invoking a max-fiber
conjecture. What remains is a clean extension of the upstream divisor problem:
flatness of primitive split divisors under received-word Toeplitz coefficient
windows, or a budgeted transport to prefix-affine windows.
