# Proof

Fix source signs, target signs, and `xi in {0,2}`. On the proved cell-11
four-basis tower, canonical matching `5` gives quadratics `P_u(u)` and
`P_f(f)`, where `u=df`. Put `de=m, eta=1` for `xi=0`, and `de=-m, eta=-1`
for `xi=2`. Eliminating `e=de*f/u` from the deleted squared-sum equation
gives

```text
R(u,f)=(u^2+eta*de*f^2)^2-S*f^2*u^2=0.            (RS5-DE5)
```

The pinned compiler reduces the exact relation resultant modulo `P_u`,
forms a division-free `f` eliminant, and pseudo-reduces it modulo `P_f`.
The resulting common-root cut is normed through `1,t,b,bt`, retaining all
leading-coefficient drops.

The adapter runs all 32 source-sign/target-lane/`xi` rows. Its complete root
union has 336 case-labeled candidates and lifts to 224 guarded source
points. Their quadratic Cartesian products give 256 `(u,f)` rows. The
missing relation is nonzero on 224 of them. The other 32 reconstruct
`d,e,v` and have a nonzero third colored-pair cut. No colored solution,
witness, or unresolved branch survives.

An external compiled Frobenius/gcd pass reconstructs all 146 roots of the 41
unique polynomial profiles and certifies that each squarefree root-part
degree equals its printed root count. The local audit validates each profile
and directly replays all 256 `(u,f)` rows and all 32 zero-relation lifts.

The exact generic quotient gives the two disjoint orbits printed in the
statement, closing eight labels from the direct representatives `(0,5)` and
`(2,5)`. QED.
