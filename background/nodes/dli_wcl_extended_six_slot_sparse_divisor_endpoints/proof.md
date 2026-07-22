# Proof

Let

```text
F(X)=product_i(X-rho_i)
```

be the monic root locator. Newton's identities, used successively in odd
degrees, show that `(XW1)` is equivalent to

```text
e_1=e_3=...=e_(2ell-1)=0,                              (1)
```

because the characteristic is zero or exceeds `w` on every official row.

Suppose first that `w=2r+1`. Since `w` is odd and `M` is a power of two,
raising to the `w`th power permutes `mu_M`. There is therefore a unique common
dilation making the product of the roots one. The constant coefficient of
the normalized locator is then `-1`. Separating its odd and even powers gives

```text
F(X)=XA(X^2)-B(X^2),                                   (2)
```

where `A` is monic of degree `r` and `B(0)=1`. The vanished coefficients in
`(1)` are precisely the top `ell` coefficients of `B`, so
`deg B<=r-ell`. Multiplying `(2)` by its value at `-X` gives

```text
-F(X)F(-X)=X^2A(X^2)^2-B(X^2)^2=G(X^2).               (3)
```

Thus `G(Y)=product_i(Y-rho_i^2)`.

If `w=2r`, parity separation instead gives

```text
F(X)=E(X^2)-XB(X^2),                                   (4)
```

with `E` monic of degree `r`. Again `(1)` kills the top `ell` coefficients
of the odd part, hence `deg B<=r-ell-1`, and

```text
F(X)F(-X)=E(X^2)^2-X^2B(X^2)^2=G(X^2).                (5)
```

The roots `rho_i` are distinct and antipodal-free, so their squares are
distinct elements of `mu_N`; `(XW6)` follows.

Conversely, suppose one of the displayed `G` divides `Y^N-1`. This ambient
polynomial is squarefree. In the odd case, `A(y)=0` at a root of `G` would
also force `B(y)=0`, making that root multiple in `YA^2-B^2`; hence `A(y)`
is nonzero. Put `rho=B(y)/A(y)`. Then `rho^2=y` and `(2)` vanishes at
`rho`. The even case is identical with `rho=E(y)/B(y)`. The `w` reconstructed
roots are distinct and no two are antipodal, because either coincidence
would give the same squared root. Their locator is the monic degree-`w`
polynomial `(2)` or `(4)`, and `(1)` plus Newton's identities recovers
`(XW1)`. This proves the exact divisor correspondence.

The repeated-squaring presentation is triangular because `G` is monic. At
each stage Euclidean division uniquely determines the quotient of degree at
most `w-2` and the next remainder of degree below `w`. Starting from
`Y^(2^s)` therefore gives the unique successive remainders
`Y^(2^t) mod G`; the terminal condition is exactly `G|Y^(2^m)-1`.
There are `(k-1)w` intermediate-remainder variables, `k(w-1)` quotient
variables, and `b` base variables, proving the size formula. Coefficients of
`G` have degree at most two in the base variables, so every lifted equation
has total degree at most three. The six table rows are direct substitutions.

It remains to prove characteristic-zero emptiness. A nonempty set of
distinct `2^a`th roots of unity summing to zero contains an antipodal pair.
Indeed, write a primitive root as `zeta`. Over `Q(zeta^2)`, the elements
`1,zeta` are linearly independent. Splitting a relation into even and odd
exponents gives two relations at order `2^(a-1)`; induction from order two
partitions each nonempty relation into antipodal pairs. Applied to the
reconstructed roots, this contradicts their proved antipodal-freeness.

Hence each divisor ideal has no point over `Qbar`. Hilbert's Nullstellensatz
makes it the unit ideal over `Q`, and clearing denominators gives `(XW8)`
with nonzero integer `Delta`. Reducing that identity modulo a supporting
characteristic shows that the characteristic divides `Delta`.

Finally, an antipodal-free signed support is obtained by choosing `w` of the
`M/2` base exponents and one of `2^(w-1)` sign patterns modulo global sign.
This gives the raw count in the table. The affine group has order
`M phi(M)=M^2/2`, so dividing by its maximum orbit size and taking a ceiling
gives the stated rigorous class lower bounds. QED.

