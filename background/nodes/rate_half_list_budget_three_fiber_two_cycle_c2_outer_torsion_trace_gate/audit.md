# Audit

1. The subgroup ratio is `t=A/B`, not a square-root ratio; its order divides
   the quotient order `N=2^40`.
2. The trace variable in the cubic is `z=t+t^(-1)+2`, so the recurrence starts
   from `Q_0=Z-2`.
3. Forty, not 39 or 41, doubling steps produce `C_(2^40)`.
4. The terminal test is `Q_40-2`; the recurrence already subtracts two at
   each doubling.
5. Cubic reduction is legal in every harmonic or equianharmonic outer class
   because separability, not `I J!=0`, gives `4I^3-J^2!=0`.
6. A passing outer torsion trace is only necessary. It does not identify an
   actual denominator pair or pay canonical span.

