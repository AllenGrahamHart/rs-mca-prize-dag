# Proof

The staged direct-Singular replay first proves the `w=0` chart empty: its
35-element, dimension-one basis reduces the 15-factor boundary localizer to
a 521-term polynomial whose square is zero.

On `w!=0`, the successful replay reconstructs the four exact `M01-R11`
q-slice generators and the full quotient-parity polynomials from pinned PR
#1144 commit `05ff2348de8f2c0f99683875ff12a9a79dcf21ec`. Their degrees, term
counts, and SHA-256 values agree with the upstream certificate. Singular
computes the q-slice basis of size 168 and dimension two, reduces `J` to a
degree-21, 6510-term remainder, and computes the augmented basis of size 174
and dimension two.

Let `G` be the output of `interred` on those 174 generators. This operation
preserves their ideal. Divide the 151178 terms of `I` into 148 disjoint
blocks `I_r`. Starting with `R_0=0`, the replay sets

```text
R_r = reduce(R_(r-1) + I_r, G).
```

Polynomial division gives `R_(r-1)+I_r-R_r` in `(G)`. Induction therefore
gives `I-R_148` in `(G)`, whether or not `G` carries Singular's standard-basis
flag. Thus `(G,I)=(G,R_148)` exactly. The terminal remainder has the pinned
degree 19 and 4435 terms.

A fresh `slimgb(G,R_148)` has size 168 and dimension two. Sequential exact
reduction of all 20 named-open factors gives a degree-29, 10653-term
localizer, and its square reduces to zero. Hence the localized full-chart
ideal is unit, so `M01-R11` is empty over the algebraic closure and therefore
over the challenge extension field. Combined with the boundary calculation,
the complete cell is empty.

The sibling ten-cell theorem proves that literal `b -> b^-1` is an
isomorphism of the complete `M01-Rxx` and `M02-Rxx` source systems, including
q-slice equations, quotient factors, and named opens. Applying it at `R11`
proves `M02-R11` empty. QED.
