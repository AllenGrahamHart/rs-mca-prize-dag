# Proof

Let

```text
U(y)=y^hP(1/y),       V(y)=U(y)+dy^h.
```

For `e=2`, the pinned defect is

```text
G=d^2X^2 gamma(y),
gamma=-h/m+((m-1)/m)ay+c_2y^2.
```

Put `W=y^(m-2h)R(1/y)`. Then

```text
UVW=1-y^m,
XP'(X)|_(X=1/y)=y^(-h)(hU-yU').
```

Substitute these expressions and `G(1/y)=d^2y^(-2)gamma(y)` in
`m(P+Q-PQG)=d^2XP'R`. Multiplication by
`y^(m-h)UV/d^2`, followed by `m-3h=2`, gives the exact reciprocal equation

```text
(hU-yU')(1-y^m)
 =(h-(m-1)ay-mc_2y^2)U^2V^2
  +(m/d^2)y^(h+2)UV(U+V).                           (1)
```

Modulo `y^h`, put `Z=U^(-3)` as in the linear case. Equation `(1)` becomes

```text
yZ'+3hZ
 =3h-3(m-1)ay-3mc_2y^2.                            (2)
```

Since `m=3h+2`, coefficient comparison gives

```text
Z=1-3ay-3c_2y^2 mod y^h,
```

which proves `(QBO2)--(QBO3)`.

Let `F=F_(a,c_2)`. The actual `U` agrees with `F` below degree `h`, has
coefficient `epsilon` at degree `h`, and coefficient zero at degree `h+1`.
Retain coefficients `h,h+1` in `(1)`. At degree `h`, replacing
`V^2` by `U^2+2dUy^h` gives

```text
4h(epsilon-f_h)+2dh=0,
```

or `f_h=epsilon+d/2=epsilon(1+x)/2`.

At degree `h+1`, the change from `F^4` is

```text
-4f_(h+1)+12a(epsilon-f_h).
```

The coefficient of `y` in
`(h-(m-1)ay-mc_2y^2)F^3` is `-a`, and the `2dUy^h` correction contributes
`-2da`. Subtracting the formal equation for `F` leaves

```text
(4h+1)f_(h+1)=0.
```

The characteristic hypothesis makes `4h+1` invertible, proving `(QBO4)`.

It remains to count. Since `gcd(h,m)=2`, the image of
`lambda -> lambda^h` on `mu_m` is the square subgroup. Thus every scaling
orbit has a representative whose constant lies in the fixed two-element
transversal `{1,omega}`. For such a representative the zero-value scalar
gate gives `(QBO1)`. Once `(epsilon,x,a)` is fixed, `(QBO3)` and the constant
term determine `P`, and then `Q=P+d`.

In the binomial expansion of `(QBO2)`, the term selecting `ay` exactly
`h+1` times gives the leading coefficient

```text
product_(r=0)^h(3r+1)/(h+1)!
```

of `f_(h+1)` as a polynomial in `a`. It is nonzero under the characteristic
hypothesis. Therefore there are at most `h+1` choices of `a` for each of the
two values of `epsilon` and the `m-1` values of `x`. Candidate triples may
duplicate an orbit or fail the first endpoint, split-root, exact-level, or
primitive tests; all such effects only decrease the count. This proves
`(QBO5)`. QED.
