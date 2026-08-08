# Proof

The six edges on `J_0` give the eight fixed-moving assignments `F00--F07`
and four moving-moving assignments `M00--M03`. The target root is one of the
four literal labels in `(KBLB-2)`. This is a disjoint census of `32+16=48`
cells. The output additionally checks that each target root and each possible
common vertex occurs exactly twelve times.

For one literal assignment, let `a` be its common vertex and let `e,f` be its
ordered adjacent edge quadratics. The repaired homogeneous odd vector is

```text
V(T,W)=(-d, 1+W, -dW).
```

The coefficient of `W` in `V(a,W)` is nonzero on an actual named-open cell,
so its root `z` is finite and distinct from `0,+/-1`. Evaluating `V` at `z`
determines the internal-star target in the span of `e,f`, exactly as in the
internal reconstruction theorem.

Write the positive reciprocal even vector in its five-coefficient basis.
Membership of `U(T,0)` in `Y(T-dY)` gives the two linear equations

```text
x_2=0,       x_0+d*x_3=0.                         (KBLB-5)
```

Together with the three coefficients of `U(T,z)` from the internal star,
`(KBLB-5)` is the literal `5 x 5` reconstruction system. Its determinant is
localized only because the proved positive evaluation map is an isomorphism
on every actual packet. Direct substitution verifies all five equations.

At the two projective roots of `q_hom`, the resultant identity is `(KBLB-3)`:
the finite factor is evaluation at `d`, and the infinity factor is the
`T^4` coefficient. Complete-source ramification forces an exact `W^2`
division in each factor. Both quotients have degree two, so their product has
degree four. Comparing this product with `(KBLB-4)` yields four polynomial
equations in `b,d` after clearing only recorded denominators.

For each cell, factor the named-open product into distinct irreducibles over
`QQ`, reduce the equations and factors modulo `p`, and form

```text
<equations, 1-y*product(localizers)>.
```

Its Groebner basis is `[1]` in every cell. Independently, saturating the
two-variable equation ideal by the same localizers one at a time also ends
at `[1]` in every cell. The two runs agree on each equation fingerprint,
localizer product, and classification. A unit complete-chart ideal has no
point over the algebraic closure of `F_p`, hence none over `F_(p^6)`. QED.
