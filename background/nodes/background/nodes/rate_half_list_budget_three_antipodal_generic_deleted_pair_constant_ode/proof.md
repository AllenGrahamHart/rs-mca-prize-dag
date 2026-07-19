# Proof

The even-factorization dependency says that the reverse polynomials `B` and
the normalized reverse of `V` are even. Since

```text
B(z)=z^rU(z^-1),       r=4M-1,
Cbar(z)=c z^vV(z^-1),  v=2M-2,       c!=0,            (1)
```

reversing an even polynomial at odd degree makes an odd polynomial, while
reversing at even degree preserves evenness. The deleted divisor is even as
well. This proves `(COD1)` and its degree assertions.

The split outer quartic in the same dependency has two opposite root pairs.
After absorbing the harmless normalization scalar from `(1)`, its product in
the original coordinate is

```text
(U^2+lambda V^2)(U^2+mu V^2),                        (2)
```

with `lambda,mu` distinct and nonzero. Substitute `(COD1)` into the original
norm equation

```text
D product_i(U+c_iV)=Y^(16M)-1.                        (3)
```

Equation `(3)` becomes `(COD2)` because `Y^(16M)=x^(8M)`.

On the generic minimum-degree boundary the reverse-residual dependency gives

```text
T=dDU-Y(D'U+4DU')                                    (4)
```

nonzero of exact degree one. In `(COD1)`, `D` is even and `U` is odd. Both
terms in `(4)` are therefore odd, so `T=kappa Y` for a nonzero scalar
`kappa`. Now

```text
D'=2Y D_0',       U'=U_0+2xU_0'.                     (5)
```

Substitution of `(5)` into `(4)` and division by `Y` gives `(COD3)`.

Expand `(COD3)` using `(COD4)`. The coefficient of `x^j` is

```text
d_0(16M-4-8j)u_j
 +d_1(16M+2-8j)u_(j-1)
 +(16M+8-8j)u_(j-2),                                 (6)
```

which proves `(COD5)`. For `1<=j<=2M-1`, the coefficient of `u_j` in `(6)`
is nonzero: its integer representative lies between `4` and `16M-12`, while
the characteristic exceeds `d=16M`. Since `d_0!=0`, these equations determine
the coefficients successively from `u_0`. At `j=2M`, the absent coefficient
`u_(2M)` leaves

```text
2d_1u_(2M-1)+8u_(2M-2)=0,
```

which is `(COD6)`; the next coefficient vanishes identically and there are no
further conditions. The constant coefficient is `(COD7)`. Both `d_0` and
`kappa` are nonzero, so `u_0!=0`.

For completeness, the differential operator in `(COD3)` has no nonzero
polynomial of degree at most `2M-1` in its homogeneous kernel. If such a
polynomial has first nonzero term `a x^ell`, its lowest coefficient in the
homogeneous equation is

```text
d_0(8ell-(16M-4))a.
```

For `0<=ell<=2M-1`, its nonzero integer factor has absolute value between
`4` and `16M-4`, strictly below the characteristic. Therefore two solutions
with nonzero constants are proportional: cross-multiplying them by their
constants gives a homogeneous-kernel element of degree at most `2M-1`.
Monicity removes the proportionality, proving uniqueness of `U_0` for fixed
`D_0`.

Finally `u_0!=0` makes the root `Y=0` of `U=YU_0(Y^2)` simple. The
reverse-residual theorem says that every repeated root of `U`, and every root
shared by `U` and `D`, is a root of `T`. But `T=kappa Y` has no nonzero root.
Thus all other roots of `U` are simple and avoid `D`. QED.
