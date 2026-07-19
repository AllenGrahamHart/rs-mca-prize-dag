# Result

The exact fourth-power branch carries an additional differential signature.
Its fourth root is not an arbitrary degree-`M-1` divisor: it must divide the
single ODE polynomial `2N+kappa x^2U_0^3`. Equivalently, the already-computed
Euclidean quotient `S` must divide the square of that polynomial and share a
gcd of degree at least `M-1` with it.

CR-002 should apply this inexpensive algebraic rejection gate before seeking
or certifying a fourth root. A contributor implementation should return a
compact modular remainder and gcd certificate, not a dense square `P^2`.

Uniform failure is still open. No compute is authorized until `S` and the ODE
polynomial have a compressed official-scale representation.
