# Audit

1. Both cubic components are replayed independently.
2. Clearing the denominator is restricted explicitly to `e!=0`.
3. Each completed basis has a one-term monic element at exponent `(0,2)`,
   so the guard contradiction is exactly `e^2=0`.
4. The result is recorded as guard-saturated, not raw-unit.
5. The forced sign disappears in the full signed pair.
6. No source-root, `q`, or interpolation conclusion is asserted.
