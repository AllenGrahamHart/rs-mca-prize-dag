# Audit

1. The collision parameter is excluded from supported slopes using the
   exact vertical-fiber gcd, not by assuming corrections are unsupported.
2. The common split-biform root at the collision is derived from the Pade
   syzygy before the vertical-fiber gcd is applied.
3. `x_* notin U_0` removes the actual-inside factor; unsharedness removes
   the padded-heavy factor.
4. The interpolation uses all classified rows and is valid because each
   coefficient has `X`-degree at most `n<|X|`.
5. The derivative weights differentiate the Lagrange basis; they are not
   guessed finite-difference coefficients.
6. Exact order two of `G(t,x_*)` uses the Pade syzygy and the unequal
   orders two and six, so no cancellation assumption is hidden.
7. `R_2!=0` is retained. The gate is not weakened to mere double
   divisibility.
8. No line of the Smith router is declared empty.
