# Proof - L1 Mersenne HNF m=8 order-one conic reduction

For `h=7`, the hypergeometric series is

```text
U(t)=(1-t)^(c rho)(1-ct)^(-rho).
```

Its logarithm has no linear term and is

```text
log U(t)=rho sum_(j>=2) (c^j-c)t^j/j.                (1)
```

Only four partitions of seven use parts at least two: `7`, `5+2`, `4+3`,
and `3+2+2`. Therefore

```text
Phi_7=[t^7]U
 =rho(c^7-c)/7
  +rho^2(c^5-c)(c^2-c)/10
  +rho^2(c^4-c)(c^3-c)/12
  +rho^3(c^3-c)(c^2-c)^2/24.                        (2)
```

Factor `rho*c*(c-1)*(c+1)` from (2). The remaining factor is

```text
(c^4+c^2+1)/7
 +rho*c*(c-1)(11c^2+5c+11)/60
 +rho^2*c^2*(c-1)^2/24.                             (3)
```

The dependency normalizes

```text
7!*Phi_7=6*rho*c*(c-1)*(c+1)*Psi_7.
```

Multiplying (3) by `840`, and using the definitions in (OCR1), gives
exactly (OCR2). This also expands to ten terms, agreeing with the independent
term-count and digest packet in the dependency.

Five times (OCR2) is

```text
175u^2+70Au+600B=0.                                  (4)
```

Completing the square gives

```text
7(5u+A)^2=7A^2-600B.                                (5)
```

Direct expansion of the right side is the polynomial `D(c)` in (OCR3),
proving (OCR4). All official characteristics exceed seven, so the divisions
and the equivalence with (OCR2) are valid.

Divide (OCR4) by `c^2`. Since

```text
c^2+c^(-2)=z^2-2,
A/c=11z+5,
u/c=rho(c-1),                                        (6)
```

the result is (OCR6), with `w` as in (OCR5). Conversely, (OCR5)--(OCR6)
multiply back to (OCR4), so no component is lost when `c!=0`.

At `z=-1`, the right side of (OCR6) is `252=7*6^2`. Intersecting the line
`w=6+t(z+1)` with the conic gives one known root `z=-1`; the other root is
the pair of rational functions in (OCR7), by direct linear-factor division.
Finally `z=c+c^(-1)` is equivalent to (OCR8), and (OCR5) solves for `rho`
because `5(c-1)` is nonzero on the order-one chamber. QED.
