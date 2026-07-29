# Proof - L1 Mersenne HNF m=8 order-one cubic three-double q=-6x^2 degree-12 reduction

On `q=-6x^2=-6y`, direct substitution in (TLR4)--(TLR5) gives

```text
M_5=3x^2[(d+2)E_0-x(d+6y)(s-y)],                   (1)

E_0=-2D/5+(13d^2+33d+33)y-21y^2.                  (2)
```

The residual conic is (QDR2). Reducing (2) by that quadratic gives the
particularly simple identity

```text
E_0+2u(d+6y)/5=-C_y/5.                             (3)
```

The saturated chamber has `q!=0`, hence `x!=0`. Equations (1)--(3) prove
(QDR3). The factor `d+6y` is forbidden because it is exactly `d-q`; the
remaining factor is therefore zero. Squaring it and using `x^2=y` gives
(QDR4). Squaring is used only in the necessary direction and may add roots.

For the final reduction, write

```text
y^2=(A/15)y-2B/21                                  (4)
```

from (QDR2), and use (4) once more for `y^3`. The coefficient of `y` in the
remainder of (QDR4) is

```text
25((A/15-s)^2-2B/21)=2E/63,                        (5)
```

because `A/15-s=-2(2d^2+9d+9)/15`. Its constant term is

```text
25(-2B/21)(A/15-2s)-4(d+2)^2u^2=2F/63,             (6)
```

which proves (QDR6).

If `E` is nonzero, (QDR6) gives `y=-F/E`; substitution in (QDR2) and
clearing `E^2` gives (QDR7). If `E=0`, a common root also has `F=0`, so
(QDR7) remains necessary without division. The leading terms are

```text
A=11d^2+...,
B=d^4+...,
E=-19d^4+...,
F=-31d^6+...,
```

and hence the degree-12 coefficient of (QDR7) is

```text
105*31^2+7*11*31*19+10*19^2=149868.                (7)
```

Finally every packet retains the norm-color condition
`d^(p+1) in mu_8`, proving that the 32 gcds (QDR8) are exhaustive necessary
tests. The quadratic-in-`b`, sixth-coefficient, color-ratio, and Frobenius
conditions can only remove roots from this endpoint. QED.
