# Proof

Use the standard first endpoint coordinate

```text
Y(r)=r+1/r.
```

The second reflection `v(r)=lambda/r` has the standard quotient

```text
Z_0(r)=r/mu+mu/r,       mu^2=lambda.                (1)
```

Its sibling `Y(vr)` and `Y(r)` have trace parameter
`a=lambda+lambda^(-1)`, while

```text
d^2=(mu+mu^(-1))^2=a+2.                            (2)
```

Retain the endpoint normalization from the one-parameter theorem,
`m(x)=(x-2)/(x-b)`. Direct reduction using `(1)` gives

```text
m(Y(r))m(Y(vr))
 = (Z_0-d)^2/Q_b(Z_0),                              (3)
Q_b(z)=z^2-b*d*z+b^2+d^2-4.
```

The left side is `P^2` on the quotient of the coefficient quartic by the
global sign involution. The actual second endpoint coordinate is a projective
transform `Z=ell(Z_0)`, and its quadratic source lift satisfies

```text
W^2=m(ell(Z_0)).                                    (4)
```

The quotient in `(3)` and the `W`-line in `(4)` are the same quadratic
subextension of the actual source normalization. Their radicands differ by
a square in the rational function field of `Z_0`.

Write

```text
m(ell(z))=L_2(z)/L_b(z),                            (5)
```

where the roots of the two distinct linear forms are the preimages of `2`
and `b`. Removing the displayed square `(z-d)^2` from `(3)`, the square-class
condition says

```text
Q_b(z)L_2(z)/L_b(z) is a square.                    (6)
```

The discriminant of `Q_b` is

```text
(b^2-4)(d^2-4),
```

which is nonzero because `b notin {-2,2}` and `d^2=a+2` is `1` or `3`.
Thus `(6)` has four simple odd-support contributions: the two roots of
`Q_b`, the root of `L_2`, and the root of `L_b`. Since the last two are
distinct, parity forces

```text
Q_b is proportional to L_2 L_b.
```

This is exactly `(KBMT-1)`.

The branch values of the standard `Z_0` projection are `2,-2`. Evaluating
`Q_b` there gives `(KBMT-2)`. In the genus-zero V4 passport the second
quadratic pullback has two branch places, so exactly one branch value of `h`
lies in the branch set of `Z`; by `(KBMT-1)--(KBMT-2)` this is equivalent to
`b=d` or `b=-d`. In the genus-one passport the second pullback has four
branch places, so neither branch value is aligned, equivalently
`b!=d,-d`. Equation `(2)` gives `(KBMT-3)`. QED.
