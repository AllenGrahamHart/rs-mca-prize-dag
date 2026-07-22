# Audit

1. Use the unnormalized numerators in the `M_1` Hankel pairing; inserting
   `p_i=q_(i+1)/q_1` there would change the source weights.
2. Squarefreeness of `A` converts pointwise annihilation into the polynomial
   divisibility used in `(HNR1)`.
3. Exactly one factor of `A` cancels against the `A(t)^2` in the Forney
   support weight.
4. `gcd(A,B_T)=1`, so the inverse in `(HNR3)` exists. It is needed only
   modulo the support locator, not modulo the degree-`2e` exceptional locator.
5. The Lagrange identity extracts the coefficient of degree `h-1`, not the
   constant or leading coefficient of the unreduced numerator.
6. The sum of finite residues of `P/Q dX` with monic `Q` and
   `deg P<=deg Q-1` is `[X^(deg Q-1)]P`; this fixes the sign in `(HNR4)`.
7. The boundary term can occur only when both annihilator numerators jointly
   attain the maximum quotient degree `deg K=2e+2`.
8. Bases of the two deficiency spaces must be retained. Testing one pair
   discards up to `d^2-1` exact equations when `d>1`.
