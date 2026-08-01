# Audit

1. The elimination starts from the saturated common ideal, not the raw three
   minors.
2. The deployed computation uses an ordinary polynomial block ring; the
   unsupported large-characteristic function-field backend is not invoked.
3. The principal elimination claim is exact and prints its sole generator.
4. The trace descent uses the existing guard `b!=0`.
5. Factors `t=+-i` in the discriminant are already forbidden; the residual
   quadratic is not asserted to be a square or nonsquare uniformly.
6. No signed-pair, colored-edge, route, row, or Prize conclusion is inferred.
