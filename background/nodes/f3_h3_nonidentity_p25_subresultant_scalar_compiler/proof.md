# Proof

Write `c_a=1-zeta_n^a` for `1<=a<n`. The roots of `F_n` are exactly the
`c_a`, and

```text
G_n(T,X)=product_b(T-c_bX).
```

After specializing `T=t`, a root `X=c_a` of `F_n` is a root of `G_n(t,X)`
exactly when `t=c_ac_b` for some `b`. The roots of `F_n` are simple whenever
the characteristic does not divide `n`. Therefore

```text
deg gcd_X(F_n,G_n(t,-))
 =#{a:exists b, c_ac_b=t}
 =#{(c_a,c_b):c_ac_b=t}=P(t),
```

because each first coordinate determines the second coordinate. This proves
`(PSC5)`.

For two degree-`d` polynomials over a field with nonzero leading
coefficients, the gcd has degree at least `q` exactly when the polynomial
subresultants of indices `0,...,q-1` all vanish. The leading coefficients of
`F_n` and `G_n` are `1` and `-n`; they are units in `R` and remain nonzero
at every prime `p=1 mod n`. Hence subresultants commute with every reduction
used here, and `(PSC2)` vanishes coefficientwise at `T=t` exactly when
`P(t)>=25`.

Over characteristic zero, shifted-product Sidonicity gives `P(t)<=2` for
every `t`. Thus the coefficient ideal in `(PSC3)` has no common zero after
tensoring with `Q`. Its zeroth subresultant is, up to the unit sign and a
power of `n`,

```text
Res_X(F_n,G_n)=Pcal_n(T),
```

whose leading coefficient is a unit in `R`. Before adjoining `Y`, the
quotient is therefore finite over `R`; adjoining the inverse of `T-1` takes
the stable image of one endomorphism of that finite module. The selected
quotient remains finite and vanishes after tensoring with `Q`, so it is
finite torsion and has the scalar annihilator `(PSC4)`.

Reduce modulo an odd prime `p=1 mod n`. The finite selected quotient is
nonzero exactly when the equations in `(PSC3)` have a common geometric
point. Any common root of `F_n` and `G_n(t,-)` has the form `c_a`, and then
`t/c_a` is another root `c_b`; all these roots lie in `F_p`, so the geometric
parameter is actually `t=c_ac_b in F_p`. The selector forces `t!=1`; the
subresultant criterion and `(PSC5)` then identify such a point exactly with a
nonidentity target satisfying `P(t)>=25`. A finite `R`-module has nonzero
reduction modulo `p` exactly when `p` divides its scalar annihilator. This
proves `(PSC6)`. QED.
