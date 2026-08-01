# Proof

Compile cell `9` from the canonical products and strip only explicit source
and target guards.  Write the product rows as

```text
P_x=A_x x+B_x,       P_0(b,c,r),                  (KB433BC-3)
```

and the q rows as `Q_2t^2+Q_1t+Q_0` and `H(b,c,r)`.  The static q row `H`
is linear in `c`; the resultant of its coefficient and constant is, up to a
nonzero scalar, `(r^2-1)`.  Thus `H` uniquely reconstructs `c` off guards.
The product branch `A_x=B_x=0` is also impossible: eliminating `c` gives
only

```text
b^2(b^2-1)^2(r^2-1)^2(r^2+1)^2.                  (KB433BC-4)
```

Eliminating `c` between `P_0` and `H` gives a quadratic `J(b,r)`.  On an
actual solution `A_x!=0`, so `x=-B_x/A_x`.  The moving q row becomes

```text
(Q_1A_x)t+(Q_0A_x-Q_2B_x)=0.                     (KB433BC-5)
```

The simultaneous-vanishing branch of the two coefficients in
`(KB433BC-5)` projects only to irreducible quadratics in `r`, hence has no
deployed point.  Equating the square of `(KB433BC-5)` with `x` and
eliminating `b` against `J` gives `(KB433BC-1)`.

Each nonlinear factor printed there is irreducible.  For the sole linear
factor in each row, specialize `r` to `(KB433BC-2)` and take the gcd in `b`
of `J` and the square equation.  It has degree two.  Exact polynomial
division shows that it divides the numerator of `A_x` after c-reconstruction,
while its gcd with the numerator of `B_x` is one.  Every projected linear
candidate therefore has `A_x=0,B_x!=0`, contradicting `(KB433BC-3)`.

The independent audit applies Rabin's criterion directly to all twelve
nonlinear sign-row factors.  The target operations generate cells
`10,12,13` from cell `9` and preserve the product/q equations. QED.
