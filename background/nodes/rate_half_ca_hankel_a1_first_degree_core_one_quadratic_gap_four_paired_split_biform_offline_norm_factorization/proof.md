# Proof

The argument is the same in both profiles. We first prove it with the
abstract notation `(ONF1)--(ONF2)`.

For every `x in M`, the split-row theorem gives

```text
G(t,x)=lambda_x product_(delta in A_x)(t-delta),
lambda_x!=0,       A_x subset Sigma_off,       |A_x|=m.       (1)
```

The roots in `(1)` are distinct. Therefore exactly `m` factors in

```text
N_G(X)=product_(delta in Sigma_off)G(delta,X)         (2)
```

vanish at `X=x`. Each contributes at least one copy of `X-x`, so

```text
(X-x)^m divides N_G(X).                              (3)
```

The rows in `M` are distinct. Multiplying `(3)` over them proves

```text
L_M(X)^m divides N_G(X).                             (4)
```

No factor in `(2)` is the zero polynomial. If `G(delta,X)` vanished
identically, then `delta` would be a root of every row polynomial in `(1)`.
By the row-root dictionary, the actual support `S_delta` would contain all
of `M`. It also contains the fixed core point `s_0`, which is not in `M`.
In the extremal profile `|M|>=3p-3>2p-1=rho-1`; in the strict profile
`|M|=2p+r_A=rho+r_A`. Hence `|S_delta|>=|M|+1>rho`, a contradiction.
Thus `N_G` and the quotient `S_G` in `(ONF3)` are nonzero.

Every factor in `(2)` has `X`-degree at most `n`. Hence

```text
deg N_G<=T_off*n.                                    (5)
```

Subtracting the degree `R*m` of `(4)` proves `(ONF3)`. Notice that `(3)`
uses polynomial vanishing order, not only a set-theoretic root count. Any
additional multiplicity remains in `S_G`.

Since the product is nonzero, its degree is the sum of its factor degrees.
Writing `q_delta=n-deg_X G(delta,X)` gives

```text
deg N_G=T_off*n-sum_delta q_delta,                  (5a)
```

and `(ONF3a)` follows. The top `X`-coefficient of `G` is a nonzero
parameter polynomial of degree at most `m`. Every slope with `q_delta>0`
is one of its distinct roots, so there are at most `m` such slopes. The
exact padded-fiber factorization has degree `n`, proving `q_delta=0` on
every selected fiber.

For the extremal profile, substitute `(ONF4)` into `(ONF3)`:

```text
T_off*n-R*m
 =3e(p-3)-(3p-3+d_A)(e-2)
 =(3-d_A)e-9+2d_A,                                  (6)
```

where the last equality uses `2p=3e-1`. This proves `(ONF5)`, and direct
substitution of the official `e` gives `(ONF6)`.

For the strict profile, the same calculation gives

```text
(3e+1)(p-2)-(2p+r_A)(e-1)
 =[3e^2-4e-7-2r_A(e-1)]/2,                         (7)
```

which proves `(ONF12)--(ONF13)`.

It remains to locate the selected fiber factors. The padded-fiber theorem
gives, for every `delta in Z_0`,

```text
G(delta,X)=zeta_delta F_delta(X),       zeta_delta!=0.         (8)
```

Split `F_delta` into the product of its roots in `M` and the complementary
factor `J_delta`. Every root of `J_delta` lies outside `M`, whereas every
root of `L_M` lies in `M`; hence

```text
gcd(J_delta,L_M)=1.                                  (9)
```

Multiplying `(8)` over `Z_0` shows that `product J_delta` divides `N_G`.
Equations `(4)` and `(9)` then imply that it divides `S_G`, including all
multiplicities. This proves `(ONF8)`. Padded-heavy roots lie outside `U_0`
and therefore outside `M`, so every `R_delta` divides `J_delta`. In the
extremal `d_A=1` profile, the source partition gives `M=U_0`; consequently
the roots of `A_delta` outside `M` are empty and `J_delta=R_delta`.

## Local reconstruction of the extremal residual

Fix `x in M` and divide the product `(2)` by `(X-x)^m`. Exactly the factors
indexed by `A_x` vanish at `x`. For one such factor,

```text
[G(delta,X)/(X-x)]_(X=x)=partial_X G(delta,x).       (10)
```

The factors indexed by the complement of `A_x` are nonzero at `x`.
Therefore

```text
[N_G(X)/(X-x)^m]_(X=x)=D_x.                         (11)
```

On the other hand, `(ONF3)` gives

```text
[L_M(X)^m S_G(X)/(X-x)^m]_(X=x)
 =L_M'(x)^m S_G(x).                                 (12)
```

Comparing `(11)` and `(12)` proves `(ONF10)`. If one incident fiber has
root multiplicity at least two at `x`, its derivative vanishes, the left
side of `(11)` vanishes because the norm has order greater than `m`, and
the same formula still applies.

For `d_A=0`,

```text
R-(3e-9)=(3e+9)/2>0,                                (13)
```

and for `d_A=1`,

```text
R-(2e-7)=(5e+7)/2>0.                                (14)
```

Thus `deg S_G<R` in both extremal profiles. Lagrange interpolation on `M`
using the values `(ONF10)` is exactly `(ONF11)`.

For completeness, we calibrate the extremal degree cap before closing the
proof. The three-center minimum-word ledger gives, for every off-line
slope,

```text
|S_delta intersect U_0|=p-3-r_delta-a_delta
                         =n-r_delta-a_delta.        (15)
```

If `d_A=1`, `M=U_0`. If `d_A=0`, the classified rows omit only
`x_circ`, so with `b_delta` as in `(ONF11a)`,

```text
i_delta:=|{x in M:G(delta,x)=0}|
 =n-r_delta-a_delta-b_delta.                        (16)
```

Summing `(16)` over all off-line slopes counts the same grid incidences as
summing the `m` roots of every classified row, and hence

```text
R*m=sum_delta i_delta.
```

Rearranging and using `(ONF5)` proves `(ONF11a)`. Combining it with
`(ONF3a)` proves `(ONF11b)`, and completes the proof. QED.
