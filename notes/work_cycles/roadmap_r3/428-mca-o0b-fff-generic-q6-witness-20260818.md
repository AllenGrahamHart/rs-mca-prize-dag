## MCA O0b `FFF` generic `q6` witness (2026-08-18)

### Proved result

Let `A` be the certified 16-dimensional generic `q5` quotient over
`K=GF(2130706433)(t)`. The exact regular matrix of `D2` is invertible after
specialization at `t=2`. Hence the quadratic relation

```text
D2 E^2 + D1 E + D0 = 0
```

has the exact 32-dimensional block representation

```text
M_E = [[0, -M_D2^-1 M_D0], [I, -M_D2^-1 M_D1]].
```

The generated program verified the `q7` matrix identity and evaluated the
final necessary equation `q6`. At `t=2`,

```text
det(M_D2) = 1573108971
det(M_q6) = 443644136
```

in the prime field. Both values are nonzero. Consequently `det(M_q6)` is a
nonzero rational function of `t`; multiplication by `q6` is invertible on a
nonempty Zariski-open subset, and the admissible `FFF` necessary subsystem
has no generic solution.

The exact result is Modal app `ap-KU787KXt0DsHdu2SHy4dhq`, result SHA-256
`1757ba06042604cd55e73c923195864ad8214e90fba2ff366574e5d2075f9be7`.

### Remaining specialization boundary

This proves generic emptiness, not all-fiber emptiness. A complete O0b close
still needs to cover every root introduced by:

1. the generic basis and q5 multiplication representation;
2. the q7 coefficient representation;
3. the numerator and denominator of `det(M_D2)`; and
4. the numerator and denominator of `det(M_q6)`.

The timed symbolic phase established that `det(M_D2)` has numerator degree
360 and denominator degree 60, but it did not retain those coefficients and
did not reach the symbolic q6 determinant. The next route should use exact
specialization/interpolation or denominator-cleared polynomial matrices,
with the finite-field witness retained as an independent nonzero anchor.

### Status discipline

The `FFF` chart and its parent O0b node remain open. The new theorem is a
proved dependency that removes the generic component and reduces the chart
to an explicit finite-specialization computation once the determinant
polynomials are reconstructed.
