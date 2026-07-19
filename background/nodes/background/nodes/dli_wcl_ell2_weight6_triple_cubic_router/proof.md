# Proof

Absorb the signs of a reduced DLI word into its roots. Since `-1 in H`,
this turns a weight-six word into an antipodal-free six-set in `H`.
Scale a selected root to `1` and choose two other roots `x,y`. For this
first triple, write

```text
u=1+x+y,       A=x+y+xy,       B=xy.
```

Let the remaining roots be `z_1,z_2,z_3`, with elementary symmetric
functions `e_1,e_2,e_3`. The first moment gives `e_1=-u`. Put
`e_2=C` and `e_3=d`. The cube sum of the selected triple is

```text
u^3-3uA+3B,
```

while the cube sum of the remaining triple is

```text
(-u)^3+3uC+3d.
```

Since the characteristic is not `3`, their sum vanishes exactly when

```text
d=u(A-C)-B.
```

The product `d=z_1z_2z_3` belongs to `H`. Conversely, selecting
`d in H` determines

```text
C=(uA-B-d)/u=W/u.
```

The denominator is legal: `u=0` would make `{1,x,y}` a reduced
antipodal-free weight-three relation, excluded by hypothesis. The monic
polynomial of the remaining roots is therefore

```text
Q(T)=T^3+uT^2+CT-d.
```

It remains to characterize membership of its roots in `H` without
division. Scale them by `u`, writing `w_i=uz_i`. For powers of two `m`,
put

```text
S_m=sum_i w_i^m,
T_m=sum_(i<j) (w_i w_j)^m,
P_m=(w_1w_2w_3)^m.
```

At `m=1`, the elementary functions of the `w_i` give

```text
S_1=-u^2,
T_1=u^2 C=uW,
P_1=u^3 d.
```

Squaring a three-term sum proves the two coupled identities

```text
S_(2m)=S_m^2-2T_m,
T_(2m)=T_m^2-2P_m S_m.
```

The product identity `P_(2m)=P_m^2` is immediate. Thus the printed
recurrences compute the three power-symmetric functions using only
cyclotomic-integer additions and multiplications.

If every `z_i` belongs to `H`, then `z_i^M=1`, and hence

```text
S_M=3u^M,       T_M=3u^(2M).
```

Conversely, suppose these equations hold. Let `Z_i=z_i^M`. Since
`d in H`,

```text
sum_i Z_i=3,
sum_(i<j) Z_iZ_j=3,
product_i Z_i=d^M=1.
```

Therefore the `Z_i` are the roots of

```text
Z^3-3Z^2+3Z-1=(Z-1)^3,
```

so every `Z_i=1`. Because `F` contains the order-`M` subgroup and
`char(F)` does not divide `M`, all roots of `X^M-1` are the distinct
elements of `H`. Thus the roots of `Q` lie in `H`. The guards are
exactly what makes their union with `{1,x,y}` a reduced antipodal-free
six-set. This proves the router equivalence.

For the norm obstruction, take `x,y,d` to be powers of `zeta_M` in
`O_M=Z[zeta_M]` and define

```text
F_(x,y,d)=S_M-3u^M,
G_(x,y,d)=T_M-3u^(2M).
```

These are integral because the scaled recurrence contains no division. If a
split prime row evaluates `zeta_M` at an exact order-`M` element and the
candidate supports a relation, evaluation kills both `F` and `G`.
Consequently its characteristic divides both principal norms (with a zero
element treated as a separate structural branch). Odd Galois dilation maps
the pair of elements to conjugates and preserves their norms.

There is a useful exact saturation. If an official split characteristic
`q` divided `Norm(u)`, then one conjugate

```text
1+zeta_M^(ai)+zeta_M^(aj)
```

would vanish at one order-`M` embedding modulo `q`. Odd dilation preserves
the legal distinctness and antipodal guards, so this would be a reduced
weight-three zero sum on the official row. The paid weight-three ambient
exclusion forbids it. Therefore an official characteristic supporting the
weight-six candidate divides

```text
g_sat = largest divisor of gcd(|Norm(F)|,|Norm(G)|)
        coprime to |Norm(u)|.
```

Equivalently, repeatedly divide the norm gcd by its gcd with `Norm(u)`.
This removes only a branch already excluded at every conjugate embedding.

The existing pair-orbit certificate counts `1,514` legal normalized
`(x,y)` orbits at `M=1024`. Retaining all `M` possibilities for `d`
therefore gives the stated upper bound `1,514M=1,550,336`. This may
overcount stabilizers, which is harmless for a complete certificate.
