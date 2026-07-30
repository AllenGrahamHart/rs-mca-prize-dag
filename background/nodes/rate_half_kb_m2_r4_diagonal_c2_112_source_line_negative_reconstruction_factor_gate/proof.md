# Proof

The four `J_0` labels form two fixed-point-free `tau` pairs. An admissible
internal assignment consists of two distinct adjacent edges whose four-edge
`tau` closure has collision defect at most one. Directly on the six edges,
eight assignments contain one `tau`-fixed edge and one moving edge, while
four contain two moving edges. The matching centralizer is transitive on
each class, giving the two templates in `(KBNF-1)`.

The endpoint centralizer of `T->1/T` is transitive on nonfixed reciprocal
pairs. Orient the common endpoint to `2`; its mate is `1/2`, and write the
other pair as `{b,1/b}`. This changes neither the source quotient coordinate
nor negative reconstruction solvability.

Write `q=(T-c)(T-d)` and specialize the pinned odd part `(KBOI-2)` to
`epsilon=-1`. At the common endpoint `2`, the incidence denominator is

```text
D_-(2)=-E.                                         (1)
```

Thus `z=-N_-(2)/D_-(2)` has denominator `E`, which is nonzero by the
odd-incidence theorem.

Use the negative reciprocal basis

```text
u_0=x_0+x_1W+x_2W^2,
u_1=x_3(1-W^2),
u_2=-(x_2+x_1W+x_0W^2).                           (2)
```

The condition `U(T,w) in <q>` gives two homogeneous rows in
`x_0,...,x_3`. For either template, divide `V(T,z)` by `T-2`; if
`V(T,z)=(T-2)(l_0+l_1T)`, the internal-star difference fixes the target

```text
U(T,z)=((l_0+s l_1)e(T)+(l_0+r l_1)f(T))/(s-r),   (3)
```

where `r,s` are the noncommon endpoints of `e,f`. Append the three
coefficient equations from `(3)` to the two forced rows from `(2)`. This is
the augmented `5 x 5` determinant whose vanishing is the negative image-
plane condition.

Substitute `z=-N_-(2)/D_-(2)` and expand the determinant. For
`(r,s)=(1/2,b)` and `(r,s)=(b,1/b)`, respectively, collection of the linear
factors gives exactly

```text
Delta_F=-6 Pi A^2 B / ((2b-1)E^5),
Delta_M= 6 Pi A B C / (((b-1)(b+1))E^5).          (4)
```

This is a direct determinant identity; the bounded symbolic expansion and
an independent exact-rational replay are recorded with the node.

The roots `c,d` are disjoint from `{2,1/2}`, so the first four factors of
`Pi` are nonzero. The source label `w` is not fixed by inversion, so
`w!=+1,-1`. If `cd=1`, then `{c,d}` is `tau`-invariant, contrary to
`tau(J_1) subset I` and `J_1 subset J`. Hence `Pi!=0`. The remaining
template denominators express distinctness inside `J_0`, and `E!=0` by
`(1)`. The reconstruction theorem gives rank four for the coefficient
matrix, so augmented-determinant vanishing is necessary and sufficient.
Removing the proved nonzero factors from `(4)` gives `(KBNF-4)`. QED.
