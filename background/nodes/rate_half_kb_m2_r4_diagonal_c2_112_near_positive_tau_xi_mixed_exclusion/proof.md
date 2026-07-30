# Proof

Use the parent positive fixed-moving reconstruction. At either root `r=c,d`
of `q`, divide the endpoint norm by `(W-w)^2` and write the residual as
`A_r W^2+B_r W+C_r`. Condition `(KBNTM-1)` is equivalent to

```text
C_r-2A_r/d=0,
B_r+(2+1/d)A_r=0.                                (1)
```

The direct checker verifies the exact source determinant and both forced
roots. After removing the finite-chart factor `H^2` from the product
conditions, the four equations in `(1)` are primitive quadratics in `b`, of
degrees `(2,6,5)` for product and `(2,10,7)` for sum in `(b,c,d)`.

Eliminating `b` between product and sum over either q-root gives the same
bidegree-`(8,6)` residual curve after the printed collision, inversion-fixed,
`z=1`, and finite-boundary factors are removed. The two cross-product
conditions leave factors of bidegrees `(2,1),(6,5)`; the two cross-sum
conditions leave `(1,1),(4,3),(10,8)`. Thus every retained solution lies on
the residual curve, one product factor, and one sum factor.

Eliminate `c` between the residual curve and each retained cross factor.
The aggregate product and sum projections have degrees 96 and 186, and their
squarefree gcd is `(KBNTM-2)`. The independent checker reconstructs with
`DomainMatrix.solve_den`, verifies its matrix identity, eliminates `d`, and
gets `(c-2)(c-1)(2c-1)`. Both checkers clear denominators and reproduce these
gcds modulo `2130706433`. Resultants are used only in their necessary
direction. All projected roots are forbidden, so no admissible solution
exists. QED.
