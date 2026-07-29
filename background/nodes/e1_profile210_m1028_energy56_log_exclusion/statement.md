# E1 profile-(2,10) cofactor-1028 energy-five/six exclusion

- **status:** PROVED
- **closure:** bounded-deviation logarithm majorant with exact rational margins
- **scope:** binding prize rate-`1/8` row, profile `(2,10,S=18)`, cofactor `1028`

No profile-`(2,10,S=18)` collision on a prize-envelope row with cofactor

```text
m=1028=4*257
```

has positive-half autocorrelation energy `E=5` or `E=6`.

For these energies, integrality bounds every conjugate deviation above by
`12`. On the full interval `-18<x<=12`,

```text
log(1+x/18) <= x/18-x^2/925.
```

The exact first and second conjugate moments therefore give

```text
log Norm(F(zeta_256)) <= 64 log(18)-128/185
                       < log(1028*p_min).
```

Thus a cofactor-`1028` collision can survive only at energies `2`, `3`, or
`4`. This node does not assert that any of those three energies occurs.
