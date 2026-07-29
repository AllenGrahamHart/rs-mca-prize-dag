# Proof

Let `D subset {1,...,63}` be the twelve positive lags. All nonzero
autocorrelation coefficients have magnitude one. Modulo two, the folded
autocorrelation polynomial is

```text
P(X)=sum_(d in D)(X^d+X^(128-d)).                    (1)
```

Its zeroth and first Hasse derivatives vanish automatically. Lucas' theorem
gives

```text
P^[2](1)=sum_(d in D) d mod 2.                      (2)
```

Local multiplicity one for `F` forces exact multiplicity two for `(1)`, so
the number `o` of odd lags in `D` is odd.

## Parity-split cubic cap

In the full oriented support modulo 128, let `O` and `E_0` denote the odd and
even lag sets. Their sizes are

```text
|O|=2o,       |E_0|=e=2(12-o).                     (3)
```

A zero-sum relation has either three even entries or one even and two odd
entries. Choosing two entries determines the third. For three evens, the `e`
opposite ordered pairs force the absent zero entry, giving at most

```text
e^2-e                                                     (4)
```

relations. For one fixed ordering of the `E_0,O,O` type, choosing an even and
an odd gives at most `2eo` possibilities, while choosing the two odds gives
at most `4o^2-2o` after deleting their `2o` opposite pairs. Hence

```text
|M_3| <= e(e-1)+3 min(2eo,4o^2-2o).                 (5)
```

The six possible odd values of `o` give

```text
o:                 1    3    5    7    9   11
right side of (5): 468  396  452  510  354  134.
```

Therefore

```text
M_3<=510.                                           (6)
```

## Cubic Hermite majorant

For one representative from each positive conjugate pair, put

```text
y_u=F(zeta_256^u)F(zeta_256^-u)>0.
```

The conductor-256 moment dictionary and `(6)` give

```text
mean_u y_u=18,
mean_u y_u^2=18^2+24,
mean_u y_u^3<=18^3+3*18*24+510.                    (7)
```

Let `p` be the cubic interpolant matching `log y` and its derivative at
`17` and `40`. Since

```text
log y-p(y)=-(y-17)^2(y-40)^2/(4 xi^4)<=0,           (8)
```

it is a global majorant on `y>0`. Its leading coefficient is

```text
gamma=(1311-1360 log(40/17))/8273560>0.             (9)
```

Substitution of `(7)` therefore yields

```text
mean_u log y_u
 <= (11608/12167) log 17
    +(559/12167) log 40
    -173/44965
 < (1/64) log(514*p_min).                          (10)
```

The verifier proves `(9)--(10)` with 96-term rational atanh intervals. The
positive margin in `(10)` has numerator and denominator bit lengths `27282`
and `27294`. Thus `Norm(F)<514*p_min`, contradicting a cofactor-`514`
prize-row collision. QED.
