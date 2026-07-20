# Audit

The following details are load-bearing.

1. `G` must be monic. Triangular quotient uniqueness uses its leading
   coefficient being exactly one over arbitrary commutative rings.
2. `Q_t` has degree at most `w-2`, while `V_t` has degree less than `w`.
3. `V_0=Y` is fixed; only `V_1,...,V_m` contribute variables.
4. There are `2w-1` coefficient equations per squaring and `w` terminal
   equations.
5. The degree-three bound counts base and auxiliary variables together;
   it uses the proved fact that every coefficient of `G` has base degree at
   most two.
6. The scheme claim survives base change because monic division is
   triangular, not because field-valued points happen to correspond.
7. A lifted unit ideal proves existence of an integer certificate. It does
   not supply that integer or show that a generic Groebner basis is feasible.
8. In the pruned system `2^s<w`, not `2^s<=w`; `V_s` is fixed and `V_m` is
   substituted. Neither polynomial contributes variables.

Expanded quotient remainders remain useful as small independent checks, but
they are no longer required inputs to the certificate computation.
