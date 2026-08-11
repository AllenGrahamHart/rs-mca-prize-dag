# `A=1` core-one general middle-Hankel adjugate factorization

- **status:** PROVED
- **closure:** primitive-kernel adjugate factorization and local Smith ledger
- **consumer:** `rate_half_band_crossing_location`

Retain any live half-distance `A=1` profile with fixed core `s=1`. Put

```text
d=rho-1,       Delta=d-2e.                            (GMA1)
```

After core contraction, the residual divided-power form has degree `2d`.
Its middle catalecticant is a square symmetric Hankel pencil

```text
M(U,V),       size (d+1) x (d+1),
rank_(F(U/V)) M=d.                                    (GMA2)
```

Let `q(U,V)` be the primitive homogeneous degree-`e` coefficient vector of
the residual apolar generator. Then there is a nonzero homogeneous form
`D(U,V)` of degree `Delta`, unique up to scalar, such that

```text
Mq=0,       adj M=D q q^T.                            (GMA3)
```

The gcd of every nonzero maximal minor is exactly `D`. Up to a nonzero
scalar, `D` is the determinant of the size-`Delta` regular Kronecker block.
If `c_gamma` is the residual rank loss at a projective parameter `gamma`,
then

```text
c_gamma<=ord_gamma(D),       sum_gamma c_gamma<=Delta. (GMA4)
```

Let `P_p` be the pushforward to the parameter line of the pole-cancellation
scheme for the residual-domain-locator ratio, and let `p=deg P_p`. Then

```text
P_p<=div(D),       D=P_p E_D,       deg E_D=Delta-p.   (GMA5)
```

The factor notation in `(GMA5)` identifies effective divisors with their
homogeneous forms, up to nonzero scalars.

## Scope

No squarefreeness of `D`, equality between rank loss and `ord(D)`, or
profile exclusion is asserted.
