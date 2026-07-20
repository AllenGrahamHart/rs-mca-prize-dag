# Claim contract

## Proved

- The half-order swap divisor condition has an exact repeated-squaring
  presentation over `Z`.
- The pruned presentation has the variable, equation, and degree bounds in
  `(SLC4)`.
- Every fixed `(N,h)` presentation is a characteristic-zero unit ideal and
  therefore admits a nonzero integer bad-characteristic certificate.

## Consumer

`f3_hge4_norm_gate_count`, through the primitive swap route.

## Falsifier

A base ring on which `(SLC1)` and `(SLC2)` define different solution schemes,
or a characteristic-zero divisor `YT^2-c | Y^N-1` at odd `h`, falsifies the
theorem.

## Nonclaims

- No integer `Delta_(N,h)` is computed or factored.
- No official characteristic is excluded.
- No survivor count, cross-width transfer, or free-union bound is proved.
- Cubic equations do not imply cheap Groebner elimination.
