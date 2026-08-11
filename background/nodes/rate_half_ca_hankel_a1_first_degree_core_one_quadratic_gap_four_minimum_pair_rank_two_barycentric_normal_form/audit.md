# Audit

1. With `m=r_sigma+3`, the coefficient-chain moment range
   `0..r_sigma` is exactly `0..m-3`; its Vandermonde nullspace has dimension
   two, not one.
2. The vectors in `(3)` use the monic `L_X`; all derivatives are nonzero
   because the domain points are distinct.
3. Rank one is excluded separately. It is not inferred merely because the
   pair union exceeds the old boundary.
4. The orientation rule is used only for the full-locator triple estimate.
   The two-simple zero/zero case uses the sharper fact that both endpoint
   locators have no padded roots.
5. `tau` lies in the common gcd because at least two distinct forms vanish
   there. `sigma` does not because every difference point is absent from its
   locator.
6. Root counts are projective and multiplicity-free: every row form is
   squarefree of exact degree `e`.
