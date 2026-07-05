# e22_fixed_tail_local_saturation

- **status:** CONDITIONAL
- **closure:** proof

## Statement

For E22 mixed/full-petal challengers satisfying the petal-locator divisibility
constraints

```text
L_{T_i}(X) | U(X)L_{Z\C}(X) - a_i L_{C\Z}(X),
```

the divisor constraints isolate:

- one exceptional tail `B`;
- local dyadic quotient moduli `M_i > t`;
- and local non-tail blocks that are unions of full fibers of `x -> x^{M_i}`;

with `|B| < min_i M_i`.

This is reduced to:

- `e22_local_quotient_factor_extraction`: extract the common tail, the tail
  bound, and local quotient factors `X^{M_i}-z` from the cofactors;
- `e22_fiber_locator_saturation`: convert those quotient factors into full
  local quotient-fiber blocks.

## Falsifier

A family of petal divisor constraints whose non-tail roots cannot be separated
into one common tail plus locally saturated dyadic quotient-fiber blocks.
