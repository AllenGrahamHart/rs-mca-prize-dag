# Proof

Write `q_i(X)=H(alpha_i,X)`. By the product formula for resultants,

```text
Res_T(P_J,H) ~ product_(j in J) q_j,
Res_T(P_I,H) ~ product_(i in I) q_i.                (1)
```

All divisor counts below include pullback multiplicity.

At every point above `K`, the component star is `J-J`. The product of the
six `J` rows therefore has local order twice the local order of `D_K`.
The `eta` fiber is `I-I`, so it contributes nothing to the `J` row product.

At a point above `L^c`, the source facet has five `I` roots and one
exchanged `J` root. The component contributes that `J` root exactly when
the corresponding pole-graph edge is colored by `H`. Corollary 9.28 says
that a source-degree-two component colors exactly four edges, all at simple
free-deck pole roots. Let their effective divisor be `C_H`. There are no
other `J` incidences outside `K`. Consequently

```text
div product_(j in J)q_j = 2 div(D_K)+div(C_H).      (2)
```

This proves `(KBCR-1)` through `(1)`. It also proves that `C_H` is a
squarefree degree-four subdivisor of the pullback over `L^c`.

Complete-source saturation gives

```text
product_(i in I)q_i product_(j in J)q_j ~ B^2.     (3)
```

Since `B=D_K D_R`, dividing `(3)` by `(KBCR-1)` and clearing `C_H` gives
`(KBCR-2)`. This argument is valid even over ramified `K` or `eta` fibers,
because `(2)--(3)` are divisor equalities.

Finally, Corollary 9.28 colors an edge `(j,ell)` precisely when the root at
the opposite pole point lies on the `j` row of `H`. The two edge roots
incident to the left pole-graph vertex `j` form the divisor `E_j=bZ_j`.
Thus the number `c_j` of outside-`K` incidences of source label `j` is
exactly `deg gcd(C_H,E_j)`, proving `(KBCR-3)`. QED.
