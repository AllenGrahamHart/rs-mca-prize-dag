# Proof - L1 Mersenne HNF m=8 order-one cubic two-triple exclusion

Retain the normalized cubic `e=W^3+uW^2+vW+w` and the factorization

```text
L=e^2-se+t                                             (1)
```

from the dependency. In addition to its previously used coefficients,
comparison at `W^2` gives

```text
l_4=v^2+2uw-su=v^2+u(l_3-2uv).                       (2)
```

The HNF coefficients are

```text
u=3/d,
v=(12+rd)/(4d^2),
l_3=(20+rd(d+8)/3)/d^3,
l_4=(15+rd(d^2+7d+23)/4+r^2d^2/8)/d^4.              (3)
```

Substitution of (3) into (2), followed by multiplication by `16d^4`,
leaves

```text
rd(4(d^2+3d+3)+rd)=0.                               (4)
```

The inherited saturation has `r*d!=0`, proving (CTE1). Put

```text
s=d^2+3d+3,       S=2d^2+9d+9.                      (5)
```

Thus `r=-4s/d`. Substitution into the h=7 conic from the dependency gives

```text
35d^2r^2+14d(11d^2+27d+27)r
 +120(d^4+4d^3+7d^2+6d+3)=32sS.                    (6)
```

Substitution into its second quadratic gives

```text
q_2r^2+q_1r+q_0=-8d(d+2)S.                          (7)
```

Both left sides vanish. If `S!=0`, equations (6)--(7) force `s=0` and
`d=-2`; but `s(-2)=1`. Hence `S=0`, and

```text
S=(2d+3)(d+3),                                      (8)
```

which proves (CTE2).

Every official characteristic satisfies `p=7 mod 8`. Therefore

```text
F_p intersect mu_8=mu_gcd(p-1,8)=mu_2={1,-1}.       (9)
```

If `d=-3`, then `d^(p+1)=d^2=9`, which can equal `1` or `-1` only in
characteristic `2` or `5`. If `d=-3/2`, its norm is `9/4`, which can equal
`1` or `-1` only in characteristic `5` or `13`. None of the four official
primes is `2`, `5`, or `13`. This contradicts the inherited condition
`d^(p+1) in mu_8` and excludes the chamber. QED.
