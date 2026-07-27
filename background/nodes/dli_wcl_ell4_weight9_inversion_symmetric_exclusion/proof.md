# Proof

Write

```text
A=Y^4+c3 Y^3+c2 Y^2+c1 Y+c0,   x=c0,   z=c1.
```

The monic degree-nine polynomial `P=YA^2-1` has constant term `-1`, so the
product of its roots is one. If its root set is inversion-invariant, then

```text
Y^9 P(1/Y)=-P(Y).
```

The four nontrivial coefficient equations are

```text
x^2+2c3=0,
2xz+2c2+c3^2=0,
2xc2+z^2+2z+2c2c3=0,
2xc3+2x+2zc2+2zc3+c2^2=0.                 (1)
```

Outside characteristic two, the first two equations give

```text
c3=-x^2/2,             c2=-xz-x^4/8.                    (2)
```

After substitution, clear denominators from the last two equations to get

```text
Q = x^6-2x^5+8x^3z-16x^2z+8z^2+16z,
R = x^8+16x^5z-16x^4z-64x^3
    +64x^2z^2-64x^2z-128xz^2+128x.
```

Cancelling the quadratic term in `z` gives the necessary linear equation

```text
L = 7x^8-32x^7+32x^6+48x^5z-240x^4z+256x^3z
    +64x^3+192x^2z-256xz-128x.                         (3)
```

The exact resultant is

```text
Res_z(Q,L)=8 x^2(x-2)^2
  (x^3-6x^2+8)(x^3-6x^2+24)
  (x^3-12x-8)(x^3-12x+8).                              (4)
```

Thus, outside characteristic two, every candidate lies on one of six
parameter factors. The two linear factors give four rational branches:

| `x` | `z` |
|---:|---:|
| `0` | `0` or `-2` |
| `2` | `0` or `-2` |

On the four cubic factors the coefficient of `z` in `(3)` is invertible
except in the following characteristics, and the unique branches are

| cubic factor | `z` | exceptional resultant support |
|---|---|---|
| `x^3-6x^2+8` | `2-x^2` | `{2,3,17}` |
| `x^3-6x^2+24` | `4-x^2` | `{2,3,17,19}` |
| `x^3-12x-8` | `-2x-2` | `{2,3,17,19}` |
| `x^3-12x+8` | `-2x` | `{2,3,17}` |

For every branch, compute the exact remainder

```text
Y^1024-1 mod P = sum_(j=0)^8 r_j Y^j.                  (5)
```

On a rational branch, divisibility forces the characteristic to divide the
gcd of the nonzero integer numerators of the `r_j`. On a cubic branch with
parameter polynomial `f`, it forces the characteristic to divide every
`Res_x(f,numer(r_j))`, hence their gcd. Exact repeated squaring gives

```text
branch obstruction gcds = 1,1,1,1,1,1,1,1.            (6)
```

The router, parameter inverses, and coefficient denominators introduce only
the primes

```text
{2,3,17,19}.                                          (7)
```

Equations `(4)--(7)` prove the first assertion. Finally

```text
v2(2-1)=0, v2(3-1)=1, v2(17-1)=4, v2(19-1)=1,
```

so no exceptional characteristic meets the official split gate
`v2(p-1)>=41`. QED.
