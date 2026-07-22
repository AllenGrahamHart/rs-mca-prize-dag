# Audit - L1 m=4, h=3, nu=0, h=0 projective quarter certificate

1. The normalized quantities are shifted fiber products
   `lambda_i=beta_i-R(0)`, not the split values themselves.
2. Every `lambda_i` is nonzero, so both projective ratios are legitimate.
3. The sum identity gives `s=-3R(0)/lambda_1!=0`; no division by a
   potentially vanishing projective sum occurs.
4. The formula for `B` comes from the product of the unshifted roots and is
   checked before the branch relation is imposed.
5. Frobenius is applied only after recording the exact quarters
   `u^(p+1),v^(p+1)`.
6. All 16 ordered quarter pairs are retained. Resultant factors at `u=0`
   are saturated only because `u` is already proved nonzero.
7. Every nonconstant resultant/power gcd is resolved in `v`; the three
   nonconstant quadratic packets on the largest characteristic are handled
   in their exact quotient fields.
8. Zero, repeated, and `s=0` packets are rejected explicitly.
9. The table is necessary only. No listed projective packet is called a
   lift or a split pencil.
