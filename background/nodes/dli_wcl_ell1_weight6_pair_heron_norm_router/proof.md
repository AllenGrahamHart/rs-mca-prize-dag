# Proof

For arbitrary `A,B,C`, direct multiplication gives the Heron identity

```text
(A+B+C)(A+B-C)(A-B+C)(A-B-C)
  = H(A^2,B^2,C^2).                                    (1)
```

Fix internal signs `tau_1,tau_2,tau_3` and put

```text
A=r_1+tau_1 r_2,
B=r_3+tau_2 r_4,
C=r_5+tau_3 r_6.                                      (2)
```

The four factors on the left of `(1)` are the four external pair-sign
choices modulo global negation. Their product is `H_tau`, because

```text
A^2=U_1(tau_1), B^2=U_2(tau_2), C^2=U_3(tau_3).       (3)
```

As `tau` ranges over eight internal choices and the external signs range
over four choices, the resulting sign vectors with the sign of `r_1` fixed
positive are

```text
(1, tau_1, delta_2, delta_2 tau_2,
    delta_3, delta_3 tau_3).                           (4)
```

This is a bijection from `{+/-1}^3 x {+/-1}^2` to all 32 global-sign
classes. Multiplying `(1)` over the eight internal choices therefore proves
`(PH3)`.

Each change `t_j -> -t_j` exchanges `U_j(+)` and `U_j(-)`. Consequently the
eight factors in `(PH3)` are exactly the conjugates under the three quadratic
relations `t_j^2=y_(2j-1)y_(2j)`. Their product is the determinant norm from
`L` to `R`; the identity can be checked over the fraction field and then
descends polynomially over `Z`.

Over a field of odd characteristic, `(1)` is a product identity with no
denominators. Hence `H_tau=0` exactly when one of its four factors vanishes.
The bijection `(4)` proves the signed-lift partition. Multiplicativity of
cyclotomic norms then shows that the union of rational prime supports across
the eight `H_tau` is exactly the prime support of `Psi_6`. Relabeling the
roots proves the same statement for all 15 pairings. QED.
