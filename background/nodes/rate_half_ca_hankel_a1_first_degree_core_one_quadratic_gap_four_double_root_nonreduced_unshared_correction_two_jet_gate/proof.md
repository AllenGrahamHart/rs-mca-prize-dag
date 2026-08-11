# Proof

The exact row and regular-factor identities give

```text
Q(t,x_*)=a_Qg_*S_B^3,
D_1=a_Dg_*S_B^2.                                   (1)
```

Under `(HNJ1)`, their base orders at `tau` are six and four.

The correction contact divisor is `2B`, while the vertical heavy-row
divisor is `3B`. Even when the degree-two divisor `B` is nonreduced or its
units lie on different normalized branches above `tau`, each correction
branch forces the fixed value `P_F(t,x_*)=F_0(t)` to vanish to base order at
least two: replacing the moving point by `x_*` changes `P_F` only through
`X-x_*`, whose branch order is strictly larger than the contact order.
Therefore

```text
z^2|F_0.                                            (2)
```

No addition of branch orders is used in `(2)`. This is why the two
coefficients in `(HNJ4)` remain explicit.

The kernel equation gives

```text
F_(i+1)=x_*F_i-Q(t,x_*)h_i.                         (3)
```

The last term has order six. Comparing coefficients of `z^2` and `z^3` in
`(3)` and inducting on `i` proves `(HNJ5)`.

Since `D_1` has exact order four, it divides `F_0` locally exactly when the
two coefficients after the forced `z^2` vanish. If they vanish, then

```text
Q(t,x_*)/D_1=(a_Q/a_D)S_B                          (4)
```

is polynomial and recurrence `(3)` propagates `D_1|F_i` to every `i`.
The converse follows from `i=0`, proving `(HNJ6)`. Global degree counting
after division is unchanged and gives quotient degree at most three.

On the vanishing branch, the class of the divided row in the regular
quotient is nonzero at `tau`. Its image is divisible by `z^4`, while the
regular determinant has valuation four. Hence one positive Smith exponent
is at least four and their sum is four, giving type `[4]`. QED.
