# Proof - L1 Mersenne HNF m=8 order-one cubic three-double x=0 quintic reduction

At `x=0`, formula (TLR4) gives

```text
B_5=6+q(d^2+5d+11)/2+q^2(d+5)/12.                 (1)
```

Insert (1) and the printed `G` in (TLR5). The constant terms cancel, and
collection by powers of `q` yields

```text
M_5=q(d+2)
 [D/5+qC/12+5q^2/24],                              (2)
```

which is (XQ2). Since `q=dr` and both `d` and `r` are saturated, `q` is
nonzero.

If `d=-2`, its base-field norm is `4`. Every official prime is `7 mod 8`,
so the base-field eighth roots are only `1,-1`; `4` equals neither in an
official characteristic. Hence take `J=0`.

Using (XQ1), direct subtraction gives

```text
A-C=-(2d+3)(d+2),
25B-7D=-(2d+3)P.                                   (3)
```

Equations (3) prove (XQ4). If `d=-3/2`, its base-field norm is `9/4`, which
can equal `1` or `-1` only in characteristics `5` or `13`. These are not
official. Since `d=-2` has already been removed, the other factor in (XQ4)
gives (XQ5).

Substitute (XQ5) in `C_0` and clear `35(d+2)^2`. Expansion gives

```text
144P^2-168AP(d+2)+4200B(d+2)^2
 =-24(d+3)P_5(d),                                  (4)
```

which is (XQ6). At `d=-3`, the base-field norm is `9`; equality with `1` or
`-1` can occur only in characteristics `2` or `5`, again not official.
Every survivor therefore satisfies `P_5(d)=0`. The inherited norm-color
condition is (XQ8), so the stated gcd family is exhaustive. The unused
quadratic-in-`b`, sixth-coefficient, color-ratio, and Frobenius conditions
can only remove roots from this necessary endpoint. QED.
