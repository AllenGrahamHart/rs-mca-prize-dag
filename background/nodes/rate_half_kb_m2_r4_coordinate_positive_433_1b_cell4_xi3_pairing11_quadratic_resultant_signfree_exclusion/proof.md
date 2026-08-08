# Proof

Write `m=df`, `s=(d+f)^2`, `z=1/d`, `y=z^2`, and `q=de`. The missing-sum
equation is

```text
M(y)=1+(2m-s)y+m^2y^2=0.                          (1)
```

The second and third matching pairs are the two quadratics in `q`

```text
B(q,z)=Pair(q,bmz),
C(q,z)=Pair(q,sigma_c cmz).
```

For quadratics `a q^2+bq+c` and `d q^2+eq+f`, their Sylvester resultant is

```text
(af-cd)^2-(ae-bd)(bf-ce).                        (2)
```

Applying (2) to `B` and `C` gives a degree-six necessary cut `D(z)` for a
common `q` root.

Reduce `D(z)` modulo the quartic `M(z^2)`. The result is a cubic
`R(z)=E(y)+zO(y)`. Every common root satisfies the second sign-free cut

```text
E(y)^2-yO(y)^2=R(z)R(-z)=0.                       (3)
```

Reducing (3) modulo the quadratic (1) leaves a linear remainder in every
source-sign/`sigma_c` row. The corresponding division-free common-root cut
is normed through the exact four-basis source tower.

The compiler includes roots of the norm numerator and denominator and every
inverse-guard numerator and denominator. It lifts them through the base `t`
quadratic, `b` quadratic, linear `c` recovery, and compact kernel. The four
`sigma_c=-1` rows have norm bidegree `(3864,1560)` and the four `sigma_c=1`
rows have norm bidegree `(3868,1560)`. Their complete exceptional root union
contains 60 candidate `r` roots and 16 guarded source points. Direct finite
replay of the original equations leaves eight compatible `(z,q)` candidates.

For every candidate and both remaining `sigma_o` lanes, the third paired
equation

```text
Pair(-q,sigma_o ef)=0
```

is checked directly. All 16 evaluations are nonzero. The target-boundary,
witness, free-branch, and unresolved ledgers are empty. QED.
