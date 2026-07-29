# Proof

Write the positive-half conjugate squares as

```text
y_u=|F(zeta_256^u)|^2=18+x_u,
```

where `u` runs over one representative from each conjugate pair. If `A_d`
are the 63 positive-half negacyclic autocorrelations and

```text
E=sum_(d=1)^63 A_d^2,
```

then conductor-256 orthogonality gives

```text
sum_u x_u=0,
sum_u x_u^2=128E,
Norm(F(zeta_256))=product_u(18+x_u).                 (1)
```

All `A_d` are integers. Consequently

```text
sum_d |A_d| <= sum_d A_d^2=E.
```

For `E in {5,6}`, every conjugate therefore satisfies

```text
x_u<=2 sum_d |A_d|<=12.                             (2)
```

A collision has nonzero norm, so also `x_u>-18`.

We next prove the pointwise estimate

```text
log(1+x/18) <= x/18-x^2/925       (-18<x<=12).       (3)
```

Let the left side minus the right side be `g(x)`. Then `g(0)=0` and

```text
g'(x)=x(2/925-1/(18(18+x))).                        (4)
```

Thus `g` increases on `(-18,0)`, decreases on `(0,277/36)`, and increases
on `(277/36,12)`. It remains only to check the right endpoint. The positive
atanh series at `1/4` gives

```text
log(5/3)
 =2 sum_(j>=0) 1/((2j+1)4^(2j+1))
 <49/96+1/2400
 =613/1200
 <1418/2775
 =2/3-144/925.                                      (5)
```

The tail bound in `(5)` replaces every denominator `2j+1`, for `j>=2`, by
`5` and sums the resulting geometric series. Hence `g(12)<0`, proving
`(3)`.

Summing `(3)` over `(1)` yields, for `E>=5`,

```text
log Norm(F(zeta_256))
 <=64 log(18)-(1/925)sum_u x_u^2
 =64 log(18)-128E/925
 <=64 log(18)-128/185.                              (6)
```

The last comparison with the prize floor is also exact. Put `z=128/185`.
The positive exponential series gives

```text
exp(z)>1+z+z^2/2+z^3/6
      >18^64/(1028*p_min).                          (7)
```

The second inequality in `(7)` is an integer cross-multiplication reproduced
by the verifier. Taking reciprocals in `(7)` and applying `(6)` proves

```text
Norm(F(zeta_256))<1028*p_min.
```

This is incompatible with `Norm(F(zeta_256))=1028*p` for an official row
prime `p>=p_min`. Therefore energies five and six are impossible. QED.
