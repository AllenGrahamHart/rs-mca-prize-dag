# Audit

1. The kernel vector is chosen from a full-rank minor. Its `U`-degree is
   bounded by the number of quadratic-block columns, not by the matrix size
   times two.
2. Clearing scalar denominators and removing a common polynomial factor do
   not increase either bidegree.
3. The resultant is taken in `U`. Coprimality is imposed in `F[U,Z]`, so a
   genuinely `U`-dependent denominator gives a nonzero resultant.
4. Specializations where `B(U,gamma)` becomes constant are not charged to
   the resultant. More than `t` such specializations force every positive
   `U` coefficient of `B` to vanish globally.
5. Once `B` is static, coefficients of `A` above degree two vanish on the
   whole class and are killed by the same degree-`t` root count.
6. The residual signs follow
   `Q_U=U^2M_0-2UM_1+M_2`; changing them does not affect gcd degree but would
   invalidate certificate replay.
7. The theorem reduces the object but does not infer a genericity bound for
   the three residuals. Their coefficients come from the exact packet and
   must be paid uniformly.
8. The class factor divides `P_Z`. The closure target is therefore the gcd
   with `P_Z`, not the unnecessarily stronger unrestricted residual gcd.
