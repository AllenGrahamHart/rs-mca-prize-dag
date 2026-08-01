# Proof

Apply the zero-loop product-q weld to `(KBZ433F-1)`.  Safe division removes
only target and even label/denominator factors, preserving affine linearity
of the q system in `(t,r)`.  Product compatibility is linear in `c` and
`x=t^2`.  After solving them, Cramer's rule and `t^2=x,r^2=y` leave residual
degrees `(16,13)` in same-sign rows and `(8,5)` in opposite-sign rows.  In
every row the common cleared factor is exactly `X_den(y^2-1)`.

Lex elimination followed by binary Frobenius gcd gives

```text
(+,+): b^8+527279086b^7-32385165b^6-285229632b^5
       -613639525b^4-285229632b^3-32385165b^2+527279086b+1,
(+,-): b^2-399402603b+1,
(-,+): b^2+825543884b+1,
(-,-): b^8+502371476b^7-181830825b^6-372406267b^5
       -987253675b^4-372406267b^3-181830825b^2+502371476b+1. (1)
```

Each polynomial in `(1)` is exactly its gcd with `b^p-b`; all factors are
linear in the deployed field.  Specializing each root and taking the exact
`y` gcd gives `(KBZ433F-3)`.  In the same-sign rows, two further roots force
`y=-1`, and two force `X_den=0,X_num!=0`.  In each opposite-sign row, both
roots force `X_den=0,X_num!=0`.  Thus no other generic projection is valid.

The lost linear-`c` and product-solve branches contain only

```text
(b,y)=(0,0),(1,-1),(-1,1).                       (2)
```

The singular-q branches add only target guards and the same false product
projections just listed.  Hence `(KBZ433F-3)` is exhaustive.  Direct replay
in the original four determinants and full guard proves existence of all
eight packets.

Finally the target sign/exchange group has orbit `[2,5,6,9]` on cell `2`.
It preserves the complete common system and acts bijectively, so the orbit
contains exactly 32 packets. QED.
