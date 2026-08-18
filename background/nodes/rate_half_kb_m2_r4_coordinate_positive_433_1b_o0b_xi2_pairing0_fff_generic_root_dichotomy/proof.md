# Proof

On the guarded ratio graph, the `q5` quotient is a 16-dimensional algebra
over `F_2130706433(t)`. Eliminating `E` from `q7,q6` gives
`R76=Res_E(q7,q6)`. If a common `q5,q7,q6` zero exists, multiplication by
`R76` in the `q5` quotient cannot be invertible.

The exact column-cleared 16 by 16 multiplication matrix has determinant of
degree 19060 with 18711 nonzero coefficients. Its independently checked
values at `t=2,3` are nonzero, and exact NTT reconstruction commits every
coefficient. Therefore it is not the zero polynomial and the generic
necessary system is empty wherever the transformations and determinant are
nonzero.

The exceptional-root ledger takes the monic LCM of every denominator and the
determinant, computes its gcd with `t^p-t`, and factors the square-free result.
It finds exactly the fourteen printed roots. The determinant group itself has
all fourteen and contains every denominator-root group. Hence no base-field
fiber outside the list can escape the generic proof. QED.
