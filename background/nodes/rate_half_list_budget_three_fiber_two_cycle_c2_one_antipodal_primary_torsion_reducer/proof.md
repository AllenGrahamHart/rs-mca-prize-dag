# Proof

Let the known antipodal pair be `{a,-a}`. Since `a in mu_N`, common scaling
by `a^(-1)` is allowed and the covariance of the normalized gap compiler
preserves every primary-gap verdict. This gives `(OAR1)` and `(OAR2)`.

Replacing `S` by `-S` gives

```text
E(z;-S,P)=E(-z;S,P).
```

The normalized fourth root with constant term one is unique, so

```text
a_n(-S,P)=(-1)^n a_n(S,P).                            (1)
```

Every scalar denominator in the coefficient recurrence is invertible on the
official row. Hence each even coefficient is a polynomial in `S^2,P`, while
each odd coefficient is `S` times such a polynomial. Since `M` is even,
equation `(1)` defines the unique `F_H,G_H` in `(OAR3)`. The primary gap is
`a_M=a_(M+1)=0`. If `S!=0`, this is exactly `(OAR4)`. If `S=0`, then
`d=-c` and the denominator has two antipodal pairs; the converse is
immediate. This proves the primary and parity assertions.

For the sign-free torsion circuit, induction in `(OAR5)` gives

```text
U_j=c^(2^(j+1))+d^(2^(j+1)),
V_j=(cd)^(2^(j+1)).                                  (2)
```

At `j=39`, the exponent is `N=2^40`. Thus `c^N=d^N=1` implies the terminal
conditions in `(OAR6)`. Conversely put `x=c^N` and `y=d^N`. The terminal
conditions and `(2)` give `x+y=2` and `xy=1`, so both are roots of
`(T-1)^2`. The official characteristic is odd, and in fact the same
conclusion follows directly from the repeated root, so `x=y=1`. This proves
`(OAR6)`.

The factors in the nonvanishing condition have direct meanings:

```text
X!=0                         iff c+d!=0,
P!=0                         iff cd!=0,
X-4P=(c-d)^2!=0             iff c!=d,
(1+P)^2-X=(1-c)(1-d)(1+c)(1+d)!=0
                              iff c,d notin {1,-1}.   (3)
```

An actual packet therefore gives `(OAR7)`. Conversely choose either square
root `S` of `X` and let `c,d` be the roots of `Y^2-SY+P`. The terminal
argument proves `c^N=d^N=1`; because `mu_N` is contained in the base field,
both roots are base-field elements. Conditions `(3)` make the four roots
distinct and leave exactly one antipodal pair. Changing the sign of `S`
replaces the quadratic by `Y^2+SY+P`, whose roots are `-c,-d`. This proves
the exact reconstruction modulo sign.

Finally, two polynomials with a common `X`-root have zero resultant. Hence
`(OAR4)` implies the printed resultant gate. The converse can fail because a
common primary root need not satisfy the joint trace recurrence in `(OAR5)`;
the theorem retains that condition explicitly. QED.
