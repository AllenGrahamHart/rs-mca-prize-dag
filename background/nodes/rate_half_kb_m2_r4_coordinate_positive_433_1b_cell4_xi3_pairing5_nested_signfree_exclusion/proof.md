# Proof

Write `m=df`, `s=(d+f)^2`, `z=1/d`, `y=z^2`, and `q=de`. The missing-sum
equation is

```text
M(y)=1+(2m-s)y+m^2y^2=0.                          (1)
```

The first matching pair gives `A(q)=Pair(q,-q)`. It is even and therefore
is a quadratic `A_u(u)` in `u=q^2`. The second pair is

```text
B(q,z)=Pair(q,sigma_c cmz).
```

Multiply `B(q,z)` by `B(-q,z)` and rewrite the product as a polynomial in
`u,z`. Reduce it modulo the quadratic `A_u`. The remainder is linear in
`u`; its division-free common-root cut is a degree-eight polynomial `D(z)`.

Reduce `D(z)` modulo the quartic `M(z^2)`. The result is a cubic
`R(z)=E(y)+zO(y)`. Every common root satisfies the second sign-free cut

```text
E(y)^2-yO(y)^2=R(z)R(-z)=0.                       (2)
```

Reducing (2) modulo the quadratic (1) leaves a linear remainder in every
source-sign/`sigma_c` row. The corresponding division-free common-root cut
is normed through the exact four-basis source tower.

The compiler includes roots of the norm numerator and denominator and every
inverse-guard numerator and denominator. It lifts them through the base `t`
quadratic, `b` quadratic, linear `c` recovery, and compact kernel. The eight
degree-5058 norm rows yield 104 candidate `r` roots and 128 guarded source
points. Direct finite replay of the original equations leaves 32 compatible
`(z,q)` candidates.

For every candidate and both remaining `sigma_o` lanes, the third paired
equation

```text
Pair(sigma_o ef,bf)=0
```

is checked directly. All 64 evaluations are nonzero. The target-boundary,
witness, free-branch, and unresolved ledgers are empty. QED.
