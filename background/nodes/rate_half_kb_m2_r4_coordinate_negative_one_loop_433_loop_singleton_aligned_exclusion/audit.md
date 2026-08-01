# Audit

1. All four root-sign rows and both `bc` signs are routed explicitly.
2. Only source/target collision factors are stripped.
3. Rational substitutions are protected by `b!=0`.
4. The product elimination uses `x=t^2`; it does not assume that an
   extension-field square root lies in the deployed base field.
5. Base-field emptiness is proved from irreducible quadratic factors, not
   inferred from the `F_29` or `F_41` scans.
6. No other matching cell is claimed.
