# Proof - L1 Mersenne HNF m=8 order-one cubic three-double affine-color compiler

For an ordered triple of distinct points, translate and scale it to
`(0,1,lambda)`. Its elementary symmetric functions are

```text
e_1=1+lambda,   e_2=lambda,   e_3=0.
```

After centering, the depressed-cubic invariants are

```text
P=e_2-e_1^2/3=-A(lambda)/3,
Q=e_3-e_1e_2/3+2e_1^3/27=B(lambda)/27.              (1)
```

Under an affine change `z -> cz+t`, centering removes `t` and gives
`P -> c^2P`, `Q -> c^3Q`. Consequently (1) is equivalent to the homogeneous
necessary relation

```text
27 A(lambda)^3 Q^2+B(lambda)^2 P^3=0.               (2)
```

In a `2+2+2` packet, (TDF3) gives

```text
a_i=w+f(u_i),       alpha_i=e_3 a_i.
```

The three values `f(u_i)` therefore differ from the three distinct colors
`alpha_i` by one common nonzero scale and one translation. Their ordered
affine ratio is a root of `Lambda_321` by (RPC4). Equation (2) holds for
that root, so the root formula for the resultant proves (TAC3).

There are 56 three-element subsets of `mu_8`. Rotation acts freely because
a three-element subset cannot be a union of orbits of a nontrivial subgroup
of a group of order eight. This gives seven oriented cyclic gap classes:

```text
(1,1,6),
(1,2,5), (1,5,2),
(1,3,4), (1,4,3),
(2,2,4),
(2,3,3).
```

Reflection does not identify the two scalene pairs for a complex affine map:
it conjugates their depressed-cubic invariant. Direct substitution in (1)
gives the seven values

```text
gap type                 T=-27Q^2/P^3
(1,1,6)                  112-81 sqrt(2)
(2,3,3)                  112+81 sqrt(2)
(2,2,4)                  -50
(1,2,5), (1,5,2)         2 +/- 5 sqrt(-2)
(1,3,4), (1,4,3)         (1202 +/- 486 sqrt(-1))/125.   (4)
```

These values are pairwise distinct. Their rational minimal factors are
exactly the four factors in (TAC5), proving that the primitive squarefree
color form has degree seven and proving (TAC5)--(TAC6). The full product is
Galois invariant, so its primitive model has rational, hence after clearing
content integer, coefficients.

Finally, since `R` is monic, the root formula gives

```text
Res_T(R(T),Z-f(T))=product_i (Z-f(u_i)).             (3)
```

Its printed coefficients are therefore the elementary symmetric functions
of the three translated values. Formula (TAC8) centers those values, so
(TAC3) is expressible through `s_1,s_2,s_3,U,V` only. The triangular
identities (TSC2) and the scaling (TLR1) give the claimed equation in the
existing core variables. Off (TLR9), (TLR5) has nonzero `b` coefficient;
substitution removes `b` and leaves the four stated equations. QED.
