# Proof

Let `a_j` be the elementary symmetric functions of the six signed roots.
Newton's first identity says

```text
a_1=sum_i rho_i=0.                                      (1)
```

The monic locator is therefore

```text
F(X)=X^6+a_2X^4-a_3X^3+a_4X^2-a_5X+a_6.                (2)
```

Its even and odd parts give the unique polynomials

```text
E(Y)=Y^3+a_2Y^2+a_4Y+a_6,
B(Y)=a_3Y+a_5,                                         (3)
```

which proves `(END2)--(END3)`. Multiplying the two parity conjugates gives

```text
F(X)F(-X)=E(X^2)^2-X^2B(X^2)^2=G(X^2).                 (4)
```

The relation is reduced, so the six roots are distinct and nonantipodal.
Their squares are six distinct elements of `mu_256`; comparison of the monic
degree-six polynomials in `(4)` proves `(END5)`.

Conversely suppose `G` divides `Y^256-1`. The binomial is separable. If a
root `y` of `G` had `B(y)=0`, then `(END4)` would also give `E(y)=0`, and

```text
G'=2EE'-B^2-2YBB'                                      (5)
```

would vanish there. This contradicts squarefreeness. Hence `(END6)` is
defined, and `(END4)` gives

```text
rho^2=y,       E(y)-rho B(y)=0.                        (6)
```

Thus the six reconstructed values are exactly the roots of the monic
degree-six polynomial `(END3)`. Their squares are distinct, so they are
distinct and nonantipodal. They lie in `mu_512`, and the missing `X^5`
coefficient gives `sum rho_i=0`. Their unique signed representations relative
to `omega` have distinct base exponents. This proves the converse.

Monic division gives the integer remainder polynomials in `(END7)`. If their
ideal were proper over `Q`, a complex point and the converse would yield a
nonzero reduced signed polynomial

```text
sum_i s_i Z^e_i,       deg<256,                         (7)
```

vanishing at a primitive `512`th root. Its minimal polynomial is
`Z^256+1`, a contradiction. The ideal is therefore the unit ideal over `Q`.
Clear denominators in a rational unit-ideal identity to obtain `(END8)`.
Reducing that identity in any solution field proves the characteristic-
divisor assertion. QED.
