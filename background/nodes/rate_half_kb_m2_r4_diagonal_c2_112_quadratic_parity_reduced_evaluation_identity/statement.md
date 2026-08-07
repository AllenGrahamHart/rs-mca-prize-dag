# Statement

Let

```text
R = U^2 - V Z,
P(w) = sum_(i=0)^d a_i w^i,
C_P = V^d P(-U/V) = sum_i a_i (-U)^i V^(d-i).
```

Then, modulo `(R)`,

```text
C_P =
  sum_(2j<=d)   a_(2j)   V^(d-j)   Z^j
  - sum_(2j+1<=d) a_(2j+1) U V^(d-j-1) Z^j.
```

The right side is polynomial, uses `U` only to exponent zero or one, and
does not divide by `V` or any coefficient of a quadratic row.
