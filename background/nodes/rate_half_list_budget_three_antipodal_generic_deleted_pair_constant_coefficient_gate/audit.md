# Audit

The variable `x` is the original half-degree polynomial coordinate. The
variable `z` appears only in the reversal formula, and `chi` is the source
trace. Keeping these three symbols separate is essential.

The normalization `D_0=(x-1)(x-t)` comes from the same source-lift
normalization as the Mobius router. Replacing `t` by its reciprocal requires
the corresponding common source rescaling; it must not be done in `(CCG3)`
without transforming `S` as well.

The formula for `sigma` uses the top `s+1` coefficients of `R` and `A` via
reversal. It does not claim that a constant coefficient of the ordinary
power-series quotient `R/A` exists, since `A(0)=0`.

Passing `(CCG3)` is only necessary. It checks one coefficient of the full
scalar identity and says nothing by itself about the torsion trace, gcd, or
fourth-power gates.

A contributor computation remains inappropriate until the terminal
coefficient has a compressed recurrence, diagonal, or other representation
that avoids a length-`2^36` array.
