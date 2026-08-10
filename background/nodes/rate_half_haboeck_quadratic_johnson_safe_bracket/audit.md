# Audit

1. The reduced rate is `(k-1)/n`, matching a degree-less-than-`k` code.
2. The real theorem bound is converted to an integer numerator by taking its
   floor. Safety needs `Q_m<=floor(q/2^128)`; no real-valued budget shortcut
   is used.
3. The real agreement threshold is rounded upward. Both `a_m` and `a_m-1`
   are checked by exact squared inequalities.
4. The `q<2^256` cutoff is strict, hence `B*<=2^128-1`. The `m=95/96`
   boundary is checked against that integer.
5. The theorem is field-general and domain-general. Smoothness, primality,
   and the six official extension-degree strata introduce no extra premise.
6. `a_m` is only a safe point. Monotonicity places the exact crossing at or
   below it but supplies no unsafety at `a_m-1`.
7. The stronger BCHKS25 linear error term is deliberately absent.
8. `verify_audit.py` checks the hard-coded landmarks independently of the
   search routine in `verify.py`.
