# Audit

1. The trace quadratic is `t(Y-2)^2+4(t-1)^2`; changing the center from two
   or dropping the leading `t` is a detected mutation.
2. Both roots are retained. Squaring the source formula is exact only because
   the two roots correspond to the two available square roots `u,-u`.
3. The scalar resultant uses `S^2-4T`, not `S^2-2T`, because
   `Y+2=S^2/T`.
4. Scalar passage and trace passage must use the same root; separate
   existential tests are insufficient. The common-coefficient gcd enforces
   this selector.
5. `T` is nonzero on a complete nonharmonic pencil, so clearing `T^2` loses
   no survivor.
6. The constant gate is necessary, not sufficient, and does not authorize a
   dense computation of `H_(2^38-1)`.

